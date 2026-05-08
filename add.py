
import sqlite3

conn = sqlite3.connect("exam.db")
c = conn.cursor()

c.execute("INSERT INTO questions VALUES (1,'Physics','Unit of force?','Newton','Joule','Watt','Pascal','Newton')")
c.execute("INSERT INTO questions VALUES (2,'Physics','Speed formula?','d/t','t/d','m*v','a*t','d/t')")

conn.commit()
conn.close()
c.execute("INSERT INTO questions VALUES (3,'Math','2+2=?','3','4','5','6','4')")
