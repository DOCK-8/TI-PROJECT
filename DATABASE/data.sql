-- Crear base de datos y usarla
CREATE DATABASE IF NOT EXISTS systemPV;
USE systemPV;

-- Tabla de irradiacion
CREATE TABLE irradiacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    month VARCHAR(10) NOT NULL,
    value DECIMAL(5,2) NOT NULL
);

-- Tabla de paneles solares
CREATE TABLE paneles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255),
    precio DECIMAL(10,2),
    potencia INT,
    consumo_mensual DECIMAL(10,2),
    tiempo_vida INT,
    eficiencia DECIMAL(5,2),
    ancho INT,
    alto INT
);

-- Tabla de inversores
CREATE TABLE inversores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255),
    precio DECIMAL(10,2),
    potencia INT,
    tension_admisible INT,
    consumo_mensual DECIMAL(10,2),
    tiempo_vida INT,
    eficiencia DECIMAL(5,2),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL
);

-- Tabla de baterías
CREATE TABLE baterias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255),
    precio DECIMAL(10,2),
    largo INT,
    ancho INT,
    alto INT,
    voltaje INT,
    eficiencia DECIMAL(5,2),
    capacidad INT,
    tipo VARCHAR(20),
    consumo_mensual DECIMAL(10,2)
);

--LENADO DE LA BASE DE DATOS
-- Insertar baterías
INSERT INTO baterias (modelo, precio, largo, ancho, alto, voltaje, eficiencia, capacidad, tipo, consumo_mensual) VALUES
('Bateria AGM 12v 65Ah CSBattery', 396.00, 350, 167, 178, 12, 92, 65, 'AGM', 792),
('Bateria AGM 12v 100Ah CSBattery', 656.95, 350, 175, 190, 12, 91, 100, 'AGM', 742),
('Bateria AGM 12v 150Ah CSBattery', 814.41, 360, 180, 200, 12, 91, 150, 'AGM', 810),
('Bateria Narada 12v 100Ah AGM', 751.17, 395, 108, 287, 12, 94, 100, 'AGM', 1217.76),
('Bateria Narada 12v 150Ah AGM', 1585.92, 550, 125, 283, 12, 93, 150, 'AGM', 1585.92),
('Bateria AGM 12v 100Ah Kaise', 814.45, 330, 171, 215, 12, 97, 100, 'AGM', 868.28),
('BATERIA KAISE AGM 12V 65A', 616.80, 348, 167, 178, 12, 98, 65, 'AGM', 616.80),
('Bateria Solar AGM 12v 100Ah Aokly', 714.29, 331, 173, 213, 12, 91, 100, 'AGM', 857.21),
('Bateria Kaise AGM 150Ah Libre Mantenimiento', 1305.60, 483, 170, 239, 12, 96, 150, 'AGM', 1305.61),
('BATERIA SOLAR AOKLY 12V 200AH AGM LIBRE MANTENIMIENTO', 1066.00, 522, 240, 218, 12, 91, 200, 'AGM', 1388.05),
('Bateria Kaise AGM 200Ah Libre Mantenimiento', 1837.40, 546, 125, 310, 12, 96, 200, 'AGM', 1837.40),
('Bateria Solar AGM 12v 65Ah Aokly', 425.00, 340, 170, 180, 12, 95, 65, 'AGM', 648.05),
('BATERIA SOLAR GEL 12V 100AH AOKLY', 550.00, 329, 172, 214, 12, 91, 100, 'GEL', 1097.20),
('Bateria GEL 12v 100Ah Kaise', 673.66, 330, 171, 216, 12, 96, 100, 'GEL', 744.05),
('BATERIA CSBattery 600A 6V', 1288.71, 300, 200, 250, 6, 95, 600, 'GEL', 0),
('BATERIA SOLAR 200Ah 12v GEL CSBATTERY', 1197.00, 532, 206, 219, 12, 95, 200, 'GEL', 1047.00),
('BATERIA DE GEL CSBattery 100Ah 12V', 583.00, 307, 169, 211, 12, 96, 100, 'GEL', 525.00),
('BATERIA MARCA CSBATTERY LITIO 12V 100AH', 2595.51, 522, 240, 224, 12, 95, 100, 'LITIO', 1500.00);

-- Insertar inversores
INSERT INTO inversores (modelo, precio, potencia, tension_admisible, consumo_mensual, tiempo_vida, eficiencia, usuario_id) VALUES
('Inversor Victron Phoenix 24V 375VA VE.Direct', 260.11, 700, 24, 458.06, 25, 90, 1),
('Inversor Victron Phoenix 24V 500VA VE.Direct', 698.05, 900, 24, 570.66, 25, 91, 1),
('Inversor Victron Phoenix 24V 250VA VE.Direct', 389.77, 400, 24, 486.76, 25, 88, 1),
('Inversor Victron Phoenix 24V 800VA VE.Direct', 1022.79, 1500, 24, 1038.78, 25, 91, 2),
('Inversor Victron Phoenix 24V 1200VA VE.Direct', 1375.63, 2200, 24, 1397.18, 25, 92, 2),
('Inversor Victron Phoenix 48V 1200VA 120V VE.Direct 5-15R', 1373.91, 2200, 48, 1363.17, 25, 91, 3),
('Inversor Victron Phoenix 48V 375VA VE.Direct', 475.39, 700, 48, 521.04, 25, 90, 3),
('Inversor Victron Phoenix 48V 800VA VE.Direct', 1159.86, 1500, 48, 1114.62, 25, 91, 2),
('Inversor Victron Phoenix 48V 1200VA VE.Direct', 1373.91, 2200, 48, 1600.12, 25, 92, 1),
('Inversor Victron Phoenix 48V 250VA VE.Direct', 365.42, 400, 48, 644.46, 25, 88, 2),
('Inversor Victron Phoenix 12V 375VA 120V VE.Direct 5-15R', 1912.54, 650, 12, 471.54, 25, 89, 3),
('Inversor Victron Phoenix 12V 500VA 120V VE.Direct 5-15R', 2394.69, 1000, 12, 592.99, 25, 90, 1),
('Inversor Victron Phoenix 12V 375VA VE.Direct', 475.39, 700, 12, 455.33, 25, 89, 2),
('Inversor Victron Phoenix 12V 250VA VE.Direct', 365.42, 400, 12, 494.74, 25, 87, 3),
('Inversor cargador 300W 12V 10A Must Solar', 450.45, 300, 12, 506.40, 25, 80, 1),
('Inversor Victron Phoenix 12V 800VA VE.Direct', 1159.86, 1500, 12, 973.85, 25, 90, 2);

