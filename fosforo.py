def calcular_adubacao_fosforo(produtividade_sacas_ha, fosforo_mg_dm3):
    tabela_recomendacao = {
        "< 20": {
            "< 15": 20,
            "15-40": 20,
            "> 40": 20
        },
        "20 - 30": {
            "< 15": 40,
            "15-40": 20,
            "> 40": 20
        },
        "30 - 40": {
            "< 15": 60,
            "15-40": 40,
            "> 40": 20
        },
        "40 - 50": {
            "< 15": 80,
            "15-40": 60,
            "> 40": 40
        },
        "50 - 60": {
            "< 15": 80,
            "15-40": 60,
            "> 40": 40
        },
        "60 - 70": {
            "< 15": 100,
            "15-40": 80,
            "> 40": 60
        },
        "70 - 80": {
            "< 15": 120,
            "15-40": 80,
            "> 40": 60
        },
        "> 80": {
            "< 15": 140,
            "15-40": 100,
            "> 40": 60
        }
    }

    faixa_produtividade = None
    if produtividade_sacas_ha < 20:
        faixa_produtividade = "< 20"
    elif produtividade_sacas_ha >= 20 and produtividade_sacas_ha < 30:
        faixa_produtividade = "20 - 30"
    elif produtividade_sacas_ha >= 30 and produtividade_sacas_ha < 40:
        faixa_produtividade = "30 - 40"
    elif produtividade_sacas_ha >= 40 and produtividade_sacas_ha < 50:
        faixa_produtividade = "40 - 50"
    elif produtividade_sacas_ha >= 50 and produtividade_sacas_ha < 60:
        faixa_produtividade = "50 - 60"
    elif produtividade_sacas_ha >= 60 and produtividade_sacas_ha < 70:
        faixa_produtividade = "60 - 70"
    elif produtividade_sacas_ha >= 70 and produtividade_sacas_ha < 80:
        faixa_produtividade = "70 - 80"
    else:
        faixa_produtividade = "> 80"

    if faixa_produtividade in tabela_recomendacao:
        if fosforo_mg_dm3 < 15:
            faixa_fosforo = "< 15"
        elif fosforo_mg_dm3 >= 15 and fosforo_mg_dm3 <= 40:
            faixa_fosforo = "15-40"
        else:
            faixa_fosforo = "> 40"

        # Verificando se a faixa_fosforo está presente na tabela de recomendação
        if faixa_fosforo in tabela_recomendacao[faixa_produtividade]:
            adubacao_fosforo_kg_ha = tabela_recomendacao[faixa_produtividade][faixa_fosforo]

            # Cálculo da quantidade de produto composto necessário em kg/ha
            # Considerando que o produto composto contém 1,5% de fósforo
            quantidade_produto_composto_kg_ha = adubacao_fosforo_kg_ha / 0.015

            # Verifica se o nível de fósforo está baixo (abaixo de 12 mg/dm³)
            dose_yorin_kg_ha = None
            if fosforo_mg_dm3 < 12:
                dose_yorin_kg_ha = adubacao_fosforo_kg_ha / 0.18
            return adubacao_fosforo_kg_ha, quantidade_produto_composto_kg_ha, dose_yorin_kg_ha

        else:
            return None, None, None
    else:
        return None, None, None

def calcular_dose_yorin_grama_metro(dose_yorin_kg_ha, largura_da_rua):

    # Cálculo da dose de calagem em gramas por metro

    dose_yorin_grama_metro = dose_yorin_kg_ha * 0.1 * largura_da_rua
    return dose_yorin_grama_metro

def calcular_compra_yorin(dose_yorin_kg_ha, area_talhao):
    quantidade_yorin = dose_yorin_kg_ha * area_talhao

    return quantidade_yorin
