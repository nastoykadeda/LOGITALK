from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.setblocking(0)
server_socket.listen(5)

while True:
    try:
        connection, address = server_socket.accept()
        print("Підключився клієнт", address)

        connection.setblocking(0)
        connection.send("Повідомлення від сервера".encode())
        connection.close()

    except:
        pass