-- Insertar paneles solares
INSERT INTO paneles (modelo, precio, potencia, consumo_mensual, tiempo_vida, eficiencia, ancho, alto) VALUES
('Panel solar 100w 12v policristalino Sunlake', 296.61, 100, 700, 25, 21.30, 670, 1130),
('Panel Solar 100w 12v Monocristalino Sunlake', 354.58, 100, 700, 25, 21.30, 700, 1150),
('Panel solar 150w 12v policristalino Sunlake', 475.00, 150, 900, 25, 17.52, 680, 1480),
('Panel solar 150w 12v monocristalino Sunlake', 475.00, 150, 950, 25, 17.50, 680, 1480),
('Panel Solar 340w 24v Policristalino Eco Green', 349.00, 340, 871.5, 25, 21.00, 992, 1956),
('Panel Solar 450w 24v Monocristalino PERC Eco Green', 3155.62, 450, 1410, 25, 21.00, 1040, 2102),
('Panel Solar 460Wp 24v Amerisolar Monocristalino Perc Half Cell', 590.00, 460, 1180, 25, 21.27, 1040, 2102),
('Panel Solar 550w 24v Monocristalino PERC Eco Green', 4084.75, 550, 1350, 25, 21.28, 1040, 2102),
('Panel Solar policristalino 100wp Renjiang', 300.72, 100, 369.64, 25, 16.60, 670, 1000),
('Panel Solar 100W Amerisolar Policristalino', 625.56, 100, 456, 25, 17.79, 670, 1010),
('Panel Solar 340W Amerisolar Policristalino', 1160.00, 340, 1160, 25, 17.52, 992, 1956),
('Panel Solar 370Wp Amerisolar Monocristalino PERC', 1272.00, 370, 1272, 25, 19.33, 992, 1956),
('Panel Solar 160W Amerisolar Policristalino', 625.56, 160, 625.56, 25, 17.65, 670, 1480),
('Panel Solar 285W Amerisolar Policristalino', 530.44, 285, 846.72, 25, 17.52, 992, 1640),
('Panel Solar 370W Peimar Monocristalino PERC Peimar Italian', 1142.89, 370, 1142.89, 25, 19.06, 992, 1957),
('Panel Solar 150W Peimar Italian Policristalino', 485.72, 150, 485.73, 25, 15.04, 674, 1480),
('Panel Solar 285wp Policristalino Peimar Italian', 620.00, 285, 885.72, 25, 17.52, 992, 1640),
('Panel Solar Jinko Solar 400Wp HC Monocristalino PERC', 871.36, 400, 1244.80, 25, 19.88, 1002, 2008),
('Panel Solar 400W Peimar Monocristalino PERC Peimar Italian', 860.00, 400, 1196, 25, 20.17, 1002, 1979),
('Panel Solar 450W Peimar Monocristalino Half Cell PERC Peimar Italian', 990.00, 450, 1465.72, 25, 20.30, 1048, 2115),
('Panel Solar 315wp Monocristalino PERC Peimar Italian', 687.99, 315, 982.84, 25, 19.36, 992, 1640),
('Panel Solar 340wp Policristalino Peimar Italian', 1040.00, 340, 1040, 25, 17.51, 992, 1956),
('Panel Solar Jinko Solar 335Wp Policristalino', 485.72, 335, 1045.73, 25, 17.26, 992, 1956),
('Panel Solar 270wp Policristalino AE Solar PowerPlus', 732.92, 270, 732.92, 25, 16.50, 992, 1650),
('Panel Solar 450W TrinaSolar Monocristalino Half Cell PERC TALLMAX', 576.13, 450, 1465.72, 25, 20.60, 1040, 2102),
('TRINA SOLAR PANEL 24V 400W MONOPERC HALF CELL', 432.02, 400, 1220.02, 25, 19.50, 1096, 1754),
('PANEL SOLAR 460W 24V AE SOLAR MONOCRISTALINO PERC', 500.32, 460, 1046, 25, 21.16, 1133, 1902);

-- Carga de irradiacion
INSERT INTO irradiacion (year, month, value) VALUES
(2023, 'Enero',    6.80),
(2023, 'Febrero',  5.93),
(2023, 'Marzo',    5.54),
(2023, 'Abril',    6.64),
(2023, 'Mayo',     5.52),
(2023, 'Junio',    5.75),
(2023, 'Julio',    5.85),
(2023, 'Agosto',   6.65),
(2023, 'Septiembre', 7.49),
(2023, 'Octubre',  7.54),
(2023, 'Noviembre', 8.04),
(2023, 'Diciembre', 7.48);
