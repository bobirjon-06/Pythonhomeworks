import sqlite3

def create_db():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    ""
    )
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    data = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    cur.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def update_year():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984"))
    conn.commit()
    conn.close()

def query_dystopian():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT Title, Author FROM Books WHERE Genre = ?", ("Dystopian",))
    results = cur.fetchall()
    conn.close()
    return results

def delete_old_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Books WHERE Year_Published < ?", (1950,))
    conn.commit()

if __name__ == "__main__":
    create_db()
    insert_data()
    update_year()
    print("Dystopian books:", query_dystopian())
    delete_old_books()
""")