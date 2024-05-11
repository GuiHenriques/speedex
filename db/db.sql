CREATE TABLE funcionarios(cpf VARCHAR(11) PRIMARY KEY, nome VARCHAR(255) NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, senha VARCHAR(255) NOT NULL);

CREATE TABLE tipos_de_entrega(id SERIAL PRIMARY KEY, nome VARCHAR(255) NOT NULL, taxa FLOAT NOT NULL, descricao TEXT);

CREATE TABLE clientes(cpf VARCHAR(11) PRIMARY KEY, nome VARCHAR(100),
cep VARCHAR(8), estado VARCHAR(100), cidade VARCHAR(100), bairro VARCHAR(100), rua VARCHAR(100), numero VARCHAR(10));

CREATE TABLE encomendas(id SERIAL PRIMARY KEY, conteudo TEXT, peso FLOAT, tipo_de_caixa_id INT, FOREIGN KEY(tipo_de_caixa_id) REFERENCES tipos_de_caixa(id));

CREATE TABLE entregas(id SERIAL PRIMARY KEY, remetente_cpf VARCHAR(11), destinatario_cpf VARCHAR(11), encomenda_id INT, tipo_de_entrega_id INT, funcionario_cpf INT, distancia FLOAT,
FOREIGN KEY(remetente_cpf) REFERENCES clientes(cpf), FOREIGN KEY(destinatario_cpf) REFERENCES clientes(cpf), FOREIGN KEY(encomenda_id) REFERENCES encomendas(id), FOREIGN KEY(tipo_de_entrega_id) REFERENCES tipos_de_entrega(id), FOREIGN KEY(funcionario_cpf) REFERENCES funcionarios(cpf));