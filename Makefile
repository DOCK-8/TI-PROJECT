install:
	echo "Instalando Base de Datos"
	sudo docker compose up database -d
	echo "Iniciando Servicio REST"
	sudo docker compose up backend -d
