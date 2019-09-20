import socket
import subprocess
import os
_socket=socket.socket()
_socket.bind(("localhost",1998))

_socket.listen(1)

(client_socket,client_address) = _socket.accept()
print('Conexión establecida: ',client_address)

while True:
    client_input=client_socket.recv(1024).decode()

    if client_input == 'exit':
        print("Conextión",client_address[0],"finalizada.")
        break
    else:
        print(client_input)
        cad=client_input.split(" ")
        if(cad[0]=='cd'):
            try:
                os.chdir(cad[1])
                client_socket.send(os.getcwd().encode())
            except:
                client_socket.send("Directorio no encontrado.")
        else:
            output=subprocess.getoutput(client_input)
            client_socket.send(output.encode())
_socket.close()
client_socket.close()
