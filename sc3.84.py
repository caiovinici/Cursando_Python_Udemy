"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Caio', 171, 'Janeiro', 2024]
lista_b = lista_a.copy() # copia a lista
#
lista_a[0] = 'Qualquer coisa' # adc item no índice desejado
print(lista_a)
print(lista_b) # lista_a copiado em variavel lsita_b

# tento duas listas 'iguais' cm valores diferentes

#  SC  3  . 85 
"""
for in com listas
"""
lista_c = ['Dry', 'Ice', 'Haxixe', 'Flor']
#
for nome in lista_c:
    print(nome)

#  SC  3 . 86 
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista_nome = ['Adriana', 'Paulo', 'Bruno']
lista_nome.append('Caio')

indices = range(len(lista_nome))

for i in indices:
    print(i, lista_nome[i])
