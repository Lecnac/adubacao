def calcular_dose_boro(teor_boro_solo):
    if teor_boro_solo < 0.6:
        dose_boro = 4.0
    elif 0.6 <= teor_boro_solo <= 1.0:
        dose_boro = 3.0
    else:
        dose_boro = 2.0
    return dose_boro

def calcular_recomendacao_ulexita(teor_boro_solo, dose_boro):
    if teor_boro_solo < 1.0:
        recomendacao_ulexita = dose_boro / 0.1
    else:
        recomendacao_ulexita = 0.0  # Não recomenda ulexita se o teor de boro for maior ou igual a 1.0
    return recomendacao_ulexita

def calcular_recomendacao_acido_borico(dose_boro):
    recomendacao_acido_borico = dose_boro / 0.17
    return recomendacao_acido_borico

def calcular_compra_ulexita_acido_borico(recomendacao_acido_borico, recomendacao_ulexita, area_talhao):
    quantidade_ulexita = recomendacao_ulexita * area_talhao
    quantidade_acido_borico = recomendacao_acido_borico * area_talhao
    return quantidade_ulexita, quantidade_acido_borico