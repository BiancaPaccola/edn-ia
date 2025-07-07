# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
print("########## EXERCÍCIO 01 ##########")
def calculadora ():
  print("- Digite 1 para somar dois valores\n- Digite 2 para subtrair dois valores\n- Digite 3 para multiplicar dois valores\n- Digite 4 para dividir dois valores\n- Digite 5 para realizar uma potência entre dois valores\n- Digite 6 para realizar uma radiciação entre dois valores\n- Digite qualquer outro número para sair")
  opcao = int(input("Digite uma opção: "))
  if opcao <= 0 or opcao > 6:
    print("Você saiu...")
  else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if opcao == 1:
      print(num1+num2)
    elif opcao == 2:
      print(num1-num2)
    elif opcao == 3:
      print(num1*num2)
    elif opcao == 4:
        if num2 != 0: 
            print(num1 / num2)
        while num2 == 0:
            print("\nNão é possível dividir por Zero!\nInforme o segundo valor novamente: ")
            num2 = int(input("Segundo valor: "))
            if num2 != 0: 
                print(num1 / num2)
            else:
                continue
    elif opcao == 5:
      print(num1**num2)
    elif opcao == 6:
      print(num1**(1/num2))
calculadora()

# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.
print("########## EXERCÍCIO 02 ##########")

notas = []
while True:
   try:
    entrada = input("Informe uma nota por vez, seguido de ENTER. Para sair pressiona S: ")
    if entrada == 's' or entrada == 'S':
        break
    if float(entrada) >= 0 and float(entrada) <= 10:
        notas.append(float(entrada))
   except ValueError:
      print("Entrada inválida")

total_notas = 0
qtde_notas = 0
for i in notas:
    total_notas += i
    qtde_notas += 1

if not notas:
   print("A lista de notas está vazia")
else: 
   print(total_notas / qtde_notas)

# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.
print("########## EXERCÍCIO 03 ##########")
senha = input("Informe a senha: ")
tamanho_senha = 0
tem_numero = False

for car in senha:
    if car.isdigit():
        tem_numero = True
    tamanho_senha += 1

if tem_numero == True and tamanho_senha >= 8:
    print("Senha válida")
else:
    print("Senha inválida")

# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
print("########## EXERCÍCIO 04 ##########")
lista_numeros = []
while True:
    try:
        entrada_usuario = input("Digite um número ou S para sair: ")

        if entrada_usuario.upper() == 'S':
            print("Saindo...")
            break

        lista_numeros.append(int(entrada_usuario))
    except ValueError:
        print("Entrada inválida")

num_par = 0
num_impar = 0
for i in lista_numeros:
    if i % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

print(F"""
    Números pares: {num_par}
    Números ímpares: {num_impar}
""")