def validar_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

print([validar_numero(x) for x in ["10", "2.5", "a", "dez", "1,0", ".25", "0.25", "0,25"]])