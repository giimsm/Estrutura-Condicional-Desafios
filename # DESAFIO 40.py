# DESAFIO 40
# Crie um programa que leia duas notas entre 0 a 10 de um aluno
# e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida.
#
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média igual ou superior a 7.0: APROVADO

nota1=float(input("Digite a primeira nota"))
nota2=float(input("Digite a primeira nota"))

media= (nota2+nota1)/2
if media < 5.0:
    print(f"Média baixa, {media}: REPROVADO")
elif media >= 5.0 and media < 6.9:
    print(f"Média, {media}: RECUPERAÇÃO")
else:
    print(f"media alta, {media}: APROVADO")