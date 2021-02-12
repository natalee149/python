import sqlite3
conn = sqlite3.connect(r"D:\natalee_python\example.db")
c = conn.cursor()
c.execute('''INSERT INTO users (id,fname,lname,email) VALUES (NULL,"natalee","na","A")''')
c.execute('''INSERT INTO users VALUES (NULL,"Banana","Black","Blach")''')
conn.commit()
conn.close()