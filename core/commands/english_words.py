import sqlite3 as sql
from core.commands.commands_for_working_with_db import insert_words,clear_table,create_table

con = sql.connect('C:\\Users\\Mikayel\\PycharmProjects\\My-Bots\\core\\bases\\english_base.db')
cur = con.cursor()

cur.execute('''
    SELECT name FROM sqlite_master WHERE type='table'
''')
tables_names = cur.fetchall()
tables_names = [name[0] for name in tables_names]




con.commit()
con.close()