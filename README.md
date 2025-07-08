# ☀️ solAR – Calculadora de Viabilidad Solar para Hogares en Arequipa

solAR es una aplicación web desarrollada para ayudar a los ciudadanos de **Arequipa, Perú**, a calcular el **retorno de inversión (ROI)** y el **dimensionamiento óptimo** de un sistema de paneles solares doméstico. Aprovecha el alto potencial de radiación solar de la región para ofrecer recomendaciones precisas, accesibles y sostenibles.

---

## 📌 Problema

En Arequipa y otras regiones urbanas del Perú, el aumento del consumo energético está presionando las redes eléctricas y elevando los costos. Aunque Arequipa cuenta con una de las **mayores radiaciones solares del país**, este potencial se encuentra subutilizado debido a:

- Falta de conocimiento técnico y económico sobre energía solar.
- Ausencia de herramientas accesibles para evaluar la viabilidad de paneles solares en hogares.

---

## 💡 Solución Propuesta

**solAR** nace como una herramienta que permite:

- Calcular el consumo eléctrico mensual estimado.
- Evaluar el área disponible en el techo para instalación de paneles.
- Sugerir un sistema óptimo de paneles, baterías e inversores.
- Estimar el **costo inicial**, **ahorros anuales**, **payback** y **ROI**.
- Promover el uso de energía limpia y sostenible.

Toda esta información se presenta en una interfaz amigable, orientada a usuarios no técnicos.

---

## 🌱 Justificación

El proyecto contribuye directamente a:

- **Reducir la dependencia de fuentes no renovables**.
- **Mitigar el impacto ambiental** del consumo urbano.
- **Aprovechar el potencial fotovoltaico** de Arequipa (>5.5 kWh/m² promedio diario).
- **Disminuir los costos eléctricos** para los hogares locales.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend**: React + Vite
- **Backend**: Django + Django REST Framework
- **Base de Datos**: MySQL 8
- **Contenedores**: Docker + Docker Compose

---

## 🚀 Despliegue Local

### 1. Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 2. Clonar el repositorio

```bash
git clone https://github.com/DOCK-8/TI-PROJECT.git
cd TI-PROJECT
```

### 3. Levantar el proyecto
```bash
docker-compose up --build
```

### 4. Acceder a la app

- **Frontend (React)**: http://localhost:5173/
- **Backend**: http://localhost:8000/api/v1
- **Base de Datos**: Puerto 3306 (MySQL)

---

## 📈 Resultados Esperados

- Recomendaciones personalizadas basadas en consumo real (datos de SEAL).
- Estimaciones de ahorro energético y económico.
- Mayor conciencia y adopción de tecnologías solares en hogares urbanos.

## 🤝 Contribuciones
¡Toda colaboración es bienvenida! Puedes abrir issues o pull requests para mejorar la herramienta.
