# Introdução ao  for / in 
texto = 'Familia é tudo'
novo_texto = ''
#
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print('\nnovo_texto', novo_texto)  

# SC  3 . 73 = range + for 
"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 101) # range(inicio,parar,contar ex = 2 em 2)
# ranger(0,100) vai contar até 99, sempe acrescer +1 do desejado para paracer na contagem
for numero in numeros:
    print(numero)


