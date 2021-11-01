# Disponibilizado também em: https://github.com/GustavoArsenio/universidade/tree/main/sistemas_distribuidos/Sockets
# Author : Gustavo Arsenio de Sousa
# Data : 26/09/2021

import os 
import socket
import logging
import time
import ast

from data_manipulation.data_manipulator import Gerenciador_clientes,Cliente

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s [%(module)s:%(lineno)s] : %(message)s'
)

logger = logging.getLogger()

# ====================== #
# Construindo constantes #
# ====================== #

logger.info('Inicializando Constantes Conexão de Socket')
TCP_IP = '127.0.0.1'
TCP_PORT = 9998
BUFFER_SIZE = 4096

COUNTER_WAIT = 0

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH  = f'{os.path.dirname(LOCAL_PATH)}/data'

# =========================== #
# Abrindo Conexão com Sockets #
# =========================== #
logger.info('Inicializando Conexão de Socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
logger.info('Finalizando configuração de Conexão de Socket')

# ================================= #
# Inicializando serviço de controle #
# ================================= #

logger.info('Levantando meta dados e configurando Processamento ')
gerenciador = Gerenciador_clientes(path_info=DATA_PATH)
gerenciador.load_meta_dados()

logger.info('Aguardando Mensagens ')
s.listen(1)
conn, addr = s.accept()
while True:
    data = conn.recv(BUFFER_SIZE).decode('utf-8')
    if not data: break
    logger.info(f' Recebendo informação: {data}')
    request = ast.literal_eval(data)
    
    OPERACAO      = request['method']
    OPERACAO_INFO = request['data']

    RESPONSE = 'requisicao finalizada'

    if   OPERACAO == 'add':
        gerenciador.add_cliente( Cliente(**OPERACAO_INFO) )
    elif OPERACAO == 'remove':
        gerenciador.remove_cliente(OPERACAO_INFO)
    elif OPERACAO == 'read':
        if gerenciador.clientes_dict.get(OPERACAO_INFO,False) :
            RESPONSE = str(gerenciador.clientes_dict[OPERACAO_INFO].json_format())
        else:
            RESPONSE = 'Cliente não encontrado'

    logger.debug(f' Clientes:  { [ f" {item}: {value}" for item,value in gerenciador.clientes_dict.items()]}')
    conn.send(RESPONSE.encode('utf-8'))

# ========================== #
# Fechando conxeão de Socket #
# ========================== #
conn.close()