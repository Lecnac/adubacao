def calcular_adubacao_potassio(produtividade, potassio_mg_dm3):
    tabela_adubacao_potassio = {
        "< 20": [120, 100, 80],
        "20 - 30": [40, 120, 100],
        "30 - 40": [60, 140, 120],
        "40 - 50": [220, 180, 140],
        "50 - 60": [260, 220, 180],
        "60 - 70": [300, 260, 220],
        "70 - 80": [360, 300, 260],
        "> 80": [400, 340, 300]
    }

    # Determinar a faixa de produtividade
    faixa_produtividade = ""
    if produtividade < 20:
        faixa_produtividade = "< 20"
    elif 20 <= produtividade < 30:
        faixa_produtividade = "20 - 30"
    elif 30 <= produtividade < 40:
        faixa_produtividade = "30 - 40"
    elif 40 <= produtividade < 50:
        faixa_produtividade = "40 - 50"
    elif 50 <= produtividade < 60:
        faixa_produtividade = "50 - 60"
    elif 60 <= produtividade < 70:
        faixa_produtividade = "60 - 70"
    elif 70 <= produtividade < 80:
        faixa_produtividade = "70 - 80"
    else:
        faixa_produtividade = "> 80"

    if potassio_mg_dm3 < 1.5:
        adubacao_potassio = tabela_adubacao_potassio[faixa_produtividade][0]
    elif 1.5 <= potassio_mg_dm3 < 3.0:
        adubacao_potassio = tabela_adubacao_potassio[faixa_produtividade][1]
    else:
        adubacao_potassio = tabela_adubacao_potassio[faixa_produtividade][2]

    return adubacao_potassio

def calcular_potassio_corrigido_composto(adubacao_potassio, composto_ton_ha, teor_k2o_composto):
    # Calcular o teor de potássio no composto
    potassio_composto = teor_k2o_composto * composto_ton_ha*1000

    # Calcular o potássio corrigido pelo composto
    potassio_corrigido_composto = adubacao_potassio - potassio_composto
    return potassio_corrigido_composto

def calcular_dose_kcl(potassio_corrigido_composto):
    # Realizar o cálculo da dose de KCL (cloreto de potássio)
    dose_kcl = dose_kcl = potassio_corrigido_composto / 0.60
    return dose_kcl

def calcular_dose_kcl_grama_metro(dose_kcl, largura_da_rua):

    # Cálculo da dose de kcl em gramas por metro

    dose_kcl_grama_metro = dose_kcl * 0.1 * largura_da_rua
    return dose_kcl_grama_metro

def calcular_compra_kcl(dose_kcl, area_talhao):
    quantidade_kcl = dose_kcl * area_talhao

    return quantidade_kcl

