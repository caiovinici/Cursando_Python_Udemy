"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
#
Ex.:  746.824.890-70 (746824890)
      485.943.748.95 (485943748)
   10  9  8  7  6  5  4  3  2
*  4   8  5  9  4  3  7  4  8
   40 72  40 63 24 15 28 12 16
#   
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
40+72+40+63+24+15+28+12+16 = 310
Multiplicar o resultado anterior por 10
301 * 10 = 3010
310 * 10 = 3100
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
3100 % 11 = 9
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#  SC  3  .  99 = Verificando CPF válidos
print('='* 25)
print('Válidador de CPF\'s')
#
import re
import sys
from time import sleep
#
entrada_cpf = input('Insira seu CPF: ')
print('='* 25)
cpf_recebido = re.sub(
    r'[^0-9]',
    '',
    entrada_cpf
) # re recebendo apenas números s/ sequencias
entra_em_sequencia = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)
if entra_em_sequencia:
    print('Você enviou dados sequenciais.')
    sys.exit() # sys.exit() fecha o programa aut.
#
nove_digitos = cpf_recebido[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0 
#
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
#
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0
#
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1 
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 
#
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
#
print('VERIFICANDO SE CPF É VÁLIDO!')
sleep(2)
if cpf_recebido == cpf_gerado_pelo_calculo:
    print(f'CPF {cpf_recebido} é válido!')
else:
    print(f'CPF {cpf_recebido} INVÁLIDO!')
