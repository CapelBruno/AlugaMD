#Programa para realizar um pedido de aluguel de mídia digital.

import datetime

def linha():
    print('\033[0;30;44m-*\033[m' * 100)


jogos = ['GTA 5', 'FIFA 22', 'HORIZON FORBIDDEN WEST', 'ELDEN RING', 'FARCRY 6', 'ALAN WAKE', 'UFC 4', 'BATTLEFIELD 2042', 'RED DEAD REDEMPTION 2', 'WATCH DOGS LEGION']

linha()
print(f'Nossa biblioteca tem: {jogos}')
linha()
semanal = 20
mensal = 50

while True:         #Verifica se o jogo está disponível ou não.
    escolha = str(input('Qual jogo deseja alugar? ')).upper().strip()  # Escolha de jogo do usuário.
    if escolha in jogos:
        linha()
        print('Jogo disponível! ')
        linha()
        break
    else:
        escolha = str(print('Erro, jogo não encontrado ou indisponível. Tente mais uma vez! '))
print('Oferecemos aluguéis semanais por R$20 e mensais por R$50.')
while True:
    período = str(input('Deseja alugar por que período, semanal ou mensal [S/M]? ')).upper().strip()            #Solicita o tempo que o usuário deseja ficar com a mídia.
    linha()
    if período == 'S':
        hoje = datetime.date.today()
        print(f'Envie um comprovante de pagamento de R${semanal} para @CapelBruno.')
        print(f'O aluguel começará {hoje} e acabará em 7 dias.')
        break
    elif período == 'M':
        hoje = datetime.date.today()
        print(f'Envie um comprovante de pagamento de R${mensal} para @CapelBruno.')
        print(f'O aluguel começa {hoje} e acabará em 31 dias.')
        break
    else:
        print('Tente novamente!')
print('Obrigado pelo pedido!')