SELECT 
    en.id AS "ID",
    remetente.cpf AS "CPF Remetente",
    remetente.nome AS "Remetente",
    destinatario.cpf AS "CPF Destinatario",
    destinatario.nome AS "Destinatario",
    f.cpf AS "CPF Funcionario",
    f.nome AS "Funcionario",
    tc.altura AS "Altura",
    tc.largura AS "Largura",
    tc.comprimento AS "Comprimento",
    tc.nome AS "Caixa",
    e.conteudo AS "Conteudo",
    tc.taxa AS "Taxa da Caixa",
    tde.nome AS "Tipo de Entrega",
    tde.taxa AS "Taxa de Entrega",
    remetente.cep AS "CEP",
    en.created_at AS "Data",
    en.distancia AS "Distancia",
    (tc.taxa + tde.taxa) AS "Valor Total"
FROM entregas en
LEFT JOIN clientes remetente ON en.remetente_cpf = remetente.cpf
LEFT JOIN clientes destinatario ON en.destinatario_cpf = destinatario.cpf
LEFT JOIN funcionarios f ON en.funcionario_cpf = f.cpf
LEFT JOIN encomendas e ON en.encomenda_id = e.id
LEFT JOIN tipo_de_caixa tc ON e.tipo_de_caixa_id = tc.id
LEFT JOIN tipos_de_entrega tde ON en.tipo_de_entrega_id = tde.id;
