#Introdução às listas mutáveis
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
# string = 'ABCDE'  # 5 caracteres 
# # print(bool([]))  # falsy
# # print(lista_1, type(lista_1))
# #        0    1      2              3    4
# #       -5   -4     -3             -2   -1
lista_1 = [123, True, 'Caio Vinicius', 1.7, []]
lista_1[-3] = 'Caio Vinicius Ferreira'
lista_adc = input('Digite algo na lista_1: ')
lista_1.append(lista_adc)
print(lista_1)
print(lista_1[0], type(lista_1[1])) 

# #  SC 3  .  81 = alterando uma lista_1 com índice:
# # del(), append(), e pop().
# """
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis:
#     append, insert, pop, del, clear, extend, +
# Create Read Update   Delete
# Criar, ler, alterar, apagar = lista_1[i] (CRUD)
# """
# #        0   1   2   3   4   5
lista_2 = [10, 20, 30, 40, 50, 60]
del lista_2[2] # deletando índice da lista_1 
print(lista_2)
print(lista_2[2])
lista_2.append(171) # adiciona índice na lista_1
lista_2.pop() # removeo último índice da lista_1 (171)
lista_2.append(172)
ultimo_valor = lista_2.pop(3) # removendo índice ex:(3)
# ultimo_valor = índice removido da lista_1 
print(lista_2, 'Removidoos: ', ultimo_valor)
# OBS = lista_1 com mais de 1k de item, recomendado remover os itens pelo fim da lista_1; pop()

#  SC 3  .  82 
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#          0    1   2   3
lista_3 = [10, 20, 30, 40]
lista_3.append('Caio')
nome = lista_3.pop()
lista_3.append(171)
del lista_3[0]
lista_3.insert(0,172) # adc item na lista insert(i, adc/obj)
print(lista_3,'Removido: ',nome)

#  SC 3  . 83 
'''extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
lista_4 = [1, 2, 3]
lista_5 = [4, 5, 6]
lista_6 = [7, 8, 9]
lista_4.extend(lista_5) # faz estende a lista cm outras lista
lista_4.extend(lista_6)
print(lista_4)
