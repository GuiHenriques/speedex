def cpf_formatador(cpf: str) -> str:
  cpf = cpf.replace(".", "")
  cpf = cpf.replace("-", "")
  return cpf