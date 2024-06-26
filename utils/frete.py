def calcula_valor_total(distancia, peso, dimensoes, taxa_caixa, taxa_entrega):
    taxa_distancia = 0.005
    taxa_peso = 0.2
    taxa_volume = 0.00005

    distancia = distancia / 1000  # convertendo m para km

    volume = dimensoes.altura * dimensoes.largura * dimensoes.comprimento
    valor_total = (
        (distancia * taxa_distancia) + (peso * taxa_peso) + (volume * taxa_volume)
    )

    valor_total *= 1 + (taxa_entrega/100)
    valor_total += taxa_caixa

    return round(valor_total, 2)
