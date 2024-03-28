""" while/else """
string = 'ValorQualquer'
i = 0
#
while i < len(string):
    letra = string[i]
#   #
    if letra == ' ':
        break # com break else não será executado
#   #
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

# SC  3 .  71
frase = str(input('Digite frase > '))
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
#
while i < len(frase):
    letra_atual = frase[i]
#
    if letra_atual == ' ':
        i += 1
        continue
#   #
    qtd_atual = frase.count(letra_atual)
#   #
    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
#   #
    i += 1
#
print(
    'A letra que apareceu mais vezes foi '
    f'{letra_apareceu_mais_vezes}'' apareceu '
    f'{qtd_apareceu_mais_vezes}x'
    )
