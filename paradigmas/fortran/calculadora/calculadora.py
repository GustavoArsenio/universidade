def SOMA(n1,n2):
    return n1 + n2

def SUB(n1,n2):
    return n1 - n2

def MULT(n1,n2):
    return n1 * n2

def DIV(n1,n2):
    return n1 / n2

def QUADRADO(n1):
    return n1 ** 2

def CUBO(n1):
    return n1 ** 3

def RAIZ_QUADRADA(n1):
    return n1 ** (1/2)
    pass

def RAIZ_CUBICA(n1):
    return n1 ** (1/3)
    pass

def LOG(n1):
    from math import log
    return log(n1)

def SAIR():
    import sys
    print(" Saindo do projeto")
    sys.exit(0)


def calculadora(n1,n2=None,function= lambda:'nothing'):
    if n2 is not None:
        value = function(n1,n2)
    else:
        value = function(n1)
    print(f" O Resultado é : {value}")
    return value


if __name__ == '__main__':
    option = 999
    while option != 0:
        n1 = n2 = None
        operacoes = {
            '1':SOMA,
            '2':SUB,
            '3':MULT,
            '4':DIV,
            '5':QUADRADO,
            '6':CUBO,
            '7':RAIZ_QUADRADA,
            '8':RAIZ_CUBICA,
            '9':LOG,
            '0':SAIR
        }

        print('┌-------------------------------┐')
        print('| 1 - SOMA                      |')
        print('| 2 - SUBTRAÇÃO                 |')
        print('| 3 - MULTIPLICAÇÃO             |')
        print('| 4 - DIVISÃO                   |')
        print('| 5 - ELEVAR NUMERO AO QUADRADO |')
        print('| 6 - ELEVAR NUMERO AO CUBO     |')
        print('| 7 - RAIZ QUADRADA             |')
        print('| 8 - RAIZ CÚBICA               |')
        print('| 9 - LOGARITMO                 |')
        print('| 0 - SAIR                      |')
        print('└-------------------------------┘')  
        option = input(' Seleciona a opção a cima : ')
        if option == '0':
            SAIR()
        n1     = int(input('     Digite o N1: ') )
        if int(option) < 5:
            n2     = int(input('     Digite o N2: ') )
        
        calculadora(n1=n1,n2=n2,function=operacoes.get(option,' Opção não encontrada'))
