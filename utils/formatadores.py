def cpf_formatador(cpf: str) -> str:
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    return cpf

def cep_formatador(cep: str) -> str:
    cep = cep.replace("-", "")
    return cep