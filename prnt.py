import requests
from time import sleep
import re
from bs4 import BeautifulSoup as bs
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["printds"]
col = db["ids"]

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
headers = {
    "content-type":"text",
    'User-Agent':user_agent
}

def sendReq(id,rec):
    res = requests.get(f'https://prnt.sc/{id}', headers=headers)
    soup = bs(res.text, 'html.parser')

    img = soup.find(class_="no-click screenshot-image")
    img_src = img["src"]
    if img_src=="//st.prntscr.com/2020/05/14/1716/img/0_173a7b_211be8ff.png":
        newvalues = { "$set": { "checked": True } }
        col.update_one(rec, newvalues)
    elif img_src=="http://img404.imageshack.us/img404/899/8f2d0ddc979a4594804d7a7.png":
        newvalues = { "$set": { "checked": True} }
        col.update_one(rec, newvalues)
    elif re.search(r'.*', img_src):
        newvalues = { "$set": { "checked": True, "source": img_src, "status": True } }
        col.update_one(rec, newvalues)
    else:

        newvalues = { "$set": { "checked": True} }
        col.update_one(rec, newvalues)

def starter():
    count = 1
    for record in col.find({ "checked": False }):
        count += 1
    print(f'Start:{count} documents left to check')
    goThru(count)


def goThru(counter):
    for record in col.find({ "checked": False },no_cursor_timeout=True):
        end_id = record['img_id']
        if re.search(r'^0.*', end_id):
            continue
        elif re.search(r'.*', end_id):
            sendReq(end_id, record)
            sleep(20)
            counter -= 1
            print(f'{counter} documents left to check')
        else:
            print("stopping the operation")
            break 
    # cursor.close()

def writeImg():
    with open('Sources.txt', 'w') as f:
        for record in col.find({ "status":True }):
            sources = record["source"]
            print('', sources, file=f)

starter()
# writeImg()




#use lxml parser later for speed
