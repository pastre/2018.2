DROP database db;
CREATE DATABASE db;
USE db;

CREATE TABLE Cliente(nome TEXT,
 cpf INT,
 PRIMARY KEY(cpf));
 
CREATE TABLE Animal(especie TEXT,
 sexo VARCHAR(1), dataNascimento TEXT,
 codigoAnimal INT auto_increment,
 nome TEXT,
 raca TEXT,
 cpf INT,
 FOREIGN KEY (cpf) REFERENCES Cliente(cpf),
 primary key (codigoAnimal));

CREATE TABLE Consulta(codigoConsulta INT auto_increment,
dataAtendimento DATE,
preco float,
crmv TEXT,
descricao TEXT,
codigoAnimal INT,
FOREIGN KEY (codigoAnimal) REFERENCES Animal(codigoAnimal),
primary key(codigoConsulta)
);

CREATE TABLE Vacina(codigoVacina INT auto_increment,
dataAplicacao DATE,
preco FLOAT,
doenca TEXT,
lote INT,
codigoAnimal INT,
FOREIGN KEY (codigoAnimal) REFERENCES Animal(codigoAnimal),
primary key(codigoVacina)
);

CREATE TABLE Loja(ticket INT,
dataCompra DATE,
descricao TEXT,
quantidade integer,
preco FLOAT,
cpf INT,
FOREIGN KEY (cpf) REFERENCES Cliente(cpf),
primary key(ticket)
);



