#!/usr/bin/env python3

from pathlib import Path
import sqlite3

if __name__ == '__main__':
    workdir = Path(__file__).parent
    # Create a new database connection
    con = sqlite3.connect(workdir / 'tutorial.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
    cur.execute('INSERT INTO user (name, age) VALUES (?, ?)', ('Alice', 30))
    cur.execute('INSERT INTO user (name, age) VALUES (?, ?)', ('Bob', 25))
    cur.execute('INSERT INTO user (name, age) VALUES (?, ?)', ('Charlie', 35))
    con.commit()  # Save (commit) the changes

    # Query the database
    cur.execute('SELECT name, age FROM user WHERE age >= 30')
    rows = cur.fetchall()
    for row in rows:
        print('Name: {}, Age: {}'.format(row[0], row[1]))

    # Close the connection
    con.close()

    # Clean up the database file after execution
    (workdir / 'tutorial.db').unlink()
