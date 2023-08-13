
from fosforo import calcular_dose_yorin_grama_metro, calcular_adubacao_fosforo, calcular_compra_yorin
import locale
from calagem import calcular_dose_calagem, calcular_dose_calagem_grama_metro, calcular_compra_calagem
from potassio import calcular_adubacao_potassio, calcular_potassio_corrigido_composto, calcular_dose_kcl, calcular_dose_kcl_grama_metro, calcular_compra_kcl
from gessagem import calcular_dose_gesso  # <--- Adicionar a função calcular_dose_gesso
from magnesio_e_calcio import (calcular_calcio_atualizado, calcular_magnesio_atualizado, calcular_potassio_atualizado, calcular_dose_magnesita, calcular_compra_magnesita, calcular_dose_magnesita_grama_metro, calcular_dose_gesso as calcular_gesso_magnesio_e_calcio)  # Renomear a função para evitar conflitos
from nitrogenio import calcular_recomendacao_nitrogenio, calcular_recomendacao_nitrogenio_descontado_composto, calcular_recomendacao_ureia, calcular_quantidade_nitrogenio_composto, calcular_compra_ureia
from enxofre import calcular_dose_enxofre_e_gesso
from boro import calcular_dose_boro, calcular_recomendacao_ulexita, calcular_recomendacao_acido_borico, calcular_compra_ulexita_acido_borico
from zinco import calcular_dose_zinco, calcular_recomendacao_oxido_zinco, recomendar_sulfato_zinco, calcular_compra_zinco


# Função para converter a entrada com vírgula para float
def input_float(text):
    return float(input(text).replace(',', '.'))

def calcular_dose_gesso_grama_metro(dose_gesso_final, largura_da_rua):
    # Cálculo da dose de gesso em gramas por metro
    dose_gesso_grama_metro = dose_gesso_final * 0.1 * largura_da_rua
    return dose_gesso_grama_metro

def calcular_compra_gesso(dose_gesso_final, area_talhao):
    quantidade_gesso = dose_gesso_final * area_talhao
    return quantidade_gesso


