# Exercício guiado com While
# SC  3 . 66/68 = Exercício Calcularadora Part1
#
print('¨¨'*10, 'C A L C U L A D O R A ', '¨¨'*10)
print('¨¨'*40)
#
while True:
    try:
        num_1 = float(input('Digite um número:  '))
        num_2 = float(input('Digite outro número:  '))
    except:
        print('Digite apenas números')
        continue
    #
    print('¨¨'*40)
    #
    operacao = input('Qual operador deseja usar: \n[+]adição \n[-]subtração \n[x]multiplicação \n[/]divisão   :  ')
    operacao_permitida = '+-x/'
    #
    if operacao not in operacao_permitida:
        print(f'Você digitou os operadores da soma errado!')
        continue
    #
    if len(operacao) > 1:
        print(f'Digite apenas um operador!')
        continue
    #
    if operacao == '+':
        soma_d_mais = num_1 + num_2
        print(f'\nA soma de {num_1} + {num_2} é = {soma_d_mais:.0f}')
    elif operacao == '-':
        soma_d_menos = num_1 - num_2 
        print(f'\nA soma de {num_1} - {num_2} é = {soma_d_menos:.0f}')
    elif operacao == 'x':
        soma_d_multp = num_1 * num_2
        print(f'\nA soma de {num_1} x {num_2} é = {soma_d_multp:.0f}')
    elif operacao == '/':
        soma_d_div = num_1 / num_2
        print(f'\nA soma de {num_1} / {num_2} é = {soma_d_div}')
    #
    sair = input('Aperte [S] para sair/qualquer tecla para continuar somando: ').strip().lower().startswith('s')
    if sair is True:
        break
