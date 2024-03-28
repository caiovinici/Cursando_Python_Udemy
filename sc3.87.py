"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz'] # *resto = trás uma lista vazia
print(nome) # desempacotando Luiz

#  SC  3  . 88 
"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Bruno', 'Adriana', 'Paulo', 'Caio')
nomes2 = tuple(nomes) # converte em tuplas
nomes3 = list(nomes) # converte para lista
print(nomes[-1])
print(nomes)
print('\nConvertido em Tuplas: ', nomes2)
print('\nConvertido em lista : ', nomes3)

#  SC  3  . 89 
"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
#
for indice, nome in enumerate(lista, start=1): # enumerate() facilita o acesso aos índices dos elementos em uma sequência.
    # start= aonde começar 
    print(indice, nome, lista[indice])
#     # \t = tab 


