dic = dict()
list_gol = []
soma = 0
dic['nome'] = input(f'Nome do jogador: ')
n_jogos = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for i in range(n_jogos):
    list_gol.append(int(input(f'Quantos gols na partida {i}? ')))

dic['gols'] = list_gol
dic['total'] = sum(list_gol)

print("-=" * 35)
print(dic)
print("-=" * 35)

for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print("-=" * 35)

print(f'O jogador {dic["nome"]} jogou {n_jogos} partidas.')
for i in range(len(list_gol)):
	print(f' => Na partida {i}, fez {list_gol[i]} gols.')
