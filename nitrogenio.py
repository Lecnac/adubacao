
def calcular_recomendacao_nitrogenio(produtividade, analise_foliar_nitrogenio):




    tabela_recomendacao = {
        "< 20": (180, 140, 120),
        "20 - 30": (200, 160, 140),
        "30 - 40": (240, 200, 160),
        "40 - 50": (260, 220, 180),
        "50 - 60": (300, 240, 200),
        "60 - 70": (350, 260, 220),
        "70 - 80": (400, 280, 240),
        "> 80": (450, 350, 240)
    }

    # Encontrar a faixa de produtividade correspondente

    faixa_produtividade = None
    if produtividade < 20:
        faixa_produtividade = "< 20"
    elif produtividade >= 20 and produtividade < 30:
        faixa_produtividade = "20 - 30"
    elif produtividade >= 30 and produtividade < 40:
        faixa_produtividade = "30 - 40"
    elif produtividade >= 40 and produtividade < 50:
        faixa_produtividade = "40 - 50"
    elif produtividade >= 50 and produtividade < 60:
        faixa_produtividade = "50 - 60"
    elif produtividade >= 60 and produtividade < 70:
        faixa_produtividade = "60 - 70"
    elif produtividade >= 70 and produtividade < 80:
        faixa_produtividade = "70 - 80"
    else:
        faixa_produtividade = "> 80"

    # Encontrar a recomendação de nitrogênio na tabela de acordo com a faixa e a análise foliar
    recomendacao_nitrogenio = None
    if analise_foliar_nitrogenio < 20:
        recomendacao_nitrogenio = tabela_recomendacao[faixa_produtividade][0]
    elif analise_foliar_nitrogenio >= 20 and analise_foliar_nitrogenio < 30:
        recomendacao_nitrogenio = tabela_recomendacao[faixa_produtividade][1]
    else:
        recomendacao_nitrogenio = tabela_recomendacao[faixa_produtividade][2]

    return recomendacao_nitrogenio

def calcular_quantidade_nitrogenio_composto(teor_nitrogenio_composto, composto_ton_ha):
    # Calcular a quantidade de nitrogênio presente no composto (kg/ha)
    quantidade_nitrogenio_composto = teor_nitrogenio_composto * composto_ton_ha * 1000
    return quantidade_nitrogenio_composto

# Alteração:* Função para calcular a recomendação de nitrogênio descontado o composto.
def calcular_recomendacao_nitrogenio_descontado_composto(recomendacao_nitrogenio, quantidade_nitrogenio_composto):
    recomendacao_nitrogenio_descontado_composto = recomendacao_nitrogenio - (quantidade_nitrogenio_composto / 2)
    return recomendacao_nitrogenio_descontado_composto
# Alteração:* Função para calcular a recomendação de ureia.
def calcular_recomendacao_ureia(recomendacao_nitrogenio_descontado_composto):
    recomendacao_ureia = recomendacao_nitrogenio_descontado_composto / 0.44
    return recomendacao_ureia

def calcular_compra_ureia(recomendacao_ureia, area_talhao):
    quantidade_ureia = recomendacao_ureia * area_talhao

    return quantidade_ureia

