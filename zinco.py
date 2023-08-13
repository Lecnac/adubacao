def calcular_dose_zinco(zinco_solo):
    if zinco_solo < 2.5:
        dose_zinco = 4.0
    elif 2.5 <= zinco_solo <= 5.0:
        dose_zinco = 2.0
    else:
        dose_zinco = 1.0
    return dose_zinco

def calcular_recomendacao_oxido_zinco(dose_zinco):
    recomendacao_oxido_zinco = dose_zinco / 0.5
    return recomendacao_oxido_zinco

def recomendar_sulfato_zinco(zinco_solo, dose_zinco):
    if zinco_solo < 5.0:
        recomendacao_sulfato_zinco = f"Recomenda-se aplicar óxido de zinco: {calcular_recomendacao_oxido_zinco(dose_zinco)} kg/ha.\nAlém disso, recomenda-se pulverizações com sulfato de zinco, com 6 a 8 g/L na bomba."
    else:
        recomendacao_sulfato_zinco = "Não é necessária a aplicação de óxido de zinco.\nRecomenda-se pulverizações com sulfato de zinco, com 6 a 8 g/L na bomba, de 3 a 4 aplicações por ano."
    return recomendacao_sulfato_zinco


def calcular_compra_zinco(recomendacao_oxido_zinco, area_talhao):
    quantidade_sulfato_zinco = 8 * area_talhao * 400 /1000
    quantidade_oxido_zinco = recomendacao_oxido_zinco * area_talhao


    return quantidade_sulfato_zinco, quantidade_oxido_zinco


