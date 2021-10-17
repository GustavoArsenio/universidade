from animal import Animal

class Ave(Animal):
    def __init__(self,nome):
        super().__init__(nome)
        self.nome = nome
    
    def falar(self,texto=''):
        print(f"Ave {self.nome} diz: {texto}")

class Mamifero(Animal):
    def __init__(self,nome,velocidade):
        super().__init__(nome)
    
    def correr(self):
        print(f' *** Mamifero {self.nome} está correndo *** ')

if __name__ == '__main__':
    ave      = Ave('Animal Ave')
    ave.imprime()
    ave.falar(' Olá mundo ')

    mamifero = Mamifero('Animal Mamifero',12)
    mamifero.imprime()
    mamifero.correr()