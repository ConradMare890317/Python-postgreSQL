import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries_mare_masters (content TEXT, date TEXT);")


def add_entry (entry_content,entry_date):
    with connection:
        connection.execute("INSERT INTO entries_mare_masters VALUES ('This is some test content.', '2021-04-02');")

def get_entries ():
    return entries