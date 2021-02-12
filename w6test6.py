import sqlite3
conn = sqlite3.connect(r"D:\natalee_python\example.db")
c = conn.cursor()
c.execute(' SELECT * FROM users WHERE fName = "Guido" ') 
result = c.fetchall()
for x in result :
    print(x)


import sqlite3
conn = sqlite3.connect(r"D:\natalee_python\example.db")
c = conn.cursor()
try :
    c.execute(' SELECT * FROM users ORDER BY id DESC ')
    conn.commit ()
    result = c.fetchall()
    for x in result :
        print(x)
    c.close()
except sqlite3.Error as e:
    print (e)
finally :
    if conn :
        conn.close ()

