CREATE TABLE funcionarios(
  cpf VARCHAR(11) PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  senha VARCHAR(255) NOT NULL
);

CREATE TABLE tipos_de_entrega(
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  taxa FLOAT NOT NULL,
  descricao TEXT,
  velocidade INT NOT NULL
);

CREATE TABLE clientes(
  cpf VARCHAR(11) PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cep VARCHAR(8),
  estado VARCHAR(100),
  cidade VARCHAR(100),
  bairro VARCHAR(100),
  rua VARCHAR(100),
  numero VARCHAR(10)
);

CREATE TABLE tipo_de_caixa(
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  taxa FLOAT NOT NULL,
  altura FLOAT NOT NULL,
  largura FLOAT NOT NULL,
  comprimento FLOAT NOT NULL
);

CREATE TABLE encomendas (
  id SERIAL PRIMARY KEY,
  conteudo TEXT NOT NULL,
  peso INT NOT NULL,
  tipo_de_caixa_id INTEGER REFERENCES tipo_de_caixa(id),
  tipo_de_caixa_nome VARCHAR(255) NOT NULL,
  tipo_de_caixa_taxa FLOAT,
  tipo_de_caixa_altura FLOAT NOT NULL,
  tipo_de_caixa_largura FLOAT NOT NULL,
  tipo_de_caixa_comprimento FLOAT NOT NULL
);

CREATE TABLE entregas (
  id SERIAL PRIMARY KEY,
  remetente_cpf VARCHAR(11) REFERENCES clientes(cpf),
  remetente_nome VARCHAR(255) NOT NULL,
  destinatario_cpf VARCHAR(11) REFERENCES clientes(cpf),
  destinatario_nome VARCHAR(255) NOT NULL,
  funcionario_cpf VARCHAR(11) REFERENCES funcionarios(cpf),
  funcionario_nome VARCHAR(255) NOT NULL,
  encomenda_id INTEGER REFERENCES encomendas(id),
  tipo_de_entrega_id INTEGER REFERENCES tipos_de_entrega(id),
  tipo_de_entrega_nome VARCHAR(255) NOT NULL,
  tipo_de_entrega_taxa VARCHAR(255) NOT NULL,
  distancia FLOAT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
