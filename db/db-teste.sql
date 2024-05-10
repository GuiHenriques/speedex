CREATE TABLE funcionarios(
  cpf VARCHAR(255),
  nome VARCHAR(255),
  email VARCHAR(255),
  senha VARCHAR(255)
);

CREATE TABLE tipos_de_entrega(
  nome VARCHAR(255),
  taxa FLOAT,
  descricao TEXT
);

CREATE TABLE clientes(
  cpf VARCHAR(255),
  nome VARCHAR(100),
  cep VARCHAR(8),
  estado VARCHAR(100),
  cidade VARCHAR(100),
  bairro VARCHAR(100),
  rua VARCHAR(100),
  numero VARCHAR(10)
);

CREATE TABLE tipo_de_caixa(
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255),
  taxa FLOAT,
  altura FLOAT,
  largura FLOAT,
  comprimento FLOAT
);