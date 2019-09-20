import socket

_socket =socket.socket()
_socket.connect(("localhost",1998))
request=''
while request!='exit':
    request =input("Ingrese un nuevo comando: \n")
    _socket.send(request.encode())
    ans=_socket.recv(1024)
    print(ans.decode())
_socket.close()
