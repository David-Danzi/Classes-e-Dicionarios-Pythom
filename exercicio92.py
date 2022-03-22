from datetime import datetime
dados = {}
dados['nome'] = input("Nome: ")
dados['data_nas'] = int(input("Data de Nascimento: "))
dados['ctps'] = int(input("Carteira de trabalho (0 caso não tenha): "))
if dados['ctps'] != 0:
    dados['ano_contrato'] = int(input("Ano de contratação: "))
    dados['salario'] = int(input("Digite o salário: "))
    dados['aposentadoria'] = dados['ano_contrato'] - dados['data_nas'] + 35

dados['idade'] = datetime.now().year - dados['data_nas'] 

for k, v in dados.items():
    print(f' -{k} tem o valor {v}')
'''
print(' - Nome tem o valor: ',dados['nome'])
print(' - Idade tem o valor: ',dados['idade'])
print(' - Ctps tem o valor: ',dados['ctps'])
print(' - A contratação foi em: ',dados['ano_contrato'])
print(' - Salário tem o valor: ',dados['salario'])
print(' - Aposentadoria tem o valor: ',dados['aposentadoria'])'''
