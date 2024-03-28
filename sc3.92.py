"""
Imprecisão de ponto flutuante
Formato de ponto flutuante de precisão dupla IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
#
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
#
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3))

#  SC  3  .  93
"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa linda o Caio       '
lista_frases_cruas = frase.split(',')
#
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
frases_unidas = ', '.join(lista_frases)
#
print('1', lista_frases_cruas)
print('2', lista_frases) #
print('3', frases_unidas) # join

#  SC  3  .  94
"""
Lista de listas e seus índices
""" 
salas = [ #listas dentro de lista
    # 0        1
    ['Maria', 'Helena',],# lista 0
    # 0
    ['Elaine',], # lista 1
    # 0       1       2      3
    ['Luiz', 'Caio', 'João',(00,10,20,30)], # lista 2
]
#
print(salas[1][0]) # [lista][índice da lista]
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3])
#
print('__'*25)
#
for sala in salas:
    print(f'\nA sala é {sala}')
    for aluno in sala:
        print(aluno)

