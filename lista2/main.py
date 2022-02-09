from funcoes import createRules, addVar, addValues, encadeamentoFrente, encadeamentoTras

"""
From the moment I understood the weakness of my flesh, it disgusted me.
I craved the strength and certainty of steel.
I aspired to the purity of the Blessed Machine.
Your kind cling to your flesh, as if it will not decay and fail you.
One day the crude biomass that you call a temple will wither, and you will beg my kind to save you.
But I am already saved, for the Machine is immortal...
...even in death I serve the Omnissiah
"""

def chatbot():
    while True:
        print("----MENU---- ")
        print("REGRAS - para criar regras")
        print("VARIAVEIS - para criar variaveis")
        print("VALORES - para atribuir valores")
        print("FRENTE - para realizar o encadeamento para frente")
        print("TRAS - para realizar o encadeamento para tras")
        print("MISTO - para realizar o encadeamento misto")
        print("EXIT - para sair do programa")

        entrada = input("Digite uma funcao: ")

        if entrada == "REGRAS":
            createRules()

        if entrada == "VARIAVEIS":
            addVar()

        if entrada == "VALORES":
            addValues()

        if entrada == "FRENTE":
            encadeamentoFrente()

        if entrada == "TRAS":
            encadeamentoTras()

        if entrada == "MISTO":
            encadeamentoFrente()
            encadeamentoTras()

        if entrada == "EXIT":
            break

chatbot()



