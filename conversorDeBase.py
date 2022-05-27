print("pode passa um numero que esteja nas bases 2, 4, 8, 10, 16")
bolean = True
print("opicao")

while bolean:
    print("..........................")
    print("1 - passa da base 2 para 4")
    print("2 - passa da base 4 para 2")
    print("3 - passa da base 2 para 8")
    print("4 - passa da base 8 para 2")
    print("5 - passa da base 2 para 10")
    print("6 - passa da base 10 para 2")
    print("7 - passa da base 2 para 16")
    print("8 - passa da base 16 para 2")
    print("9 - passa da base 4 para 8")
    print("10 - passa da base 8 para 4")
    print("11 - passa da base 4 para 10")
    print("12 - passa da base 10 para 4")
    print("13 - passa da base 4 para 16")
    print("14 - passa da base 16 para 4")
    print("16 - passa da base 8 para 10")
    print("17 - passa da base 10 para 8")
    print("18 - passa da base 8 para 16")
    print("19 - passa da base 16 para 8")
    print("20 - passa da base 10 para 16")
    print("21 - passa da base 16 para 10")
    print("0 - para parar o codigo")
    print(".............................")

    variavel = int(input("digite a sua opicao: "))
    teste = variavel == 0

    if teste:
        print("calculadora desligada.....")
        break


# base 2 para 10

base2_base10 = str(input("numero na base 2: "))
base2_base10 = list(base2_base10)
lista1_expoente = []
lista_soma = []

for k in range(len(base2_base10)):
    lista1_expoente.append(pow(2, k))

for k in range(len(base2_base10)):
    base2_base10[k] = int(base2_base10[k])

base2_base10 = base2_base10[::-1]

for k in range(len(base2_base10)):
    lista_soma.append(base2_base10[k] * lista1_expoente[k])

lista_soma = sum(lista_soma)


print(f"o numero digitado na base 2 para base 10 {lista_soma}")

# base 10 para 2

base10_base2 = []

numero = int(input("digite um numero na base 10"))

while numero > 2:
    conta = numero % 2
    print(conta)
    base10_base2.append(conta)
    numero = numero // 2

base10_base2.append(numero % 2)

if numero == 2:
    base10_base2.append(numero // 2)

base10_base2 = base10_base2[::-1]

valor = ""

for k in range(len(base10_base2)):
    base10_base2[k] = str(base10_base2[k])
    valor = valor + base10_base2[k]

valor = int(valor)

print(valor)
