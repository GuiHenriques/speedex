-- Insert into funcionarios
INSERT INTO funcionarios (cpf, nome, email, senha) VALUES
('12345678909', 'Joao Silva', 'joao.silva@example.com', 'senha123'),
('98765432100', 'Maria Oliveira', 'maria.oliveira@example.com', 'senha456');

-- Insert into tipos_de_entrega
INSERT INTO tipos_de_entrega (nome, taxa, descricao, velocidade) VALUES
('Entrega Rapida', 15.0, 'Entrega em até 24 horas', 24),
('Entrega Economica', 5.0, 'Entrega em até 7 dias úteis', 168);

-- Insert into clientes
INSERT INTO clientes (cpf, nome, cep, estado, cidade, bairro, rua, numero) VALUES
('12345678909', 'Carlos Pereira', '01001000', 'SP', 'Sao Paulo', 'Centro', 'Rua A', '123'),
('98765432100', 'Ana Costa', '20040030', 'RJ', 'Rio de Janeiro', 'Copacabana', 'Avenida B', '456');

-- Insert into tipo_de_caixa
INSERT INTO tipo_de_caixa (nome, taxa, altura, largura, comprimento) VALUES
('Caixa Pequena', 10.0, 30.0, 20.0, 10.0),
('Caixa Grande', 20.0, 60.0, 40.0, 30.0);

-- Insert into encomendas
INSERT INTO encomendas (conteudo, peso, tipo_de_caixa_id, tipo_de_caixa_nome, tipo_de_caixa_taxa, tipo_de_caixa_altura, tipo_de_caixa_largura, tipo_de_caixa_comprimento) VALUES
('Livros', 2, 1, 'Caixa Pequena', 10.0, 30.0, 20.0, 10.0),
('Roupas', 5, 2, 'Caixa Grande', 20.0, 60.0, 40.0, 30.0);

-- Insert into entregas
INSERT INTO entregas (remetente_cpf, remetente_nome, destinatario_cpf, destinatario_nome, funcionario_cpf, funcionario_nome, encomenda_id, tipo_de_entrega_id, tipo_de_entrega_nome, tipo_de_entrega_taxa, distancia, valor, created_at) VALUES
('12345678909', 'Joao Silva', '98765432100', 'Maria Oliveira', '12345678909', 'Joao Silva', 1, 1, 'Entrega Rapida', '15.0', 100.0, 10000, CURRENT_TIMESTAMP),
('98765432100', 'Maria Oliveira', '12345678909', 'Joao Silva', '98765432100', 'Maria Oliveira', 2, 2, 'Entrega Economica', '5.0', 500.0, 200000, CURRENT_TIMESTAMP);
