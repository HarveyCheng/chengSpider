from pysqlite2 import dbapi2 as sqlite


conn = sqlite.connect("dmoz.db")
cur = conn.cursor()
cur.execute('select * from dmoz')
rs = cur.fetchall()
print rs
cur.close()
conn.close()

