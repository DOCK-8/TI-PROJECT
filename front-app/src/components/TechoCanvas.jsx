import React, { useRef, useState, useEffect } from 'react';
import { AiOutlineWarning } from 'react-icons/ai';
import Swal from 'sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import '../styles/techo.css';

const TechoCanvas = ({ onAreaDisponible }) => {
  const canvasRef = useRef(null);
  const [obstaculos, setObstaculos] = useState([]);
  const [dibujando, setDibujando] = useState(false);
  const [inicio, setInicio] = useState(null);
  const [actual, setActual] = useState(null);

  const [anchoMetros, setAnchoMetros] = useState('');
  const [altoMetros, setAltoMetros] = useState('');
  const [configurado, setConfigurado] = useState(false);

  const escala = 15;
  const anchoPx = anchoMetros * escala;
  const altoPx = altoMetros * escala;
  const techoArea = anchoMetros * altoMetros;

  const calcularAreaObstaculos = () => {
    const ocupados = new Set();

    obstaculos.forEach(({ x, y, w, h }) => {
      const startX = Math.floor(x);
      const endX = Math.ceil(x + w);
      const startY = Math.floor(y);
      const endY = Math.ceil(y + h);

      for (let i = startX; i < endX; i++) {
        for (let j = startY; j < endY; j++) {
          ocupados.add(`${i},${j}`);
        }
      }
    });

    const totalPixeles = ocupados.size;
    return totalPixeles / (escala * escala);
  };

  const dibujarTodo = () => {
    const ctx = canvasRef.current.getContext('2d');
    ctx.clearRect(0, 0, anchoPx, altoPx);

    ctx.fillStyle = '#E0F2F1';
    ctx.fillRect(0, 0, anchoPx, altoPx);

    ctx.fillStyle = '#EF5350';
    obstaculos.forEach(({ x, y, w, h }) => {
      ctx.fillRect(x, y, w, h);
    });

    if (dibujando && inicio && actual) {
      const x = Math.min(inicio.x, actual.x);
      const y = Math.min(inicio.y, actual.y);
      const w = Math.abs(actual.x - inicio.x);
      const h = Math.abs(actual.y - inicio.y);

      ctx.strokeStyle = '#00BFFF';
      ctx.setLineDash([6]);
      ctx.strokeRect(x, y, w, h);
      ctx.setLineDash([]);
    }

    const areaUtil = techoArea - calcularAreaObstaculos();
    onAreaDisponible(areaUtil);
  };

  useEffect(() => {
    if (configurado) dibujarTodo();
  }, [obstaculos, actual, configurado]);

  const handleMouseDown = (e) => {
    setDibujando(true);
    const rect = canvasRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    setInicio({ x, y });
    setActual({ x, y });
  };

  const handleMouseMove = (e) => {
    if (!dibujando) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    setActual({ x, y });
  };

  const handleMouseUp = () => {
    if (!dibujando || !inicio || !actual) return;

    const nuevo = {
      x: Math.min(inicio.x, actual.x),
      y: Math.min(inicio.y, actual.y),
      w: Math.abs(actual.x - inicio.x),
      h: Math.abs(actual.y - inicio.y),
    };

    if (nuevo.w > 5 && nuevo.h > 5) {
      setObstaculos([...obstaculos, nuevo]);
    }

    setDibujando(false);
    setInicio(null);
    setActual(null);
  };

  const anchoActual = actual && inicio ? Math.abs(actual.x - inicio.x) / escala : 0;
  const altoActual = actual && inicio ? Math.abs(actual.y - inicio.y) / escala : 0;
  const areaUtil = techoArea - calcularAreaObstaculos();
  const porcentaje = ((areaUtil / techoArea) * 100).toFixed(1);

  return (
    <div className="techo-container">
      <div className="canvas-area">
        {!configurado && (
          <div className="alerta-configuracion">
            <AiOutlineWarning size={24} color="#ff9800" />
            <span>Ingrese el ancho y alto del techo para comenzar</span>
          </div>
        )}
        {configurado && (
          <>
            <div className="canvas-wrapper">
              <canvas
                ref={canvasRef}
                width={anchoPx}
                height={altoPx}
                className="techo-canvas"
                onMouseDown={handleMouseDown}
                onMouseMove={handleMouseMove}
                onMouseUp={handleMouseUp}
              />
            </div>
            {dibujando && (
              <div className="medidas">
                Dibujando: {anchoActual.toFixed(2)} m × {altoActual.toFixed(2)} m
              </div>
            )}
            <div className="area-disponible">
              Área disponible: {areaUtil.toFixed(2)} m² ({porcentaje}% del total)
            </div>
            <button className="btn-rojo" onClick={() => setObstaculos([])}>
              Limpiar Obstáculos
            </button>
          </>
        )}
      </div>

      <div className="input-area">
        <h3>Dimensiones del techo</h3>
        {!configurado ? (
          <>
            <input
              type="number"
              placeholder="Ancho (m)"
              value={anchoMetros}
              onChange={(e) => setAnchoMetros(Number(e.target.value))}
              className="techo-input"
            />
            <input
              type="number"
              placeholder="Alto (m)"
              value={altoMetros}
              onChange={(e) => setAltoMetros(Number(e.target.value))}
              className="techo-input"
            />
            <button
              className="btn-verde"
              onClick={() => {
                const areaIngresada = Number(anchoMetros) * Number(altoMetros);
                if (anchoMetros > 0 && altoMetros > 0 && areaIngresada <= 200) {
                  setConfigurado(true);
                } else {
                  Swal.fire({
                    toast: true,
                    position: 'top-end',
                    icon: 'warning',
                    title: 'Dimensiones inválidas. El área máxima es 200 m².',
                    showConfirmButton: false,
                    timer: 3000,
                    timerProgressBar: true,
                  });
                }
              }}
            >
              Confirmar
            </button>
          </>
        ) : (
          <>
            <div className="input-text">
              Dimensiones: {anchoMetros} m × {altoMetros} m
            </div>
            <div className="input-text">
              Área total: {techoArea} m²
            </div>
            <button
              className="btn-rojo total"
              onClick={() => {
                setAnchoMetros('');
                setAltoMetros('');
                setConfigurado(false);
                setObstaculos([]);
                setActual(null);
                setInicio(null);
                setDibujando(false);
                setPasoActual(1); 
                const ctx = canvasRef.current?.getContext('2d');
                if (ctx && canvasRef.current) {
                  ctx.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
                }
              }}
            >
              Reiniciar todo
            </button>
          </>
        )}
      </div>
    </div>
  );
};

export default TechoCanvas;
