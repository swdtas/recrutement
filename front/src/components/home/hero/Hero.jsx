import React, { useState, useEffect } from "react";
import "./hero.css";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { sliderImages } from "../../data/Data";
import { CSSTransition } from "react-transition-group";

const Hero = () => {
  const [isTitleVisible, setTitleVisible] = useState(false);

  useEffect(() => {
    // Utilisez setTimeout pour retarder l'affichage du titre
    const timer = setTimeout(() => {
      setTitleVisible(true);
    }, 5000); // Délai d'une seconde (1000 millisecondes)

    return () => {
      clearTimeout(timer); // Assurez-vous de nettoyer le timer si le composant est démonté avant l'expiration du délai
    };
  }, []);

  return (
    <>
      <section className='hero'>
        <Carousel showArrows={false} showStatus={false} showThumbs={false} autoPlay={true} interval={2000} infiniteLoop={true}>
          {sliderImages.map((item, index) => (
            <div key={index} className="slide-container">
              <img
                src={item.image}
                alt={`Slide ${index + 1}`}
                className="slide-image"
              />
              <div className="slide-content">
                {isTitleVisible && ( // Condition pour afficher le titre après le délai
                  <p className="slide-title">{item.title}</p>
                )}
                <CSSTransition
                  in={true}
                  timeout={5000}
                  className="slide-description"
                >
                  <p className="slide-description">
                    <i className="fas fa-quote-left"></i> {item.description}{" "}
                    <i className="fas fa-quote-right"></i>
                  </p>
                </CSSTransition>
              </div>
            </div>
          ))}
        </Carousel>
        <form className='flex'>
          <div className='box'> 
            <input type='text' placeholder='Mots clés' />
          </div>
          <div className='box'>
            <input type='text' placeholder='Region' />
          </div>
          <button className='btn1'>
            <i className='fa fa-search'></i>
          </button>
        </form>
      </section>
    </>
  );
};

export default Hero;
