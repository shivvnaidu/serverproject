import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind((socket.gethostname(), 1347))
sk.listen()
while True:
    client, address = sk.accept()
    print("Connection Established")
    client.send(b"socket programming")
    https: // github.com / shivvnaidu / hclproject.git
