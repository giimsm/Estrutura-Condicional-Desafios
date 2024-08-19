# DESAFIO 39
# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade:
#
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou o tempo do alistamento
#
# Seu programa também deverá mostrar o tempo que falta ou
# que passou do prazo.
ano=2024-int(input("Digite o ano de nascimento"))
if ano > 18:
    print(f"já passou {ano-18}ano(s) do alistamento")
elif ano < 18:
    print(f"vai se alistar ao serviço militar em {18-ano} ano(s)")
else:
    print("hora de se alistar")