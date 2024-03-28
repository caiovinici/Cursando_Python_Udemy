# Exercicio de programação com if e comparação
#
primeiro_valor = int(input('Digite um número: '))
segundo_valor = int(input('Digite outro número: '))

if primeiro_valor > segundo_valor:
    print(f'\n{primeiro_valor=} é maior do que {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'\n{segundo_valor=} é maior do que {primeiro_valor=}')
else:
    print(f'\nO {primeiro_valor=} e o {segundo_valor=} são iguais ')
print('FIM')     