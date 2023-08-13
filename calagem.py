def calcular_dose_calagem(v_percentual_solo, ctc_solo, prnt=90):
    #calculo de calagem em ton/ha
    dose_calagem = (70 - v_percentual_solo) * ctc_solo / (prnt * 10)
    return dose_calagem
def calcular_dose_calagem_grama_metro(dose_calagem, largura_da_rua):
        # Cálculo da dose de calagem em gramas por metro

    dose_calagem_grama_metro = dose_calagem * 0.1 * largura_da_rua * 1000
    return dose_calagem_grama_metro

def calcular_compra_calagem(dose_calagem, area_talhao):
    quantidade_cal = dose_calagem * area_talhao

    return quantidade_cal
