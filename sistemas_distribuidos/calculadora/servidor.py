# Disponibilizado também em: https://github.com/GustavoArsenio/universidade/tree/main/sistemas_distribuidos/calculadora
# Author : Gustavo Arsenio de Sousa
# Data : 26/09/2021

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9998
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    resultado = eval(data)
    conn.send(resultado.__str__().encode('utf-8'))
conn.close()