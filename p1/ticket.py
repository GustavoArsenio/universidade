class Ticket():
    def __init__(self, valor,valorAdicional):
        self.valor = valor
        self.valorAdicional = valorAdicional

    def imprimeValor(self):
        print(f' Valor: {self.valor}')

class Teste():

    def imprimeValor(self):
        print('cu')

class VIP(Ticket,Teste):
    def getValorTicket(self):
        return self.valor + self.valorAdicional

    def setValorAdicional(self, valorAdicional):
        self.valorAdicional = valorAdicional

if __name__ == '__main__':
    teste_vip = VIP(2,3)
    teste_vip.imprimeValor()
    print(teste_vip.getValorTicket())