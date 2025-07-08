import React from 'react';
import { Minus, Plus, PlugZap } from 'lucide-react';
import { iconMap } from '../data/iconMap';

const ElectrodomesticoCard = ({ nombre, cantidad, onChange }) => {
  const iconSrc = iconMap[nombre];

  return (
    <div className="electro-card">
      <div className="icon">
        {iconSrc ? (
          <img src={iconSrc} alt={nombre} className="img-icono" />
        ) : (
          <PlugZap size={32} />
        )}
      </div>
      <div className="info">
        <h4>{nombre}</h4>
        <div className="controls">
          <button onClick={() => onChange(nombre, cantidad - 1)}>-</button>
          <span>{cantidad}</span>
          <button onClick={() => onChange(nombre, cantidad + 1)}>+</button>
        </div>
      </div>
    </div>
  );
};

export default ElectrodomesticoCard;
