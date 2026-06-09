import sqlite3
import pandas as pd
DB_NAME = "database.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_transactions_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    posting_date TEXT,
                    description TEXT,
                    amount REAL,
                    type TEXT,
                    UNIQUE(posting_date, description, amount, type)
                )
            """)    # UNIQUE(...) to revent duplicate imports when 
                    # the same CSV is processed multiple times

    conn.commit()
    conn.close()

def insert_transactions(df):
    conn = connect_db()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
                    INSERT OR IGNORE INTO transactions (
                       posting_date,
                       description,
                       amount,
                       type
                    )
                    VALUES(?, ?, ?, ?)
            """, (
                row["Posting Date"],
                row["Description"],
                row["Amount"],
                row["Type"]
            ))
    conn.commit()
    conn.close()
    
def get_transaction_count():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
            "SELECT COUNT(*) FROM transactions"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count

def get_all_transactions():
    conn = connect_db()

    # Convert SQLite query results into a DataFrame
    # so existing analytics functions can be reused
    df = pd.read_sql_query("SELECT * FROM transactions", conn)

    conn.close()

    return df
