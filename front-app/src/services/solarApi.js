// src/api/solarApi.js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

export const getSolucionOptima = (data) => {
  console.log('Datos enviados a la API:', data);
  return API.post('/solucion-optima', data);
};

export const getToken = (credentials) => API.post('/token', credentials);

export default API;