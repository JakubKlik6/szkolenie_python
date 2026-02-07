import psycopg2
from psycopg2.extras import RealDictCursor
from collections import defaultdict

# Konfiguracja połączenia z PostgreSQL
DB_CONFIG = {
    "host": "localhost",
    "database": "ergo_hestia",
    "user": "postgres",
    "password": "postgres"
}

def clients_policies_report():
    query = '''SELECT k.imie, k.nazwisko, p.numer, p.typ, p.wartosc 
                FROM klienci k join polisy p on k.id = p.klient_id order by k.imie'''

    conn = psycopg2.connect(**DB_CONFIG)
    try:
        conn.cursor_factory = RealDictCursor
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        client_dicts = defaultdict(lambda: {'policies' : []})
        for row in results:
            client_name = f"{row['imie']} {row['nazwisko']}"
            email = row['email']
            polisa = {'numer': row['numer'] ,'typ': row['typ'], 'wartosc': row['wartosc']}
            client_dicts['email'] = email
            client_dicts[client_name]['policies'].append(polisa)

    finally:
        conn.close()

    return client_dicts

# Test
if __name__ == "__main__":
    report = clients_policies_report()
    for client in report:
        print(f"\n{client['client']} ({client['email']}):")
        for polisa in client['policies']:
            print(f"  - {polisa['numer']}: {polisa['typ']} = {polisa['wartosc']} PLN")