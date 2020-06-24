import React from "react";
import "./retrieve.css";

export default class Retrieve extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      source: "http://localhost:5000/images/placeholder",
    };
    this.sendRec = this.sendRec.bind(this);
  }

  sendRec = () => {
    fetch("http://localhost:5000/api", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) =>
        response.forEach((object) => {
          console.log(object.source);
          this.setState({
            source: object.source,
          });
        })
      );
  };

  Initiate = () => {
    this.sendRec();
  };

  render() {
    return (
      <div className="image-wrap">
        <h1>Randomize an image</h1>
        <img
          className="main-image"
          referrerPolicy="no-referrer"
          onClick={this.Initiate}
          src={this.state.source}
          alt="random pic lol"
        />
      </div>
    );
  }
}
