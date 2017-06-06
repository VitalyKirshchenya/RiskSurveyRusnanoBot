import sqlite3

conn = sqlite3.connect('participants.db')
# create table
c = conn.cursor()
c.execute('''CREATE TABLE participants
                (data_set BLOB, ID INTEGER, conditions BLOB, country TEXT, city TEXT, industry TEXT, language TEXT, 
                timezone TEXT, question INTEGER, part INTEGER, q_idle INTEGER, active INTEGER, block INTEGER, 
                pointer INTEGER, maturity_level TEXT)''')

conn.commit()
conn.close()

