# Dicionário de exemplo
dicionario = {2: False, 3: True, 5: False}

# Encontrando a chave onde o valor é True
numero = next(key for key, value in dicionario.items() if value)

# Exibindo o resultado
print(numero)
