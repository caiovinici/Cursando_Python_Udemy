"""
Interpretador do Python
#
python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)
#
The Zen of Python, por Tim Peters
#
Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""
# SC  3  .  96
'''Desempacotando em chamadas de métodos
e funções()'''
string = 'ABC'
lista = ['Caio', 'Bruno', 1,2,3, 'Paulo']
tuplas = 'Python', 'é', 'legal'
salas = [
    # 0       1
    ['Caio', 'Adriana',], # lista 0
    # 0
    ['Bruno',], # lista 1
    # 0       1          2
    ['Paulo','Adriana', 'Bruno',], # lista 2
]
#
# a, d, *_, ap, k = lista
# print(d,a,ap)
#   
print('Caio', 'Bruno', 1,2,3, 'Paulo')
print('1', *lista, '-', lista)
print('2', *string, '-', string)
print('3', *tuplas, '-', tuplas)
#
print('4', *salas, sep='\n') # sep='' - 

#  SC  3  .  97
"""
Operação ternária (condicional de uma linha)
<valor> se <condição> senão <outro valor>
"""
condição = 10 == 11
variavel = 'Valor' if condição else 'Outro valor'
print(variavel)
digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')
