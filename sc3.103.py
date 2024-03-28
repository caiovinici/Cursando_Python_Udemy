print('='* 20)
print('GERADOR DE CPF\'s')
print('='* 20)
#
import random
from time import sleep
#
for _ in range(5):
    nove_digitos = ''
#
    for i in range(9): # gerando digitos aleatorios
        nove_digitos += str(random.randint(0,9))
#
    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    #  
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
#
    dez_digitos = nove_digitos + str(digito)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
# 
    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    #
    gerador_cpf = f'{nove_digitos}{digito_1}{digito_2}'
    #
    print('GERANDO CPF, UM INSTANTE!')
    sleep(2)
    print(f'CPF Gerado {gerador_cpf}')
    print('='* 20)
    #
