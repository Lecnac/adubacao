def calcular_dose_gesso(v_percentual_solo_20_40cm, ctc_solo_20_40cm):
    if v_percentual_solo_20_40cm < 35:
        dose_gesso = (50 - v_percentual_solo_20_40cm) * ctc_solo_20_40cm / 500
        return dose_gesso
    else:
        return 0
