install:
	@echo "Instalando Base de Datos"
	sudo docker compose up database -d
	@echo "Iniciando Servicio REST"
	sudo docker compose up backend -d

remove:
	@echo "Deteniendo servicios..."
	sudo docker compose down
	@echo "Todo fue destruido, mi estimado backyardigan."

start:
	@echo "Iniciando servicios..."
	sudo docker compose start database
	sudo docker compose start backend
	@echo "Servicios en marcha, tayron."

stop:
	@echo "Deteniendo servicios..."
	sudo docker compose stop
	@echo "Todo apagado, bob cachero."

help:
	@echo "----Hola mascota----"
	@echo -e "\e[38m-----------------------------------------------------------------------------------------------------"
	@echo -e "\e[38m1. Instalación del programa"
	@echo -e "\e[38mmake install"
	@echo -e "\e[38mMi estimado backyardigan, este comando instalará todo y lo levantará \e[38m(no te preocupes)"
	@echo -e "\e[38mBorrando System38..."
	@echo -e "\e[38m-----------------------------------------------------------------------------------------------------"
	@echo -e "\e[38m2. Desinstalación del programa"
	@echo -e "\e[38mmake remove"
	@echo -e "\e[38mMi estimado pablito, este comando desinstalará todo \e[38m(no te preocupes)"
	@echo -e "\e[38mArisaca destruyó a las hormigas..."
	@echo -e "\e[38m-----------------------------------------------------------------------------------------------------"
	@echo -e "\e[38m3. Start del programa"
	@echo -e "\e[38mmake start"
	@echo -e "\e[38mMi estimado tayron, este comando iniciará el proyecto si lo instalaste y detuviste"
	@echo -e "\e[38mPongámoslo a prueba :V"
	@echo -e "\e[38m-----------------------------------------------------------------------------------------------------"
	@echo -e "\e[38m4. Stop del programa"
	@echo -e "\e[38mmake stop"
	@echo -e "\e[38mMi estimado bob cachero, este comando detendrá el proyecto si lo instalaste y quieres detenerlo"
	@echo -e "\e[38m¡Apágalo Otto, apágalo! ¡Gokuuuuuuu!"
