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
const Book = ({img, title, author}) => {
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

const BookList = () => {
  return (
    <section className="booklist">
      {
        books.map((book) => {
          const { img, title, author, id} = book;
          // eslint-disable-next-line react/jsx-key
          return (
            <Book
              img={img}
              title={title}
              author={author}
              key={id}
            />
          );
        }
        )
      }
    </section>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<BookList/>);