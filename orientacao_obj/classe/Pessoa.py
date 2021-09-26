from datetime import datetime

class Pessoa():
    def __init__(self,nome,altura,anoDeNascimento,sexo):
        self.nome=nome
        self.altura=altura
        self.anoDeNascimento=anoDeNascimento
        self.sexo=sexo
    
    def setNome(self,Nome):
        self.nome=Nome
    def getNome(self):
        return self.nome

    def setAnoDeNascimento(self,AnoDeNascimento):
        self.anoDeNascimento=AnoDeNascimento
    def getAnoDeNascimento(self):
        return self.anoDeNascimento

    def setAltura(self,Altura):
        self.altura=Altura
    def getAltura(self):
        return self.altura

    def setSexo(self,Sexo):
        self.sexo=Sexo

    def getSexo(self):
        return self.sexo

    def imprimirNome(self):
        print('Nome: {}'.format(self.nome))
        return self.nome

    def calcularIdade(self):
        return datetime.now().year - int(self.anoDeNascimento)
    
    def __str__(self):
        return f"""
                Nome            : {self.nome}
                Altura          : {self.altura}
                AnoDeNascimento : {self.anoDeNascimento}
                Sexo            : {self.sexo}
                Idade           : {self.calcularIdade()}
                """

class Estudante(Pessoa):
    pass

if __name__ == '__main__':
    p = Pessoa('Gu',1.83,1999,'sim')
    print(p)