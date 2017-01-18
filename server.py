import socket
import sys
 
host = socket.gethostbyname(socket.gethostname())
port = 8888
 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)
 
conn, addr = serverSocket.accept()
sys.stdout.write('Connected by: {}'.format(addr))
sys.stdout.flush()
data = conn.recv(999999999)
sys.stdout.write("Creating password.db...")
sys.stdout.flush()
filesave = open("passwords.db", "wb")
sys.stdout.write("Writing data...")
sys.stdout.flush()
filesave.write(data)
serverSocket.close()
