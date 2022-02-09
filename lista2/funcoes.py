data = {"variaveis": [], "valores": [], "se": [], "entao": [], "rules": [],
        "baseData":["referencias_sim=sim","e_bacharel_ou_superior_nao=nao"],
        "objetivo": ['rendimento_alto=alto']}

def searchObj(lista, obj):
    for x in lista:
        if x == obj:
            print("Encontramos o objetivo: " + str(obj))

def searchVar(lista, var):
    x = 0
    for n in lista:
        if n == var:
            return x
        x += 1
    return -1

def addVar():
    print("Digite as variaveis ou digite EXIT para sair...")

    while True:
        i = input("Digite uma variavel: ")

        if i != "EXIT":
            data["variaveis"].append(i)
        else:
            break

def addValues():
    print("Digite os valores para as variaveis ou digite EXIT para sair...")

    for x in range(len(data["variaveis"])):
        i = input("Digite um valor: ")

        if i != "EXIT":
            data["valores"].append(i)
        else:
            break

def selectOperators():
    i = input("Digite o operador AND ou ENTAO")

    if i == "AND":
        return "and"
    else:
        return "entao"

def rmvSame(lista):
    new_lista = []

    for i in lista:
        if i not in new_lista:
            i = i.replace(" ", "")
            new_lista.append(i)

    return new_lista

def createRules():
    rule = ""

    while True:
        if rule[-6:-1].replace(" ", "") != 'entao':
            rEntao = True

        else:
            rEntao = False

        m = input("Digite a primeira variavel: ")
        mIndex = searchVar(data["variaveis"], m)

        if mIndex == -1:
            print("Digite uma variavel pertencente ao banco de dados e tente novamente...")
            return -1
        else:
            rule += f' {data["variaveis"][mIndex]} = {data["valores"][mIndex]} '

        if rEntao:
            op = selectOperators()

            data["se"].append(rule)

            rule += "/" + str(op) + "/"


        else:
            e = f' {data["variaveis"][mIndex]} = {data["valores"][mIndex]} '

            data["rules"].append(rule)

            data["entao"].append(e)

            print("A regra foi criada com sucesso: ")
            print(rule)

def encadeamentoFrente():

    for x in data["rules"]:
        se = []
        entao = []

        l = x.split("/entao/")

        se.append(l[0].split("/and/"))

        se = rmvSame(se[0])

        entao.append(l[1].split("/and/")[-1])

        entao = rmvSame(entao)

        if set(data["baseData"]).intersection(se) and len(set(data["baseData"])).intersection(entao):
            data["baseData"].append(entao[0])
            searchObj(data["baseData"])
            print(data["baseData"])



def encadeamentoTras():

    for x in data["objetivo"]:
        for y in data["entao"]:
            if x == y:
                data["baseData"].append(y)

                n = data["entao"].index(y)

                if len(data["objetivo"]) == 0:
                    print("Encadeamento realizado!")
                    print(data["baseData"])

                else:
                    data["objetivo"].remove(n)

                    z = data["se"][y].split("/and/")

                    for w in z:
                        w.replace(" ", "")
                        data["objetivo"].append(w)

        if len(data["objetivo"]) != 0:
            print("Não encontramos nenhuma correspondencia")