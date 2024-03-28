"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True
#
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    #
    if nome == 'sair':
        break
#
print('Acabou')

#  SC  3 . 60 - While e break - Condição em detalhes
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0
#
while contador <= 10:
    contador = contador + 1
    print(contador)
#
print('Acabou')

#  SC  3 .  61 - Operadores de atribuição aritméticos
"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 10
#
contador /= 5
print(contador)
