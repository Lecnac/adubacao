def calcular_dose_enxofre_e_gesso(recomendacao_nitrogenio):
    dose_enxofre = recomendacao_nitrogenio / 8
    dose_gesso_enxofre = dose_enxofre / 0.15
    return dose_enxofre, dose_gesso_enxofre
