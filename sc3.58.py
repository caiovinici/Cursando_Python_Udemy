"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000' # strings Imutáveis == sem alteração de valor 
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

print(string.zfill(10)) #zfill == acrescenta números\
#                                 000 a esquerda da strings
