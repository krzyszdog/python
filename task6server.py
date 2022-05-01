import socket

HOST = "0.0.0.0"
PORT = 6666

s = socket.socket()

s.bind((HOST, PORT))
s.listen(1)
print(f"[+] Server is listening on address {HOST} and port {PORT}")
conn, addr = s.accept()

print(f"Connection type: {conn} from {addr}")
s.close()