# Disponibilizado também em: https://github.com/GustavoArsenio/universidade/tree/main/sistemas_distribuidos/Scokets
# Author : Gustavo Arsenio de Sousa
# Data : 26/09/2021

import socket
import logging
from user_interface import Interface

print('Constantes')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s [%(module)s:%(lineno)s] : %(message)s'
)

TCP_IP = '127.0.0.1'
TCP_PORT = 9998
BUFFER_SIZE = 4096 * 1024

MODE = '__runtime__'


print(' Abrindo Socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print(' ** Inicializando processos ')

if MODE == '__runtime__':
    UI = Interface(socket=s,BUFFER_SIZE=BUFFER_SIZE)
    print('running UI')
    UI.run_UI()

if MODE == '__test__':
    operacoes = [
                    { 'method': 'add'    , 'data': {'nome':'Teste','cpf':'111.111.111/11','endereco':' Rua de Teste'} },
                    { 'method': 'read'   , 'data': 'Teste' },
                    { 'method': 'remove' , 'data': 'Teste' }
    ]



    print(" Iniciando testes ")
    for position,MESSAGE in enumerate(operacoes):
        print(f' ( {position} / {len(operacoes)} ) {MESSAGE}')
        s.send(str(MESSAGE).encode('utf-8'))
        data = s.recv(BUFFER_SIZE)

        print(f"""\n\n\t >>>>> ( {position} / {len(operacoes)} ) {MESSAGE} = {data.decode('utf-8')} \n\n""")


s.close()
print(f"*** Fim ***")