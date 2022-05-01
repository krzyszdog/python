import socket

HOST = "127.0.0.1"
PORT = 6666

s = socket.socket()
s.connect((HOST, PORT))

server_message = s.recv(2048).decode()
print(f"Message from server: {server_message}")

while True:
    try:
        message = input("Send command: ")
        if message.lower() == "exit":
            s.send(message.encode())
            s.close()
            break
        else:
            s.send(message.encode())
            res = s.recv(2048).decode()
            if res.lower() == "exit":
                print(f"Server closed the connection")
                s.close()
                break
            else:
                print(f"Received: {res}")
    except Exception as e:
        print(e)