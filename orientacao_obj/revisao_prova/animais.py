from tipos_de_animais import Mamifero, Ave
class BemTeVi(Ave):
    def falar(self):
        print(' Olá eu sou um bem-te-vi')

class Papagaio(Ave):
    def __init__(self,nome,vocabulario=None):
        super().__init__(nome)
        self.vocabulario = vocabulario
    
    def setVocabulario(self,vocabulario):
        self.vocabulario = vocabulario

class Vaca(Mamifero):
    def __init__(self,nome,velocidade,permiteOrdenhar):
        super().__init__(nome,velocidade)
        self.permiteOrdenhar = permiteOrdenhar
    
    def ordenhar(self):
        print(f'{self.nome} : { "Não" if self.permiteOrdenhar else ""} Pode ordenhar Ordenhar')

class Cachorro(Mamifero):
    def __init__(self,nome,velocidade,tipoLatido):
        super().__init__(nome,velocidade)
        self.tipoLatido = tipoLatido
    
    def setLateAlto(self):
        print(f" Cachorro {self.nome} : Late Alto")

    def setLateBaixo(self):
        print(f" Cachorro {self.nome} : Late Baixo")

    def falar(self):
        print(f" Cachorro {self.nome} : Diz olá")

if __name__ == "__main__":
    print('\n\n\n\n Inicializando: bemtevi')
    bemtevi  = BemTeVi('Bem Te Vi')
    bemtevi.falar()
    bemtevi.imprime()
    bemtevi.getNome()

    print('\n\n\n\n Inicializando: papagaio')
    papagaio = Papagaio("Papagaio")
    papagaio.falar()
    papagaio.getNome()
    papagaio.imprime()
    papagaio.setVocabulario('portugues')

    print('\n\n\n\n Inicializando: vaca')
    vaca     = Vaca("Vaca",12,False)
    vaca.getNome()
    vaca.imprime()
    vaca.ordenhar()
    vaca.correr()

    print('\n\n\n\n Inicializando: cachorro')
    cachorro = Cachorro(" Cachorro ",20,'Au Au')
    cachorro.correr()
    cachorro.falar()
    cachorro.getNome()
    cachorro.imprime()
    cachorro.setLateAlto()
    cachorro.setLateBaixo()