#Orientação a objetos
#classes e objetos

##class Veiculo:
##    def moverse(self):
##        print(f'posso me mover')
##
##    def __init__(self,fabricante,modelo):
##        self.fabricante=fabricante
##        self.modelo=modelo
##        self.num_registro=None
##
##if __name__=='__main__':
##    meu_carro=Veiculo('GM','Cadillac Escaled')
##    meu_carro.moverse()
##    print(meu_carro.fabricante)
    
#-----------------------

##class Veiculo:
##    def moverse(self):
##        print(f'posso me mover')
##
##    def __init__(self,fabricante,modelo):
##        self.__fabricante=fabricante #__ é encapsuamento, torna a "variável" privada inacessível externamente de forma direta
##        self.__modelo=modelo
##        self.__num_registro=None
##    #Getter:
##    def get_fabr_modelo(self):
##        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
##    #Setter:
##    def set_num_registro(self, registro):
##        self.__num_registro = registro
##    def get_num_registro(self):
##        return self.__num_registro
##    
##if __name__=='__main__':
##    meu_carro=Veiculo('GM','Cadillac Escaled')
##    meu_carro.moverse()
##    meu_carro.get_fabr_modelo()
##    meu_carro.set_num_registro('a234bc-213')
##    print(f'Registro: {meu_carro.get_num_registro()}\n')

#-----------------------------
#herança:


class Veiculo:
    def moverse(self):
        print(f'sou um veículo')

    def __init__(self,fabricante,modelo):
        self.__fabricante=fabricante #__ é encapsuamento, torna a "variável" privada inacessível externamente de forma direta
        self.__modelo=modelo
        self.__num_registro=None
    #Getter:
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
    #Setter:
    def set_num_registro(self, registro):
        self.__num_registro = registro
    def get_num_registro(self):
        return self.__num_registro

class Carro(Veiculo):
    #metodo __init__ será herdado
    def moverse(self):
        print(f'sou um carro')

class Moto(Veiculo):
    def moverse(self):
        print(f'sou uma moto')

class Aviao(Veiculo):
    def __init__(self,fabricante,modelo,categoria):
        self.__cat=categoria
        super().__init__(fabricante, modelo) #de onde e oq ele vai herdar
    def get_categoria(self):
        return self.__cat        
    
if __name__=='__main__':
    meu_carro=Veiculo('GM','Cadillac Escaled')
    meu_carro.moverse()
    meu_carro.get_fabr_modelo()
    meu_carro.set_num_registro('a234bc-213')
    print(f'Registro: {meu_carro.get_num_registro()}\n')

    meu_carro2=Carro('VW', 'Polo')
    meu_carro2.moverse()
    meu_carro2.get_fabr_modelo()

    mmoto=Moto('Harley-Davidson', 'Nighter Special')
    mmoto.moverse()
    mmoto.get_fabr_modelo()

    meu_aviao=Aviao('Boeing','747','Comercial')
    meu_aviao.moverse()
    meu_aviao.get_fabr_modelo()
    meu_aviao.get_categoria()
    
    
https://youtu.be/-VeVq64Fgw0?t=27333
7:35:33

