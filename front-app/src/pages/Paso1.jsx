import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import TechoCanvas from '../components/TechoCanvas';
import Swal from 'sweetalert2';
import '../styles/step.css';

const Paso1 = () => {
  const [areaDisponible, setAreaDisponible] = useState(null);
  const navigate = useNavigate();

  const handleNext = () => {
    if (!areaDisponible || areaDisponible <= 0) {
      Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'warning',
        title: 'Por favor, dibuja un techo válido con espacio disponible.',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
      });
      return;
    }
    navigate('/paso2');
  };
  
  return (
    <div className="card">
      <div className="card-title">

          <div className="paso-card active">
            <div className="circle">1</div>
            <p>Paso 1: Área del Techo</p>
          </div>

          <div className="line"></div>

          <div className="paso-card">
            <div className="circle">2</div>
            <p>Paso 2: Consumo de Energía</p>
          </div>

      </div>

      <div className="card-question">
        <p>1. Dibuja tu techo y marca los obstáculos (como termas, etc). Solo se considerará el área libre.</p>

        <TechoCanvas onAreaDisponible={(area) => setAreaDisponible(area)} />
        
        <div className="buttons-card">
          <button className="back" onClick={() => navigate(-1)}>Atrás</button>
          <button className="next" onClick={handleNext}>Siguiente</button>
        </div>
      </div>
    </div>
  );
};

export default Paso1;
