import logging

logger = logging.getLogger()

class Request():
    def __init__(self,method,data):
        self.data   = data
        self.method = method
    
    def json_format(self):
        return {'data':self.data, 'method':self.method}

class Interface():
    def __init__(self,socket):
        self.socket = socket
        self.OPERATION_SELECTOR = {
            '1':self.add_op,
            '2':self.remove_op,
            '3':self.consult_op
        }
        self.method = ''
        self.data   = ''
    
    def enviar_req(self):
        self.socket.send( str( {'method': self.method, 'data':self.data} ).encode('utf-8') )

    def add_op(self):
        data = {}

        data['nome']     = input(' Digite o Nome:')
        data['cpf']      = input(' Digite o CPF:')
        data['endereco'] = input(' Digite o Endereço:')

        self.data   = data
        self.method = 'add'
        pass

    def remove_op(self):
        nome = input(' Digite o Nome:')
        self.data   = nome
        self.method = 'remove'
        pass

    def consult_op(self):
        nome = input(' Digite o Nome:')
        self.data   = nome
        self.method = 'read'
        pass

    def render_op(self):
        return'''
           # ======================== #
           # 1) Adcionar funcionario  #
           # 2) Remover Funcionario   #
           # 3) Consultar Funcionario #
           # 4) Exit                  #
           # ======================== #\n'''
    
    def run_UI(self):
        logger.debug(' Startando UI ')
        while True: 
            logger.info(' Inicio UI')
            STOP_PROCESS = self.OPERATION_SELECTOR.get(input(self.render_op()),lambda :True)()
            if STOP_PROCESS == True:
                break
            
            self.enviar_req()

if __name__ == '__main__':    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s [%(module)s:%(lineno)s] : %(message)s'
    )