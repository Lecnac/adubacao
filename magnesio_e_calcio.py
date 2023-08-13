def calcular_calcio_atualizado(calcio_solo, dose_calagem, composto_ton_ha, teor_calcio_composto, dose_gesso):
    # Atualizar o teor de cálcio no solo após a calagem e a aplicação de composto
    teor_calcio_atualizado = calcio_solo + (0.45 * dose_calagem * 1000 / 40) + (teor_calcio_composto * composto_ton_ha * 1000 / 40) + (0.2 * dose_gesso * 1000 / 40)
    return teor_calcio_atualizado

def calcular_magnesio_atualizado(magnesio_solo, teor_magnesio_cal, dose_calagem):
    # Calcular o teor de magnésio atualizado no solo após a calagem
    teor_magnesio_atualizado = magnesio_solo + teor_magnesio_cal * dose_calagem / 24
    return teor_magnesio_atualizado


def calcular_potassio_atualizado(potassio_solo, teor_potassio_composto, composto_ton_ha, adubacao_potassio):
    # Calcular o teor de potássio atualizado no solo após a aplicação do composto
    teor_potassio_atualizado = potassio_solo +  adubacao_potassio / 94
    return teor_potassio_atualizado

def calcular_dose_gesso(teor_calcio_atualizado, teor_potassio_atualizado):
    # Verificar se há necessidade de recomendar a dose de gesso
    if teor_calcio_atualizado / teor_potassio_atualizado < 9:
        dose_gesso = ((teor_potassio_atualizado * 9 - teor_calcio_atualizado)) * 40 * 5
    else:
        dose_gesso = 0

    return dose_gesso

def calcular_dose_magnesita(teor_magnesio_atualizado, teor_potassio_atualizado):
    relacao_mg_k = teor_magnesio_atualizado / teor_potassio_atualizado
    if relacao_mg_k < 2.5:
        dose_magnesita = ((teor_potassio_atualizado * 3) - teor_magnesio_atualizado) *24/ 0.9
    else:
        dose_magnesita = 0
    return dose_magnesita






def calcular_dose_magnesita_grama_metro(dose_magnesita, largura_da_rua):
    # Cálculo da dose de magnesita em gramas por metro
    dose_magnesita_grama_metro = dose_magnesita * 0.1 * largura_da_rua
    return dose_magnesita_grama_metro


def calcular_compra_magnesita(dose_magnesita, area_talhao):
    quantidade_magnesita = dose_magnesita * area_talhao

    return quantidade_magnesita

