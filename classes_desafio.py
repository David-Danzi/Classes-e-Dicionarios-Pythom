#DESAFIO 
'''pedir para o dono o preço e o estoque das laranjas.
pedir o tipo e quantidade de laranjas que o cliente quer.
verificar se tem estoque e calcular o praço do produto .
calcular valor (preco kg * total quilos)
1 Laranja pera = 250 g
2 Laranja Lima = 200g'''
import os

class laranja:
    def __init__(self):       
        self.estoque_lima = 0
        self.estoque_pera = 0
        self.precokg_pera = 0
        self.precokg_lima = 0 
        self.tipo = ''
        self.preco_pera = ''
        self.preco_lima = ''
        self.unidades_pera = 0  
        self.unidades_lima = 0
        self.precokg_pera = ''
        self.precokg_lima = ''
        self.preco_total = 0

    def perguntar_dono(self):
        self.estoque_lima = int(input("Quantas unidades de Laranja lima há no estoque? "))
        self.estoque_pera = int(input("Quantas unidades de Laranja Pera há no estoque? "))
        self.precokg_pera = float(input("Qual o Preço do quilo de Laranja pera? "))
        self.precokg_lima = float(input("Qual o preco do quilo da Laranja lima? "))

    def perguntar_cliente(self):
        print('Obrigado pela preferência!')
        print('-'*30)
        print('Temos laranja pera e lima!')
        print(f'O preço/Kg da laranja lima é {self.precokg_lima:>00} R$ e cada unidade pesa 200g')
        print(f'O preço/Kg da laranja pera é {self.precokg_pera:>00} R$ e cada unidade pesa 250g')
        self.tipo = int(input('Digite 1 se for comprar laranja pera ou 2 se for comprar laranja Lima ou 3 se for os dois: '))
        if self.tipo != 1 and self.tipo != 2 and self.tipo != 3:
            self.tipo = int(input('Erro!, digite 1, 2 ou 3 por favor. '))
        if self.tipo == 1:
            self.unidades_pera = int(input('Digite a quantidade que quer comprar: '))
        elif self.tipo == 2:
            self.unidades_lima = int(input('Digite a quantidade que quer comprar: '))
        else:
            self.unidades_pera = int(input('Digite a quantidade de laranja pera que quer comprar: '))
            self.unidades_lima = int(input('Digite a quantidade de laranja lima que quer comprar: '))
        print()

    def verificar_estoque(self):
        if self.tipo == 1:
            if self.estoque_lima >= self.unidades_lima: 
                print('O estoque possui unidades suficientes de laranja pera.')
            else:
                print("Que pena! O estoque acabou")
        if self.tipo == 2:
            if self.estoque_pera >= self.estoque_pera:
                print('O estoque possui unidades suficientes de laranja lima.')
            else:
                print("Que pena! O estoque acabou")
        if self.tipo == 3:
            if self.estoque_pera >= self.estoque_pera and self.estoque_lima >= self.unidades_lima:
                print('O estoque possui unidades suficientes de ambos.')
            else:
                print("Que pena! O estoque acabou")
        print()

    def calcular_preco(self):
        if self.tipo == 1:
            self.preco_pera = (self.unidades_pera/4) * self.precokg_pera
            print(f'O valor a ser pago é: {self.preco_pera}, Muito obrigado! Volte sempre!')
        if self.tipo == 2:
            self.preco_lima = (self.unidades_lima/5) * self.precokg_lima
            print(f'O valor a ser pago é: {self.preco_lima}, Muito obrigado! Volte sempre!')
        if self.tipo == 3:
            self.preco_lima = (self.unidades_lima/5) * self.precokg_lima
            self.preco_pera = (self.unidades_pera/4) * self.precokg_pera
            self.preco_total = self.preco_lima + self.preco_total
            print(f'O valor a ser pago é: {self.preco_total}, Muito obrigado! Volte sempre!')

def comecar_programa():
    print('-'*30)
    print('Olá, Sejá bem vindo ao programa!')
    print('-'*30)
    print("Olá Vendedor!")
    procedimento = laranja()  
    procedimento.perguntar_dono()
    os.system("cls")
    print('-'*30) 
    print("Olá Cliente!")
    procedimento.perguntar_cliente()
    procedimento.verificar_estoque()
    procedimento.calcular_preco()

comecar_programa()