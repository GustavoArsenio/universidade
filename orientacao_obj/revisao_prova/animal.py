from abc import ABCMeta, abstractmethod

class Animal():
    def __init__(self,nome):
        print('Construtor Aniaml')
        super().__init__()
        self.nome = nome
    
    def imprime(self):
        print(f' Nome do Animal : {self.getNome()}')

    def getNome(self):
        return self.nome
    
    @abstractmethod
    def falar(self):
        pass

if __name__ == '__main__':
    my_class = Animal('Nome_do_animal')
    my_class.imprime()