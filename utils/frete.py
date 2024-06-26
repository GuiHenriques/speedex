def calcula_valor_total(distancia, peso, dimensoes, taxa_caixa, taxa_entrega):
    taxa_distancia = 0.005
    taxa_peso = 0.2
    taxa_volume = 0.00005

    distancia = distancia / 1000  # convertendo m para km
    print("Distancia: ", distancia)

    volume = dimensoes.altura * dimensoes.largura * dimensoes.comprimento
    print("Volume: ", volume)
    valor_total = (
        (distancia * taxa_distancia) + (peso * taxa_peso) + (volume * taxa_volume)
    )
    print("Valor total: ", valor_total)

    valor_total *= 1 + (taxa_entrega/100)
    print("Valor total com taxa de entrega: ", valor_total)
    valor_total += taxa_caixa
    print("Valor total com taxa de entrega e de caixa: ", valor_total)

    return round(valor_total, 2)