def main():
    # Define a configuração regional para utilizar a vírgula como separador decimal
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Leitura dos parâmetros do usuário para o perfil de 0-20cm
    area_talhao = input_float("Informe o tamanho do talhão (em hectares): ")

    produtividade = input_float("Informe a produtividade esperada (em sacas/hectare): ")
    largura_da_rua = input_float("Informe a largura da rua do talhão (em metros): ")
    ph_solo = input_float("Informe o valor de pH do solo: ")
    materia_organica_solo = input_float("Informe a matéria orgânica do solo (g/dm³): ")
    fosforo_mg_dm3 = input_float("Informe o fosforo (em mg/dm³): ")
    potassio_solo = input_float("Informe a quantidade de potássio no solo (em mmolc/dm³): ")
    calcio_solo = input_float("Informe a quantidade de cálcio no solo (em mmolc/dm³): ")
    magnesio_solo = input_float("Informe a quantidade de magnésio no solo (em mmolc/dm³): ")
    hal_solo = input_float("Informe a quantidade de H+Al no solo (em mmolc/dm³): ")
    al_solo = input_float("Informe a quantidade de alumínio no solo (em mmolc/dm³): ")
    ctc_solo = input_float("Informe a capacidade de troca catiônica (CTC) do solo (em mmolc/dm³): ")
    v_percentual_solo = input_float("Informe a porcentagem de saturação por bases (V%) do solo: ")
    enxofre_solo = input_float("Informe a quantidade de enxofre no solo (em mg/dm³): ")
    boro_solo = input_float("Informe a quantidade de boro no solo (em mg/dm³): ")
    cobre_solo = input_float("Informe a quantidade de cobre no solo (em mg/dm³): ")
    ferro_solo = input_float("Informe a quantidade de ferro no solo (em mg/dm³): ")
    manganes_solo = input_float("Informe a quantidade de manganês no solo (em mg/dm³): ")
    zinco_solo = input_float("Informe a quantidade de zinco no solo (em mg/dm³): ")
    # Leitura do PRNT (separador decimal com vírgula ou ponto, será tratado automaticamente)
    prnt = float(input("Informe o valor do PRNT (90 se não souber): ").replace(',', '.'))
    composto_ton_ha = input_float("Informe a quantidade de composto que iremos aplicar no presente ano (ton/ha): ")
    teor_calcio_composto = input_float("Informe o teor de cálcio no composto (em %): ") / 100.0
    teor_potassio_composto = input_float("Informe o teor de potássio no composto (em %): ") / 100.0
    teor_nitrogenio_composto = input_float("Informe o teor de nitrogênio no composto (em %): ") / 100.0
    teor_magnesio_cal = input_float("Informe o teor de magnésio no calcário utilizado na calagem (em %): ") / 100.0
    analise_foliar_nitrogenio = input_float("Informe o valor da análise foliar de nitrogênio (g/kg): ")


    # Perguntar ao usuário se foi feita coleta e análise do perfil de 20-40cm
    coleta_20_40cm = input("Foi realizada coleta e análise do perfil de 20-40cm? (Digite 'sim' ou 'nao'): ").lower()
    # Verificar se a resposta é positiva e fazer a leitura dos parâmetros adicionais
    if coleta_20_40cm == "sim":
        # Leitura dos parâmetros do usuário para o perfil de 20-40cm
        ph_solo_20_40cm = input_float("Informe o valor de pH do solo (20-40cm): ")
        materia_organica_solo_20_40cm = input_float("Informe a matéria orgânica do solo (g/dm³) (20-40cm): ")
        fosforo_mg_dm3_20_40cm = input_float("Informe o fósforo (em mg/dm³) (20-40cm): ")
        potassio_solo_20_40cm = input_float("Informe a quantidade de potássio no solo (em mmolc/dm³) (20-40cm): ")
        calcio_solo_20_40cm = input_float("Informe a quantidade de cálcio no solo (em mmolc/dm³) (20-40cm): ")
        magnesio_solo_20_40cm = input_float("Informe a quantidade de magnésio no solo (em mmolc/dm³) (20-40cm): ")
        hal_solo_20_40cm = input_float("Informe a quantidade de H+Al no solo (em mmolc/dm³) (20-40cm): ")
        al_solo_20_40cm = input_float("Informe a quantidade de alumínio no solo (em mmolc/dm³) (20-40cm): ")
        ctc_solo_20_40cm = input_float("Informe a capacidade de troca catiônica (CTC) do solo (em mmolc/dm³) (20-40cm): ")
        v_percentual_solo_20_40cm = input_float("Informe a porcentagem de saturação por bases (V%) do solo (20-40cm): ")
        enxofre_solo_20_40cm = input_float("Informe a quantidade de enxofre no solo (em mg/dm³) (20-40cm): ")
        boro_solo_20_40cm = input_float("Informe a quantidade de boro no solo (em mg/dm³) (20-40cm): ")
        cobre_solo_20_40cm = input_float("Informe a quantidade de cobre no solo (em mg/dm³) (20-40cm): ")
        ferro_solo_20_40cm = input_float("Informe a quantidade de ferro no solo (em mg/dm³) (20-40cm): ")
        manganes_solo_20_40cm = input_float("Informe a quantidade de manganês no solo (em mg/dm³) (20-40cm): ")
        zinco_solo_20_40cm = input_float("Informe a quantidade de zinco no solo (em mg/dm³) (20-40cm): ")

        # Calcular a dose de gesso pelo módulo gessagem.py


    else:
        dose_gesso_gessagem = 0


    # Chamada das funções de cálculo de adubação para cada parâmetro
