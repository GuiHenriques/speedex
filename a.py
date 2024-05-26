# Dicionário de exemplo
dicionario = {2: False, 3: True, 5: False}

# Encontrando a chave onde o valor é True
numero = next(key for key, value in dicionario.items() if value)

# Exibindo o resultado
print(numero)
def validar_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

print([validar_numero(x) for x in ["10", "2.5", "a", "dez", "1,0", ".25", "0.25", "0,25"]])