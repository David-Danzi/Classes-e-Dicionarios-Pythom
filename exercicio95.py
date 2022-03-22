time = list()
dic = dict()
list_gol = []

while True:
    dic.clear()
    dic['nome'] = input(f'Nome do jogador: ')
    n_jogos = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    list_gol.clear()
    for i in range(n_jogos):
        list_gol.append(int(input(f'Quantos gols na partida {i}? ')))
    dic['gols'] = list_gol[:]
    dic['total'] = sum(list_gol)
    time.append(dic.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper() [0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print()
print('-' * 30)   
for k, v in enumerate(time):
    print(f'{k:>4} ', end= '')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()   
print("-" * 30)
