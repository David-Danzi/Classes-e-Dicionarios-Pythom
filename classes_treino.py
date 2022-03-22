#Sytaxe

#marca, memoria Ram, HD, placa de vídeo
class computador:
    def __init__(self, marca, memoria_ram, disco_rigido,  placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.disco_rigido = disco_rigido
        self.placa_video = placa_video 

    def ligar(self):
        print('Ligando ...')

    def desligar (self):
        print('Desligando ...') 

    def Exibir_informcoes_computador(self):
        print(self.marca, self.memoria_ram, self.disco_rigido, self.placa_video)

comput1 = computador('Asus', '8gb','WD', 'Nvigea')

comput1.ligar()
comput1.Exibir_informcoes_computador()
comput1.desligar()