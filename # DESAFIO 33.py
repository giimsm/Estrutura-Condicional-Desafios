# DESAFIO 33
# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor.
num=int(input('Digite o primeiro numero'))
num1=int(input('Digite o segundo numero'))
num2=int(input('Digite o terceiro numero'))
maiornumero=num
menornumero=float('inf')
if num1 > maiornumero:
    maiornumero= num1
if num2 > maiornumero:
    maiornumero= num2
if num < menornumero:
    menornumero = num
if num1 < menornumero:
    menornumero= num1
if num2 < menornumero:
    menornumero= num2
print('O maior numero digitado foi: ', maiornumero)
print('O menor numero digitado foi: ', menornumero)