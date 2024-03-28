# Exercícios SC 3 . 54
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#
print('- - - Escolhar um número para saber se é IMPAR ou PAR - - -')
print('=+='*20)
#
num_1 = int(input('\nDigite um número: '))
resultado = num_1 % 2 
#
if resultado == 0:
    print(f'O número {num_1} é PAR')
else:
    print(f'O número {num_1} é IMPAR')
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#
try: 
    nome = str(input('\nQual seu nome? ')).strip().capitalize()
    horas = int(input('Digite um horário em números inteiros: '))
    #
    if horas >= 5 and horas <= 11:  
        print(f'Tenha um Bom - Dia, {nome} !')
    elif horas >= 12 and horas <= 17:
        print(f'Tenha uma Boa - Tarde, {nome} ! ')
    elif horas >= 18 and horas <= 23:
        print(f'Boa - Noite, {nome} !')
    elif horas >= 0 and horas <= 4:
        print(f'Ainda está de Madrugada, {nome}')
    else: 
        print('\nNão conheço esse horário !!')
except: 
    print(f'\nPor favor digite apenas, números inteiros.')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = str(input('\nDigite seu nome: ')).strip().capitalize()
tamanho_nome = len(nome)
#
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f'O seu nome {nome} é CURTO')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'O seu nome {nome} é NORMAL')
    else:
        print(f'Seu nome {nome} é muito GRANDE')
else:
    print('\nDigite mais de uma letra!')
