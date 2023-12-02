import sqlite3 as sql
import random



def get_word(data : str) ->list:
    con = sql.connect('C:\\Users\\Mikayel\\PycharmProjects\\My-Bots\\core\\bases\\english_base.db')
    cur = con.cursor()

    cur.execute(f'''
            SELECT MAX(rowid) FROM {data} 
    ''')
    max_id = cur.fetchone()[0]
    random_number = random.randint(1, max_id)

    cur.execute(f'''
        SELECT english_word,armenian_word FROM {data} WHERE rowid= {random_number}
    ''')
    result = cur.fetchone()
    e_word = result[0]
    a_word = result[1]


    cur.close()
    con.close()

    return [e_word,a_word]
