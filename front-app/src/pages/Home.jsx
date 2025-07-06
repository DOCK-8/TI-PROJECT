// src/pages/Home.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/paso1');
  };

  return (
    <div className="content">
      <h1>
        Bienvenido a <span className="logo-first">sol</span>
        <span className="logo-second">AR</span>
      </h1>
      <p>
        Una herramienta inteligente para calcular cuántos paneles solares necesita tu hogar, basada en tu consumo eléctrico y el potencial solar de Arequipa.
      </p>
      <button className="btn" onClick={handleClick}>Probar ahora</button>
    </div>
  );
};

export default Home;
