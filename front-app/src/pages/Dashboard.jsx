// src/pages/Dashboard.jsx
import { useEffect, useState } from 'react';
import { getSolucionOptima } from '../services/solarApi';
import { FaSolarPanel, FaBatteryFull, FaExchangeAlt, FaChartLine, FaStickyNote, FaBolt, FaListOl, FaBatteryThreeQuarters, FaDollarSign, FaPiggyBank, FaClock, FaHome } from 'react-icons/fa';
import { AiOutlineWarning } from 'react-icons/ai';
import { FaEnvelopeCircleCheck } from "react-icons/fa6"; 
import { useNavigate } from 'react-router-dom';
import Swal from 'sweetalert2';
import '../styles/dashboard.css';

export default function Dashboard() {
  const [respuesta, setRespuesta] = useState(null);
  const [loading, setLoading] = useState(true);

  const area = localStorage.getItem('areaDisponible');
  const consumo = localStorage.getItem('consumoTotal');
  const navigate = useNavigate();

  const handleIrAlInicio = () => {
    navigate('/');
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = {
          area_disponible: Number(area),
          consumo_total: Number(consumo)
        };
        const res = await getSolucionOptima(data);
        setRespuesta(res.data);
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Ocurrió un error al obtener la solución óptima. Verifica los datos ingresados o intenta nuevamente.',
          confirmButtonColor: '#3085d6',
          confirmButtonText: 'Entendido'
        });
      } finally {
        setLoading(false);
      }
    };

    if (area && consumo) {
      fetchData();
    } else {
      console.warn('No hay datos en localStorage');
      setLoading(false);
    }
  }, [area, consumo]);

  if (loading) {
    return (
      <div className="content">
        <div className="loader"></div>
      </div>
    );
  }

  if (!respuesta) {
    return (
      <div className="content error-container">
        <AiOutlineWarning className="error-icon" />
        <h2 className="error-title">¡Ups! Ocurrió un error</h2>
        <p className="error-message">No se pudieron obtener los datos necesarios para mostrar la solución óptima.</p>
        <div className="error-button-wrapper">
          <button className="dash-home-button dash-error" onClick={handleIrAlInicio}>
            <FaHome className="dash-home-icon" />
            Volver al Inicio
          </button>
        </div>
      </div>
    );
  }

  const { configuracion, roi } = respuesta;

  return (
    <div className="content2">
      <div className="dash-info">
        
        <div className="dash-tittle">
          <h1>
            Calculadora 
            <span className="dash-first"> sol</span>
            <span className="dash-second">AR</span>
          </h1>
        </div>

        <div className="container-superior">
          <div className="dash-card">
            <div className="card-header"><FaSolarPanel /> Panel Solar</div>
            <div className="card-content">
              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaSolarPanel className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Modelo:</strong> {configuracion.panel_optimo.panel.modelo}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaBolt className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Potencia por panel:</strong> {configuracion.panel_optimo.panel.potencia} W</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaListOl className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Cantidad:</strong> {configuracion.panel_optimo.cantidad}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaBatteryThreeQuarters className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Energía total generada:</strong> {configuracion.panel_optimo.energia_total_kwh_dia.toFixed(2)} kWh/día</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaDollarSign className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Costo total:</strong> ${configuracion.panel_optimo.costo_total_usd}</p>
                </div>
              </div>
            </div>
          </div>

          <div className="dash-card">
            <div className="card-header"><FaBatteryFull /> Batería</div>
            <div className="card-content">
              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaBatteryFull className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Modelo:</strong> {configuracion.bateria_optima.bateria.modelo}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaDollarSign className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Capacidad:</strong> {configuracion.bateria_optima.bateria.capacidad_wh} Wh</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaListOl className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Cantidad:</strong> {configuracion.bateria_optima.cantidad}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaDollarSign className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Costo total:</strong> ${configuracion.bateria_optima.costo_total_usd}</p>
                </div>
              </div>
            </div>
          </div>

          <div className="dash-card">
            <div className="card-header"><FaExchangeAlt /> Inversor</div>
            <div className="card-content">
              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaExchangeAlt className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Modelo:</strong> {configuracion.inversor_optimo.modelo}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaBolt className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Potencia:</strong> {configuracion.inversor_optimo.potencia_unitaria} W</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaListOl className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Cantidad:</strong> {configuracion.inversor_optimo.cantidad}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaDollarSign className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Costo total:</strong> ${configuracion.inversor_optimo.costo_total}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="container-inferior">
          <div className="dash-card last-card">
            <div className="card-header"><FaChartLine /> ROI y Payback</div>
            <div className="card-content">
              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaPiggyBank className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text"><strong>Ahorro diario estimado:</strong> S/ {roi.analisis.retorno_inversion.ahorro_diario_soles}</p>
                </div>
              </div>

              <div className="panel-info-box">
                <div className="panel-info-icon-box">
                  <FaClock className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text">
                    <strong>Tiempo de recuperación:</strong> {roi.analisis.retorno_inversion.anios} años ({roi.analisis.retorno_inversion.dias} días)
                  </p>
                </div>
              </div>
            </div>            
          </div>

          {/* Notas */}
          <div className="dash-card card-notas">
            <div className="card-header"><FaStickyNote /> Notas</div>

            <div className="card-content notas-cont">
            {roi.notas.map((nota, index) => (
              <div className="panel-info-box" key={index}>
                <div className="panel-info-icon-box">
                  <FaEnvelopeCircleCheck className="panel-info-icon" />
                </div>
                <div className="panel-info-divider"></div>
                <div className="panel-info-text-box">
                  <p className="panel-info-text">{nota}</p>
                </div>
              </div>
            ))}
            </div>
          </div>

          <div className="dash-home">
            <button className="dash-home-button" onClick={handleIrAlInicio}>
              <FaHome className="dash-home-icon" />
              Inicio
            </button>
          </div>
        </div>
      </div> 
    </div>
  );
}
