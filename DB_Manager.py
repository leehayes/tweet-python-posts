"""
Manage the CRUD functionality for the database
"""

import sqlite3


class DB:
    def __init__(self):
        # Create a database in RAM
        conn = sqlite3.connect('Posts.db')
        #Create table if necessary.....

        conn.execute('''CREATE TABLE if not exists  Posts
                 (ID INT PRIMARY KEY     NOT NULL,
                 URL            TEXT    NOT NULL,
                 Title          TEXT    NOT NULL);''')
        conn.close()
