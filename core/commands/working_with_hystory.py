import sqlite3 as sql


def making_hystory(item_name : str,user_id : int) -> None:
    con = sql.connect('C:\\Users\\Mikayel\\PycharmProjects\\My-Bots\\core\\bases\\hystory.db')
    cur = con.cursor()

    cur.execute("SELECT id FROM items")
    result_tup = cur.fetchall()
    result_list = [item[0] for item in result_tup]
    if user_id not in result_list:
        cur.execute("INSERT INTO items (id) VALUES (?)",(user_id,))
    cur.execute("SELECT item_name FROM items WHERE id=?",(user_id,))
    items_by_id = cur.fetchone()[0]
    if items_by_id == None:
        items_by_id = ''
    items_by_id = item_name + '|' + items_by_id
    item_list = items_by_id.split("|")
    if len(item_list) > 5:
        items_by_id = "|".join(item_list[:5])
    cur.execute("UPDATE items SET item_name=? WHERE id=?", (items_by_id, user_id))
    con.commit()
    con.close()
def getting_history(user_id : int) -> str:
    con = sql.connect('C:\\Users\\Mikayel\\PycharmProjects\\My-Bots\\core\\bases\\hystory.db')
    cur = con.cursor()

    cur.execute("SELECT item_name FROM items WHERE id=?", (user_id,))
    result = cur.fetchone()
    item_name = result[0] if result else "**"

    con.commit()
    con.close()
    return item_name


def delete_names(user_id : int):
    con = sql.connect('C:\\Users\\Mikayel\\PycharmProjects\\My-Bots\\core\\bases\\hystory.db')
    cur = con.cursor()

    cur.execute("DELETE FROM items WHERE id = ?", (user_id,))

    con.commit()
    con.close()
