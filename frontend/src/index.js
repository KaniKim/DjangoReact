import React from "react";
import ReactDOM from "react-dom/client";

import "./index.css";

const books = [
  {
    author: "西 加奈子",
    title:  "くもをさがす",
    img: "https://m.media-amazon.com/images/I/51EsrQ2SuzL.jpg",
    id: 1,
  },
  {
    author: "Yamauchi",
    title: "Ruby on Rails7",
    img:"https://m.media-amazon.com/images/P/B0BGMWMSLN.01._SCLZZZZZZZ_SX500_.jpg",
    id: 2,
  }
];

// eslint-disable-next-line no-unused-vars
const Book = (props) => {
  const {img, title, author} = props;
  return (
    <article className="book">
      <img
        src= {img}
        alt= {title}
      />
      <h2>{title}</h2>
      <h4>{author}</h4>
    </article>
  );
};

const EventExamples = () => {
  const handleFormInput = (e) => {
    console.log(e);
    console.log("handle form input");
  };

  const handleButtonClick = () => {
    alert("handle form input");
  };

  return (
    <section>
      <form>
        <h2>Typical Form</h2>
        <input type="text" name="example" onChange={handleFormInput} style={{ margin: "1rem 0"}}/>
      </form>
      <button onClick={handleButtonClick}>Click me</button>
    </section>
  );
};

const BookList = () => {
  return (
    <section className="booklist">
      <EventExamples/>
      {
        books.map((book) =>  {
          return <Book {...book} key={book.id}/>;
        })
      }
    </section>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<BookList/>);