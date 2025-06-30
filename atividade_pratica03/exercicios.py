# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o 
# em uma das seguintes categorias: 

# *Criança (0-12 anos), 
# *Adolescente (13-17 anos), 
# *Adulto (18-59 anos) ou 
# *Idoso (60 anos ou mais).
print("########## EXERCÍCIO 01 #########")
while True:
    try: 
        idade = int(input("Informe a idade: "))

        if idade < 0:
            print("Idade inválida")
        elif idade >= 0 and idade <= 12:
            print("É uma criança (0-12 anos)")
            break
        elif idade > 12 and idade <= 17:
            print("É um adolescente (13-17 anos)")
            break
        elif idade > 17 and idade <= 59:
            print("É um adulto (18-59 anos)")
            break
        elif idade > 60:
            print("É um idoso  (60 anos ou mais)")
            break
    except ValueError:
        print("Entrada inválida")

# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"
print("########## EXERCÍCIO 02 #########")
while True:
    try: 
        peso = float(input("Informe seu peso: "))
        altura = float(input("Informe sua altura: "))
        imc = peso / (altura * altura)

        if peso < 0 or altura < 0:
            print("Altura ou peso inválidos")
        elif imc < 18.5:
            print("Abaixo do peso")
            break
        elif imc > 18.5 and imc < 25:
            print("Peso normal")
            break
        elif imc > 25 and imc < 30:
            print("Sobreopeso")
            break
        elif imc > 30:
            print("Obeso")
            break
    except ValueError:
        print("Entrada inválida")

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
print("########## EXERCÍCIO 03 #########")
while True:
    try: 
        temperatura = int(input("Informe a temperatura que deseja converter: "))
        conversao_origem = input("Escolha qual a escala de tempetura da ORIGEM: (C) para Celsius, (F) para Fahrenheit e (K) para Kelvin -> ")
        conversao_destino = input("Escolha qual escala deseja CONVERTER: (C) para Celsius, (F) para Fahrenheit e (K) para Kelvin -> ")

        if conversao_origem == 'C' and conversao_destino == 'F':
            print(f"{(temperatura * (9 / 5)) + 32}  °F")
            break
        elif conversao_origem == 'C' and conversao_destino == 'K':
            print(f"{temperatura+ 273.15}  °K")
            break
        elif conversao_origem == 'F' and conversao_destino == 'C':
            print(f"{(temperatura - 32) * (5 / 9)}  °C")
            break
        elif conversao_origem == 'F' and conversao_destino == 'K':
            print(f"{ ((temperatura - 32) * (5 / 9)) + 273.15 }  °K")
            break
        elif conversao_origem == 'K' and conversao_destino == 'C':
            print(f"{ temperatura - 273.15}  °C")
            break
        elif conversao_origem == 'K' and conversao_destino == 'F':
            print(f"{ ((temperatura - 273.15) * (9 / 5)) + 32 }  °F")
            break
        else :
            print("Opção inválida")
    except ValueError:
        print("Entrada inválida")

# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
print("########## EXERCÍCIO 04 #########")
while True:
    try:
        ano = int(input("Informe o ano que deseja consultas se é bissexto ou não: "))
        if ano <= 0:
            print("Entrada inválida")
        elif ano % 4 != 0:
            print(f"{ano} não é bissexto!")
            break
        elif ano % 100 != 0:
            print(f"{ano} é bissexto!")
            break
        elif ano % 400 == 0:
            print(f"{ano} é bissexto")
            break
        else:
            print(f"{ano} não é bissexto")
            break
    except ValueError:
        print("Entrada inválida")