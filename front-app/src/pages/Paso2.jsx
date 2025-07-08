import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { MdElectricBolt } from 'react-icons/md';
import ElectrodomesticoCard from '../components/ElectrodomesticoCard';
import { electrodomesticos } from '../data/electrodomesticos';
import Swal from 'sweetalert2';
import "../styles/card.css";

export default function Paso2() {
  const navigate = useNavigate();
  const [cantidades, setCantidades] = useState({});

  const handleCantidadChange = (nombre, nuevaCantidad) => {
    setCantidades(prev => ({
      ...prev,
      [nombre]: Math.max(0, nuevaCantidad),
    }));
  };

  const calcularConsumoTotal = () => {
    let total = 0;

    Object.values(electrodomesticos).forEach((grupo) => {
      grupo.forEach(({ nombre, potencia }) => {
        const cantidad = cantidades[nombre] || 0;
        total += cantidad * potencia;
      });
    });

    return total;
  };

  const handleNext = () => {
    const consumoTotal = calcularConsumoTotal();

    if (consumoTotal === 0) {
      Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'warning',
        title: 'Debes seleccionar al menos un equipo con consumo.',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
      });
      return;
    }

    console.log('Consumo total estimado (W):', consumoTotal);
    navigate('/paso3');
  };

  return (
    <div className="card">
      <div className="card-title">
        <div className="paso-card">
          <div className="circle">1</div>
          <p>Paso 1: Área del Techo</p>
        </div>

        <div className="line"></div>

        <div className="paso-card active">
          <div className="circle">2</div>
          <p>Paso 2: Consumo de Energía</p>
        </div>
      </div>

      <div className="card-question">
        <p>2. Selecciona cuántos equipos tienes de cada tipo para estimar tu consumo diario.</p>

        <div className="techo-container">
        {Object.entries(electrodomesticos).map(([seccion, items]) => (
          <div key={seccion} className='electro-container'>
            <h2 className='electro-tittle'>{seccion}</h2>
            <div className="cards-container">
              {items.map(({ nombre }) => (
                <ElectrodomesticoCard
                  key={nombre}
                  nombre={nombre}
                  cantidad={cantidades[nombre] || 0}
                  onChange={handleCantidadChange}
                />
              ))}
            </div>
          </div>
        ))}

          <div className="consumo-fijo">
            <h3>
              <MdElectricBolt style={{ color: '#00C853', marginRight: '0.5rem', verticalAlign: 'middle' }} />
              Consumo total estimado: <strong>{calcularConsumoTotal()} W</strong>
            </h3>
          </div>
        </div>

        <div className="buttons-card">
          <button className="back" onClick={() => navigate(-1)}>Atrás</button>
          <button className="next" onClick={handleNext}>Siguiente</button>
        </div>
      </div>
    </div>
  );
}
