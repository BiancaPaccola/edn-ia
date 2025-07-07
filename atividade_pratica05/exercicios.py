from datetime import datetime
# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada
print("########## EXERCÍCIO 01 #########")
valor_conta = 120.89
porcentagem_gorgeta = 10
print(F"""
    Total da conta: R$ {valor_conta}
    Taxa de gorjeta: {porcentagem_gorgeta}%

    Gorjeta calculada: {valor_conta * (porcentagem_gorgeta/100):.2f}
""")

# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
print("########## EXERCÍCIO 02 #########")

word = input("Informe a palavra que deseja saber se é ou não palíndromo: ")
word2 = word
def is_pal(word):
    if len(word) == 0 or len(word) == 1:
        print(f"{word2} é palíndromo!")
        return
    if word[0] == word[-1]:
        return is_pal(word[1:-1])
    else:
        print(f"{word2} NÃO é palíndromo!")
        return

is_pal(word)

# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
print("########## EXERCÍCIO 03 #########")
while True:
    try:
        valor_produto = float(input("Informe o valor do produto: "))
        porc_desconto = float(input("Informe a porcetagem do desconto. Ex: 10 para 10% : "))
        
        if valor_produto <= 0 or porc_desconto <= 0:
            print("Entrada inválida")
        else: 
            print(F"""
                Valor final com desconto: {valor_produto - (valor_produto * (porc_desconto / 100)):.2f}
            """)
        break
    except ValueError:
        print("Entrada inválida!")

# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
print("########## EXERCÍCIO 04 #########")
try: 
    data_nasc = input("informe sua data de nascimento no formato dd/mm/aaaa : ")
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = datetime.today()

    resultado = (hoje - nascimento).days

    print(f"Você está vivo há {resultado} dias.")
except ValueError:
    print("Entrada inválida! Precisa usar o formao dd/mm/aaa")
