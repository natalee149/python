import sqlite3
conn = sqlite3.connect(r"D:\natalee_python\example.db")
c = conn.cursor()
c.execute('''SELECT fname,lName FROM users''')
result = c.fetchall()
for x in result :
    print(x)