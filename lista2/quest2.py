dor_de_cabeca = False
febre = False

# Resfriado e h3n2
espirro = False

# Resfriado
coriza = False

# H1N1 e Dengue
dor_articulacao = False

# H1N1
olhos_irritados = False

# h3n2 e covid
dor_na_garganta = False

# Covid19
falta_de_ar = False

# Dengue
dor_atras_olhos = False

diagnostico = False


def factual_base():
    global dor_de_cabeca

    dor_de_cabeca = True


def diagnostico_print(diagnostico):
    print(f'Diagnóstico é {diagnostico}')


if __name__ == '__main__':
    factual_base()

    print('-----------------------')
    print('QUAIS SINTOMAS VOCÊ TEM')
    print('dor_de_cabeca, febre')
    print('espirro, coriza')
    print('dor_articulacao')
    print('olhos_irritados, diarreia')
    print('dor_na_garganta, falta_de_ar')
    print('dor_atras_olhos')
    print('-----------------------')

    sintomas = input('Descreva sintomas: ')
    print(sintomas)
    while True:
        if dor_de_cabeca and febre and dor_articulacao and olhos_irritados:
            diagnostico_print("H1N1")
            break

        if dor_de_cabeca and febre and dor_articulacao:
            diagnostico_print("Dengue")
            break

        if dor_de_cabeca and febre and espirro:
            diagnostico_print("H3N2")
            break

        if dor_de_cabeca and febre and falta_de_ar:
            diagnostico_print("COVID19")
            break

        if dor_de_cabeca and coriza and espirro:
            diagnostico_print("Resfriado")
            break

        if dor_de_cabeca:
            diagnostico_print("Dor de cabeça, tome um analgésico")
            break

        if "febre" in sintomas:
            febre = True

        if "espirro" in sintomas:
            espirro = True

        if "coriza" in sintomas:
            coriza = True

        if "dor_articulacao" in sintomas:
            dor_articulacao = True

        if "olhos_irritados" in sintomas:
            olhos_irritados = True

        if "diarreia" in sintomas:
            diarreia = True

        if "dor_na_garganta" in sintomas:
            dor_na_garganta = True

        if "falta_de_ar" in sintomas:
            falta_de_ar = True

        if "dor_atras_olhos" in sintomas:
            dor_atras_olhos = True
