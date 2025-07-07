# Usa una imagen oficial de Python
FROM python:3.13

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia el archivo de requerimientos e instala dependencias
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del backend al contenedor
COPY . .

# Copia el script de espera para la base de datos
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expón el puerto en el que correrá el servidor Django
EXPOSE 8000

# El comando de inicio lo manejará docker-compose
