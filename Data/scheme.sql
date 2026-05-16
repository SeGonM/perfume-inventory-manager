DROP DATABASE IF EXISTS perfumeria;
CREATE DATABASE perfumeria;
USE perfumeria;

-- Tablas independientes
CREATE TABLE ciudad (
    id_ciudad INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE genero (
    id_genero INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE tipo_movimiento (
    id_tipo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE razon_movimiento (
    id_razon INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(150) NOT NULL
);

CREATE TABLE marca (
    id_marca INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE familia (
    codigo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

--  TABLAS PRINCIPALES

CREATE TABLE proveedor (
    NIT INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    id_ciudad INT NOT NULL,
    FOREIGN KEY (id_ciudad) REFERENCES ciudad (id_ciudad)
);

CREATE TABLE categoria (
    codigo VARCHAR(20)  NOT NULL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_genero INT NOT NULL,
    FOREIGN KEY (id_genero) REFERENCES genero (id_genero)
);

CREATE TABLE perfume (
    codigo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    stock  INT NOT NULL DEFAULT 0,
    id_marca INT NOT NULL,
    codigo_familia INT NOT NULL,
    FOREIGN KEY (id_marca) REFERENCES marca (id_marca),
    FOREIGN KEY (codigo_familia) REFERENCES familia (codigo)
);

CREATE TABLE localizacion (
    id_localizacion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pasillo VARCHAR(20) NOT NULL,
    estante VARCHAR(20) NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    codigo_perfume INT NOT NULL UNIQUE,
    FOREIGN KEY (codigo_perfume) REFERENCES perfume (codigo)
);

CREATE TABLE movimiento (
    id_movimiento INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_tipo INT NOT NULL,
    id_razon INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_tipo)  REFERENCES tipo_movimiento (id_tipo),
    FOREIGN KEY (id_razon) REFERENCES razon_movimiento (id_razon)
);

--  TABLAS INTERMEDIAS (N:M)

CREATE TABLE proveedor_perfume (
    NIT INT NOT NULL,
    codigo_perfume INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (NIT, codigo_perfume),
    FOREIGN KEY (NIT) REFERENCES proveedor (NIT),
    FOREIGN KEY (codigo_perfume) REFERENCES perfume (codigo)
);

CREATE TABLE perfume_categoria (
    codigo_perfume INT NOT NULL,
    codigo_categoria VARCHAR(20) NOT NULL,
    PRIMARY KEY (codigo_perfume, codigo_categoria),
    FOREIGN KEY (codigo_perfume)   REFERENCES perfume (codigo),
    FOREIGN KEY (codigo_categoria) REFERENCES categoria (codigo)
);

CREATE TABLE perfume_movimiento (
    codigo_perfume INT NOT NULL,
    id_movimiento INT NOT NULL,
    PRIMARY KEY (codigo_perfume, id_movimiento),
    FOREIGN KEY (codigo_perfume) REFERENCES perfume (codigo),
    FOREIGN KEY (id_movimiento)  REFERENCES movimiento (id_movimiento)
);
