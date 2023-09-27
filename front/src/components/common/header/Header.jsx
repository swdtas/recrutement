import React, { useState } from "react";
import "./header.css";
import { nav } from "../../data/Data";
import { Link } from "react-router-dom";

const Header = () => {
  const [navList, setNavList] = useState(false);

  return (
    <>
      <header>
        <div className="container flex">
          <div className="logo">
            <img src="./images/logo.png" alt="" />
          </div>
          <div className="nav">
            <ul className={navList ? "small" : "flex"}>
              {nav.map((item, index) => ( // Utilisez "item" au lieu de "list" ici
                <li key={index}>
                  {item.button ? ( // Vérifie si l'élément a un bouton
                    <button  className="button1"  onClick={() => window.location.href = item.path}>{item.button}</button>
                  ) : (
                    <Link to={item.path}>{item.text}</Link>
                  )}
                </li>
              ))}
            </ul>
          </div>
          <div className="toggle">
            <button onClick={() => setNavList(!navList)}>
              {navList ? (
                <i className="fa fa-times"></i>
              ) : (
                <i className="fa fa-bars"></i>
              )}
            </button>
          </div>
        </div>
      </header>
    </>
  );
};

export default Header;
