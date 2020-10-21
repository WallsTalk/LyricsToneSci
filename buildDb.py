import sqlite3

conn = sqlite3.connect('songs.db')


c = conn.cursor()
c.execute('''CREATE TABLE artists_X (id INTEGER PRIMARY KEY AUTOINCREMENT, author VARCHAR, song VARCHAR, lyrics TEXT)''')
conn.commit()
conn.close()
