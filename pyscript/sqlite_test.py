import sqlite3

db=sqlite3.connect('d:\\test.db3')
# cur =db.cursor()

f = open('schema.sql','r+')

text = f.read()
# print(text)
db.executescript(text)
db.close()
