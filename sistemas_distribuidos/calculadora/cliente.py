import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 9998
BUFFER_SIZE = 4096


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print("**** Bem vindo a calculadora ***")
MESSAGE = input(" Por gentileza informe a formula para calcular: ")

s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)

print(f"""\n\n\t >>>>> {MESSAGE} = {data.decode('utf-8')} \n\n""")
s.close()
print(f"****    Fim a calculadora    ***")