#fosforo
    adubacao_fosforo, quantidade_produto_composto, dose_yorin_kg_ha= calcular_adubacao_fosforo(
        produtividade, fosforo_mg_dm3)
    dose_yorin_grama_metro = calcular_dose_yorin_grama_metro(dose_yorin_kg_ha, largura_da_rua)
    quantidade_yorin = calcular_compra_yorin(dose_yorin_kg_ha, area_talhao)


    dose_calagem = calcular_dose_calagem(v_percentual_solo, ctc_solo, prnt=90)
    dose_calagem_grama_metro = calcular_dose_calagem_grama_metro(dose_calagem, largura_da_rua)
    quantidade_cal = calcular_compra_calagem(dose_calagem, area_talhao)

    adubacao_potassio = calcular_adubacao_potassio(produtividade, potassio_solo)
    potassio_corrigido_composto = calcular_potassio_corrigido_composto(adubacao_potassio, composto_ton_ha,
                                                                       teor_potassio_composto)


    dose_kcl = calcular_dose_kcl(potassio_corrigido_composto)
    dose_kcl_grama_metro = calcular_dose_kcl_grama_metro(dose_kcl, largura_da_rua)
    quantidade_kcl = calcular_compra_kcl(dose_kcl, area_talhao)



    # Atualizar a quantidade de cálcio, magnésio e potássio no solo após a calagem e a aplicação de composto
    novo_calcio_solo = calcular_calcio_atualizado(calcio_solo, dose_calagem, composto_ton_ha,
                                                  teor_calcio_composto, dose_gesso_gessagem)
    novo_magnesio_solo = calcular_magnesio_atualizado(magnesio_solo, teor_magnesio_cal, dose_calagem)
    novo_potassio_solo = calcular_potassio_atualizado(potassio_solo, teor_potassio_composto, composto_ton_ha,
                                                      adubacao_potassio)

    dose_magnesita = calcular_dose_magnesita(novo_magnesio_solo, novo_potassio_solo)
    dose_magnesita_grama_metro = calcular_dose_magnesita_grama_metro (dose_magnesita, largura_da_rua)
    quantidade_magnesita = calcular_compra_magnesita(dose_magnesita, area_talhao)

    # Cálculo da dose de gesso pelo módulo magnesio_e_calcio.py
    dose_gesso_magnesio_e_calcio = calcular_gesso_magnesio_e_calcio(novo_calcio_solo, novo_potassio_solo)  # Corrigido

    # Calcular a quantidade de nitrogênio presente no composto
    quantidade_nitrogenio_composto = calcular_quantidade_nitrogenio_composto(teor_nitrogenio_composto, composto_ton_ha)

    # Calcular a recomendação de nitrogênio
    recomendacao_nitrogenio = calcular_recomendacao_nitrogenio(produtividade, analise_foliar_nitrogenio)

    # Calcular a recomendação de nitrogênio descontando o composto
    recomendacao_nitrogenio_descontado = calcular_recomendacao_nitrogenio_descontado_composto(recomendacao_nitrogenio,
                                                                                              quantidade_nitrogenio_composto)



