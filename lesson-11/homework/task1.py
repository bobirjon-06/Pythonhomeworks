import sqlite3

def create_database():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    ""
    )
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()
    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    cur.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()

def update_name():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()
    cur.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
    conn.commit()
    conn.close()

def query_bajoran():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()
    cur.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    results = cur.fetchall()
    conn.close()
    return results

def delete_old():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Roster WHERE Age > ?", (100,))
    conn.commit()
    conn.close()

def query_sorted():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Roster ORDER BY Age DESC")
    results = cur.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    create_database()
    insert_data()
    update_name()
    print("Bajoran characters:", query_bajoran())
    delete_old()
    print("Sorted characters:", query_sorted())
""")