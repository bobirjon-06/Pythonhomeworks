import pandas as pd
import sqlite3

def in_join(db_path='chinook.db'):
    conn = sqlite3.connect(db_path)
    query = """
    SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) AS TotalInvoices
    FROM customers
    INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
    GROUP BY customers.CustomerId
    """

    customer_invoice = pd.read_sql_query(query, conn)
    conn.close(   )

    return customer_invoice

def out_join(path='movie.csv'):
    movie_df = pd.read_csv(path)

    df1 = movie_df[['director_name', 'color']].dropna()
    df2 = movie_df[['director_name', 'num_critic_for_reviews']].dropna()

    full_outer_join_df = pd.merge(df1, df2, on="director_name", how="outer")

    return  len(full_outer_join_df)

print(customer_invoice.head())
print(full_outer_join_df)

