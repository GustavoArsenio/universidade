from abc import abstractclassmethod

class Funcionario():
    def __init__(self,nome,salario):
        self.nome    = nome
        self.salario = salario

    @abstractclassmethod
    def calcularBonus(self):
        raise NotImplementedError
        pass

    def __str__(self):
        return f""" Nome: {self.nome} - Salario: {self.salario} - Bonus: {self.calcularBonus()} """

class Gerente(Funcionario):    
    def calcularBonus(self):
        return self.salario * 0.5

class Analista(Funcionario):
    def calcularBonus(self):
        return self.salario * 1
        
if __name__ == '__main__':
    
    g1 = Gerente( 'carlos',5200)
    print(g1)
    
    a1 = Analista('jose', 2300)
    print(a1)