import socket, os

HOST = "127.0.0.1"
PORT = 6666

s = socket.socket()

s.bind((HOST, PORT))
s.listen(1)
print(f"[+] Server is listening on address {HOST} and port {PORT}")
conn, addr = s.accept()

server_message = "Greetings from server :)"
conn.send(server_message.encode())

while True:
    try:
        client_message = conn.recv(2084).decode()
        print(f"Received from {addr}: {client_message}")
        server_message = input("What's the message from server: ")
        if server_message == "exit" or client_message == "exit":
            print("Server is closing session ...")
            s.close()
            break
        else:
            conn.send(server_message.encode())
    except Exception as error:
        print(error)
