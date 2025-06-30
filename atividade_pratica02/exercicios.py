# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
print('############## EXERCÍCIO 01 ################')
valor_reais = float(input("Qual valor em reais você deseja converter? "))
taxa_dolar = 5.20
taxa_euro = 6.15

print(F"""
    ---RESULTADO---
    R$ {valor_reais} equivale a:
    U$S {valor_reais / taxa_dolar:.2f} (dólar)
    € {valor_reais / taxa_euro:.2f} (euro)    
""")

# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
print('############## EXERCÍCIO 02 ################')
produto = {
    "nome": "Camiseta",
    "preco": 50.00,
    "desconto": 20
}

print(F"""
    ---RESUMO DO PEDIDO---
      
      Item: {produto['nome']}
      Valor: R$  {produto['preco']}
    
      Total com desconto à vista: { produto['preco'] - (produto['preco'] * (produto['desconto'])/ 100) }
""")

# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
print('############## EXERCÍCIO 03 ################')
print(f"Média final: { ((nota1 + nota2 + nota3) / 3 ):.2f} ")

# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
print('############## EXERCÍCIO 04 ################')
distancia = 300
combustivel = 25

print(F"""
    Dados do consumo:
      
    Distância percorrida: {distancia}km
    Cosbustível gasto: {combustivel} l.

    Consumo médio: {distancia / combustivel:.2f} km/l
      """)