# Importação do gesso do módulo enxofre
    dose_enxofre, dose_gesso_enxofre = calcular_dose_enxofre_e_gesso(recomendacao_nitrogenio)


    # Escolher a maior dose de gesso entre as duas
    dose_gesso_final = max(dose_gesso_magnesio_e_calcio, dose_gesso_gessagem, dose_gesso_enxofre)

    dose_gesso_grama_metro = calcular_dose_gesso_grama_metro(dose_gesso_final, largura_da_rua)

    quantidade_gesso = calcular_compra_gesso(dose_gesso_final, area_talhao)

    # Calcular a recomendação de ureia
    recomendacao_ureia = calcular_recomendacao_ureia(recomendacao_nitrogenio_descontado)
    quantidade_ureia = calcular_compra_ureia(recomendacao_ureia, area_talhao)

    # Calcular a dose de boro
    dose_boro = calcular_dose_boro(boro_solo)
    # Calcular recomendações dos produtos
    if boro_solo < 1.0:
        recomendacao_ulexita = calcular_recomendacao_ulexita(boro_solo, dose_boro)
        recomendacao_acido_borico = calcular_recomendacao_acido_borico(dose_boro)
    else:
        recomendacao_ulexita = 0.0
        recomendacao_acido_borico = calcular_recomendacao_acido_borico(dose_boro)

    quantidade_ulexita, quantidade_acido_borico = calcular_compra_ulexita_acido_borico(recomendacao_acido_borico, recomendacao_ulexita, area_talhao)

    dose_zinco = calcular_dose_zinco(zinco_solo)
    recomendacao_oxido_zinco = calcular_recomendacao_oxido_zinco(dose_zinco)
    recomendacao_sulfato_zinco = recomendar_sulfato_zinco(zinco_solo, dose_zinco)

    quantidade_sulfato_zinco, quantidade_oxido_zinco = calcular_compra_zinco(recomendacao_oxido_zinco, area_talhao)


    # Exibição dos resultados

    print("Recomendação de adubação para Fosforo: {} kg/ha".format(adubacao_fosforo))
    print("Quantidade de composto necessário para suprir fósforo: {} kg/ha".format(quantidade_produto_composto))

    if dose_yorin_kg_ha is not None:
        print("Recomendação de Yorin: {:.2f} kg/ha".format(dose_yorin_kg_ha))
        print("Recomendação de Yorin: {:.2f} g/m".format(dose_yorin_grama_metro))

    else:
        print("Não há recomendação de Yorin para esta faixa de produtividade e teor de fósforo.")

    print("Dose de Calagem sugerida: {} ton/ha".format(dose_calagem))
    print("Recomendação de calagem: {:.2f} g/m".format(dose_calagem_grama_metro))

    print("Recomendação de adubação para Potássio: {} kg/ha".format(adubacao_potassio))
    print("Dose de KCl sugerida: {} kg/ha".format(dose_kcl))
    print("Dose de KCl sugerida: {} g/m".format(dose_kcl_grama_metro))

    # Exibir a recomendação de gesso ao usuário
    if dose_gesso_final > 0:
        print("Recomendação de Gesso: {:.2f} kg/ha".format(dose_gesso_final))
        print("Recomendação de Gesso: {:.2f} g/m".format(dose_gesso_grama_metro))

    else:
        print("Não há necessidade de aplicação de Gesso.")
        # Exibir a recomendação de magnesita, se necessário

    if dose_magnesita > 0:
        print("Recomendação de Magnesita: {:.2f} kg/ha".format(dose_magnesita))
        print("Recomendação de Magnesita: {:.2f} g/m".format(dose_magnesita_grama_metro))
    else:
        print("Não há necessidade de aplicação de Magnesita.")

    print("Recomendação de Nitrogênio: {} kg/ha".format(recomendacao_nitrogenio))
    print("Recomendação de Ureia: {:.2f} kg/ha".format(recomendacao_ureia))
    if recomendacao_ulexita > 0:
        print(
            "Recomenda-se aplicar {:.2f} kg/ha de ácido bórico, para satisfazer as necessidades a curto prazo da planta, e {:.2f} kg/ha de ulexita, para melhorar o teor de boro no solo a longo prazo".format(
                recomendacao_acido_borico, recomendacao_ulexita))
    else:
        print(
            "Recomenda-se aplicar {:.2f} kg/ha de ácido bórico, para satisfazer as necessidades a curto prazo da planta".format(
                recomendacao_acido_borico))

    print(recomendacao_oxido_zinco)
    print(recomendacao_sulfato_zinco)
    print("-----------------------------------------------------------------------------")
    print("compra de material!!! Em colchetes está a porcentagem do teor da substância requerida")
    print("Quantidade de Ulexita a comprar: {:.2f} kg (10%)".format(quantidade_ulexita))
    print("Quantidade de Ácido Bórico a comprar: {:.2f} kg (17%)".format(quantidade_acido_borico))
    print("quantidade de cal a comprar:{}ton".format(quantidade_cal))
    print("Quantidade de yorin a comprar: {:.2f} kg (18%)".format(quantidade_yorin))
    print("Quantidade de Magnesita a comprar: {:.2f} kg (90%)".format(quantidade_magnesita))
    print("Quantidade de Gesso a comprar: {:.2f} kg (20% calcio; 15% enxofre)".format(quantidade_gesso))
    print("quantidade de ureia a comprar:{}kg (44%)".format(quantidade_ureia))
    print("quantidade de cloreto de potássio a comprar:{}kg (60%)".format(quantidade_kcl))
    print("Quantidade de oxido de zinco a comprar: {:.2f} kg (50%)".format(quantidade_oxido_zinco))
    print("Quantidade de sulfato de zinco a comprar: {:.2f} kg".format(quantidade_sulfato_zinco))
if __name__ == "__main__":
    main()