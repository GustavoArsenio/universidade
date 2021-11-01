import logging

logger = logging.getLogger()

class Interface():
    def __init__(self,socket,BUFFER_SIZE):
        self.socket = socket
        self.BUFFER_SIZE = BUFFER_SIZE
        self.OPERATION_SELECTOR = {
            '1':self.add_op,
            '2':self.remove_op,
            '3':self.consult_op
        }
        self.method = ''
        self.data   = ''
    
    def enviar_req(self):
        request = {'method': self.method, 'data':self.data} 
        logger.info(f' Requisicao : {request}')
        self.socket.send( str( request ).encode('utf-8') )
        data = self.socket.recv(self.BUFFER_SIZE).decode('utf-8')
        logger.info(f' Resposta: {data}')

    def add_op(self):
        data = {}

        data['nome']     = input(' Digite o Nome:')
        data['cpf']      = input(' Digite o CPF:')
        data['endereco'] = input(' Digite o Endereço:')

        self.data   = data
        self.method = 'add'

    def remove_op(self):
        nome = input(' Digite o Nome:')
        self.data   = nome
        self.method = 'remove'

    def consult_op(self):
        nome = input(' Digite o Nome:')
        self.data   = nome
        self.method = 'read'

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