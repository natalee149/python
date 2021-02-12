import sqlite3 
conn = sqlite3.connect(r"D:\natalee_python\example.db")
c = conn.cursor()
c.execute('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
fname varchar(30) NOT NULL,
lName varchar(30) NOT NULL,
email varchar(100) NOT NULL)''')
conn.commit()
conn.close()
