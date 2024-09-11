""" exercicio 1

try:

    entrada = input()


    print("Ola, em que posso ajudar?")

except ValueError:

    print("ERRO")

"""




""" exercicio 2

try:
    entrada = input()
    horas = int(input())
except ValueError:
    print("ERRO")
    exit()

if horas < 0 or horas > 23:
    print("ERRO")

else:

    if 5 <= horas <= 11:
        print("Bom dia, em que posso ajudar?")
    elif 12 <= horas <= 18:
        print("Boa tarde, em que posso ajudar?")
    else:
        print("Boa noite, em que posso ajudar?")


"""

""" exercicio 3

# Rodrigo Cont


def dobro(numero):
    return numero * 2 + 29

try:

    produto_input = input().lower()

    estoque = ["hidratante labial", "perfume", "delineador"]

    if produto_input in estoque:

        print("Sim, tenho esse produto!")
    else:

        print("Infelizmente nao tenho esse produto")

except:
        print("ERRO")
"""

"""" exercicio 4
preco_a = 8.90
preco_b = 11.30
preco_c = 6.70

try:
    quantidade_a = float(input())
    quantidade_b = float(input())
    quantidade_c = float(input())



    total_a = (quantidade_a / 100) * preco_a
    total_b = (quantidade_b / 100) * preco_b
    total_c = (quantidade_c / 100) * preco_c

    total = total_a + total_b + total_c

    print(f"R$ {total:.2f}".replace('.', ','))

except ValueError:
    print("ERRO")
"""

""""  exercicio 5

from datetime import datetime


try:
    data_referencia = input()


    data_referencia = datetime.strptime(data_referencia, '%d/%m/%Y')


    produtos = [
        ("B", datetime.strptime('12/11/2023', '%d/%m/%Y')),
        ("C", datetime.strptime('25/01/2024', '%d/%m/%Y')),
        ("D", datetime.strptime('17/05/2024', '%d/%m/%Y')),
        ("E", datetime.strptime('09/07/2024', '%d/%m/%Y')),
        ("A", datetime.strptime('07/09/2024', '%d/%m/%Y'))
    ]

    produtos_lancados = []

    for produto, data_lancamento in produtos:

        if data_referencia >= data_lancamento:
            produtos_lancados.append(produto)

    if produtos_lancados:
        print(", ".join(produtos_lancados))
    else:
        print("NENHUM")

except ValueError:

    print("ERRO")

"""


"""" Exercicio 6
try:

    quantidade = int(input())


    if quantidade <= 0:
        print("ERRO")
    else:

        embalagem_C = 500
        embalagem_B = 300
        embalagem_A = 180
        quantidade_A = 0
        quantidade_B = 0
        quantidade_C = 0

        quantidade_C = quantidade // embalagem_C
        resto = quantidade % embalagem_C
        if resto > 480:
            quantidade_C+=1
        elif resto > 360:
            quantidade_B+=1
            quantidade_A+=1
        elif resto > 300:
            quantidade_A = quantidade_A + 2
            flag=False
        elif resto <=300 and resto >180:
            quantidade_B+=1
        elif resto !=0:
            quantidade_A+=1



    print("A({}) B({}) C({})".format(quantidade_A, quantidade_B, quantidade_C))

except ValueError:
    # Caso a entrada não seja um número inteiro
    print("ERRO")

"""


