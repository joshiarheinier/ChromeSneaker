import sqlite3

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()
#Execute SQL syntax
cursor.execute("SELECT url,user,pwd FROM password")

for result in cursor.fetchall():
    print("URL     :"+str(result[0]))
    print("USERNAME:"+str(result[1]))
    print("PASSWORD:"+str(result[2]))
    print("---------------------------------------")
input("Press <Return> to close...")
conn.close()
