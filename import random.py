import random

jogada=input('Selecione uma das opções:\n1-pedra\n2-papel\n3-tesoura')
pc=random.randint(1,3)

if pc == 1:
    print('pedra 👊')
    if jogada =='1' or jogada=='pedra':
        print("Empate")
    elif jogada =='2' or jogada == 'papel':
        print('Jogador venceu')
    else:
        print('O jogador perdeu')
elif pc == 2:
    print('papel ✋')
    if jogada =='2' or jogada=='papel':
        print("Empate")
    elif jogada =='1' or jogada == 'pedra':
        print('Jogador perdeu')
    else:
        print('jogador venceu')
if pc == 3:
    print('tesoura ✌')
    if jogada =='3' or jogada=='tesoura':
        print("Empate")
    elif jogada =='2' or jogada == 'papel':
        print('Jogador perdeu')
    else:
        print('O jogador venceu')

