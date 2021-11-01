# Disponibilizado também em: https://github.com/GustavoArsenio/universidade/tree/main/sistemas_distribuidos/Sockets
# Author : Gustavo Arsenio de Sousa
# Data : 26/09/2021

import os 
import socket
import logging
import ast

from server.src.data_manipulation.data_manipulator import Gerenciador_clientes

# ====================== #
# Construindo constantes #
# ====================== #

TCP_IP = '127.0.0.1'
TCP_PORT = 9998
BUFFER_SIZE = 4096

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH  = f'{os.path.dirname(LOCAL_PATH)}/data'

logging.basicConfig('')

# =========================== #
# Abrindo Conexão com Sockets #
# =========================== #

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

# ================================= #
# Inicializando serviço de controle #
# ================================= #

gerenciador = Gerenciador_clientes()
gerenciador.load_meta_dados()

logger = logging.getLogger()

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    logger.info(f' Recebendo informação: {data}')
    request = ast.literal_eval(data)
    
    OPERACAO      = request['method']
    OPERACAO_INFO = request['data']

    conn.send('Sucesso'.encode('utf-8'))

# ========================== #
# Fechando conxeão de Socket #
# ========================== #
conn.close()