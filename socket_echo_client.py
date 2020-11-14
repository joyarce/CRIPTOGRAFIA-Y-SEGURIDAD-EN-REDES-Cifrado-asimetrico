import os, hashlib, socket, pickle, elgamal, sys
from time import time
sys.path

# Crack 
'''
os.system("time hashcat -a 3 -m 0 -o out11.txt --outfile-format=2 --potfile-disable --force archivo_1 diccionario_1");
os.system("time hashcat -a 3 -m 0 -o out12.txt --outfile-format=2 --potfile-disable --force archivo_1 diccionario_2");

os.system("time hashcat -a 3 -m 10 -o out21.txt --potfile-disable --force archivo_2 diccionario_1"); 
os.system("time hashcat -a 3 -m 10 -o out22.txt --potfile-disable --force archivo_2 diccionario_2"); 

os.system("time hashcat -a 3 -m 20 -o out31.txt --potfile-disable --force archivo_3 diccionario_1");
os.system("time hashcat -a 3 -m 20 -o out32.txt --potfile-disable --force archivo_3 diccionario_2");

os.system("time hashcat -a 3 -m 1000 -o out41.txt --potfile-disable --force archivo_4 diccionario_1");
os.system("time hashcat -a 3 -m 1000 -o out42.txt --potfile-disable --force archivo_4 diccionario_2");

os.system("time hashcat -a 3 -m 1800 -o out51.txt --potfile-disable --force archivo_5 diccionario_1");
os.system("time hashcat -a 3 -m 1800 -o out52.txt --potfile-disable --force archivo_5 diccionario_2");

'''
def sha256():
    print('Comienzo Hasheo SHA256')
    for i in range(5):
        for j in range(2):
            aux1 = ('out%s%s.txt' %(i+1,j+1))
            aux2 = ('h%s%s.txt' %(i+1,j+1))
            tiempo_inicial = time() 
            with open(aux1,"r") as f:
                file = open(aux2,"w")
                for linea in f.readlines():
                    linea = linea.rstrip("\n")
                    h = hashlib.sha256(linea.encode()).hexdigest()
                    file.write(h+'\n')
                file.close()
                tiempo_final = time() 
                tiempo_ejecucion = tiempo_final - tiempo_inicial
                print(' Duracion Hash(SHA256) Output Arch %s Dicc %s' %(i+1,j+1) ,tiempo_ejecucion)
    print('Hasheo finalizado')

def gamal(publicKey):
    for i in range(5):
        for j in range(2):
            aux1 = ('h%s%s.txt' %(i+1,j+1))
            aux2 = ('elgamal%s%s.txt' %(i+1,j+1))
            tiempo_inicial = time() 
            with open(aux1,"r") as f:
                file = open(aux2,"w")
                for linea in f.readlines():
                    linea = linea.rstrip("\n")
                    cipher = elgamal.encrypt(publicKey,linea)
                    file.write(cipher+'\n')
                    # plaintext = elgamal.decrypt(privateKey, cipher)
                    # print(plaintext)
                file.close()
            tiempo_final = time() 
            tiempo_ejecucion = tiempo_final - tiempo_inicial
            print(' Duracion Encrypt El Gamal Archivo h%s%s' %(i+1,j+1) ,tiempo_ejecucion)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

sha256()

try:
    # Send data
    print('*** Solicitando llave publica ***')
    message = b'Solicitando llave publica ... '
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(2048)
        amount_received += len(data)
        print('Llave recibida {!r}'.format(pickle.loads(data)))
        pk = pickle.loads(data)
        gamal(pk)

    print('*** Encriptado terminado ***')
    message1 = b'*** Encriptado terminado ***'
    sock.sendall(message1)

        
finally:    
    print('closing socket')
    sock.close()			







