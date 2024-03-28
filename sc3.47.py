# Exercício
#
'''
pegar nome e idade de usuário
Exebir : 
Nome invertido=OK 
Se nome contém espaços=OK 
Se nome tem {n} letras=OK  
Primeira letra de nome=OK 
Última letra de nome=OK 
Se nada for digitador exebir 'Desculpe, você deixou campos vazios'.
'''
nome_usuario = str(input(f'Informe seu nome: ')).capitalize().strip()
idade_usuario = int(input('Informe sua idade: '))
#
if nome_usuario and idade_usuario:
    print(f'\nSeu nome é {nome_usuario}.')
    print(f'Seu nome invertido é {nome_usuario[::-1]}.')
    #
    if ' ' in nome_usuario: # pegando se há espaço no nome
     print(f'Seu nome contém {nome_usuario.count(' ')} espaços.')
    else:
       print('Seu nome NÃO contém espaços.')
    print(f'Seu nome tem {len(nome_usuario.replace(' ',''))} letras.') # contando somente as strings sem contar os espaços
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[-1]}')
#
else:
    print('Desculpe você deixou campos vazios!')



