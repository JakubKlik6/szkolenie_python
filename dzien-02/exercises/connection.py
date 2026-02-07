import psycopg2

if __name__ =="__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="ergo_hestia",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM klienci")
    print(f"Liczba klientów: {cursor.fetchone()[0]}")
    conn.close()