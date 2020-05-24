import psycopg2
import sqlite3
import random
from difflib import get_close_matches

# Connect
def connect():
    conn = sqlite3.connect('learned_words.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS learned_words (id INTEGER PRIMARY KEY, word TEXT NOT NULL UNIQUE, author TEXT NOT NULL)")
    conn.commit()
    conn.close()

# Add a word into the learned database
def insert(word, definition):
    conn = sqlite3.connect('learned_words.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO learned_words VALUES(NULL, ?,?)", (word, definition))
    conn.commit()
    conn.close()

# View all learned words
def view():
    conn = sqlite3.connect('learned_words.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM learned_words")
    rows=cur.fetchall()
    conn.close()
    return rows

# Delete a word from learned
def delete(id):
    conn = sqlite3.connect('learned_words.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM learned_words WHERE id=?", (id, ))
    conn.commit()
    conn.close()

# Search for a word -> from the dictionary database
def search(word = ""):
    conn = sqlite3.connect("dictionary.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary WHERE word = ?", (word,))
    rows=cur.fetchall()
    conn.close()
    return rows[0]
    
# Generate a random word & similar words 
def generate_random(database):
    conn = sqlite3.connect('{}.db'.format(database))
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(database))
    rows=cur.fetchall()
    conn.close()
    index_list = list(random.choice(rows))
    return index_list[1]

def word_list(word):
    conn = sqlite3.connect("dictionary.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary")
    rows=cur.fetchall()
    conn.close()
    word_list = list()
    for row in rows:
        word_list.append(row[1])
    return get_close_matches(word, word_list, n = 4)

def get_definition(word_tup):
    definition = random.choice(word_tup[2].split('; '))
    return definition

