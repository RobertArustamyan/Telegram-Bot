import sqlite3 as sql


def create_table(cursor, page_number):
    table_name = f'page_{page_number}'
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            ID INTEGER PRIMARY KEY,
            english_word TEXT,
            armenian_word TEXT
        );
    '''
    cursor.execute(create_table_query)

def clear_table(cursor, table_name):
    delete_query = f'DELETE FROM {table_name};'
    cursor.execute(delete_query)

def insert_words(cursor,page_number,words_pairs):
    table_name = f'page_{page_number}'
    insert_info = f'''
    INSERT INTO {table_name}(english_word,armenian_word)
    VALUES (?,?);
    '''
    for english_word,armenian_word in words_pairs.items():
        cursor.execute(insert_info,(english_word,armenian_word))
