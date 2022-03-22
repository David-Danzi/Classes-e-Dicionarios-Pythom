import json
#pesquisar quatro parametros para barometros além do id 

def inserir_barometro(barometro): # pessoa, id, nome , altura, peso
    #abrir o arquivo para leitura(open, 'r')
    arquivo = open("trabalho.json", 'r')
    # utilizar o json.load para carregar os dados para lista
    lista_dic = json.load(arquivo)
    #dar append na lista
    lista_dic.append(barometro)
    #abrir arquivo para escrita (open, 'w')
    arquivo = open("trabalho.json", 'w')
    #utilizar o json.dumb para escrever a lista no arquivo
    json.dump(lista_dic, arquivo, indent= True)

def alterar_barometro(barometro):
    dados = barometro
    arquivo = open("trabalho.json", 'r')
    lista_dic = json.load(arquivo)
    arquivo = open("trabalho.json", 'w')
    try:
        for i in lista_dic:
            if lista_dic[id] == i:
                if lista_dic[i] != dados[i]:
                    lista_dic[i].update(barometro[i])
    except Exception as erro:
        print(f'O erro foi: {erro.__cause__}')
    json.dump(lista_dic, indent= True)


opcao = 1
while (opcao != 0):
    print('SISTEMA DE CADASTRO DE PESSOAS')
    print('1- Inserir barometro')
    print('2 - Alterar barometro')
    opcao = int(input("Digite sua opção: "))

    if (opcao == 1):
        # ler dados e armazenar em um 'dicionario'
        id = int(input("Digite o id: "))
        material = input("Digite o material usado na produção: ")
        origem = input("Digite a origem do produto: ")
        peso = int(input("Digite o peso em gramas: "))
        quantidade = int(input(f'Digite a quantidade: '))
        
        dicionario = {"id":id, "material":material, "origem": origem,
         "peso": peso, "quantidade": quantidade}
        inserir_barometro(dicionario)

    if (opcao == 2):
        id = int(input("Digite o id: "))
        material = input("Digite o material usado na produção: ")
        origem = input("Digite a origem do produto: ")
        peso = int(input("Digite o peso em gramas: "))
        quantidade = int(input(f'Digite a quantidade: '))
        
        dicionario = {"id":id, "material":material, "origem": origem, 
        "peso": peso, "quantidade": quantidade}
        alterar_barometro(dicionario)