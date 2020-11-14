import socket, pickle
import sys
from time import time
import elgamal
sys.path


def gamald(privateKey):
    for i in range(5):
        for j in range(2):
            aux2 = ('decrypt%s%s.txt' %(i+1,j+1))
            aux1 = ('elgamal%s%s.txt' %(i+1,j+1))
            tiempo_inicial = time() 
            with open(aux1,"r") as f:
                file = open(aux2,"w")
                file.write('INSERT INTO dgamal%s%s'%(i+1,j+1) + ' (decrypt)\n')
                for linea in f.readlines():
                    linea = linea.rstrip("\n")
                    plaintext = elgamal.decrypt(privateKey,linea)
                    file.write('VALUES'+' ("'+plaintext+'"), '+'\n')
                file.close()
            tiempo_final = time() 
            tiempo_ejecucion = tiempo_final - tiempo_inicial
            print(' Duracion Decrypt El Gamal h%s%s' %(i+1,j+1) ,tiempo_ejecucion)         
            
            
keys = elgamal.generate_keys()

privateKey = keys.get('privateKey')
publicKey = keys.get('publicKey')




# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(2048)
            if data:
                print('*** Enviando llave publica ***')
                connection.sendall(pickle.dumps(publicKey))
            data1 = connection.recv(1000)
            if data1:
            	print(data1.decode())
            	gamald(privateKey)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

