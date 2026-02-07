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
    """
    Generuje raport klientów z ich polisami.

    Returns:
        Lista słowników w formacie:
        [
            {
                'client': 'Jan Kowalski',
                'email': 'jan@email.pl',
                'policies': [
                    {'numer': 'POL-001', 'typ': 'OC', 'wartosc': 450.0},
                    {'numer': 'POL-002', 'typ': 'AC', 'wartosc': 1200.0}
                ]
            },
            ...
        ]
    """
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
            SELECT
                k.id as client_id,
                k.imie,
                k.nazwisko,
                k.email,
                p.numer,
                p.typ,
                p.wartosc
            FROM klienci k
            LEFT JOIN polisy p ON k.id = p.klient_id
            ORDER BY k.nazwisko, k.imie, p.numer
        """)

        # Grupowanie wyników
        clients_dict = defaultdict(lambda: {'policies': []})

        for row in cursor.fetchall():
            client_id = row['client_id']
            client_key = client_id

            # Ustaw dane klienta jeśli jeszcze nie ustawione
            if 'client' not in clients_dict[client_key]:
                clients_dict[client_key]['client'] = f"{row['imie']} {row['nazwisko']}"
                clients_dict[client_key]['email'] = row['email']

            # Dodaj polisę jeśli istnieje
            if row['numer']:
                clients_dict[client_key]['policies'].append({
                    'numer': row['numer'],
                    'typ': row['typ'],
                    'wartosc': float(row['wartosc'])  # Konwersja Decimal na float
                })

        return list(clients_dict.values())
    finally:
        conn.close()

# Test
if __name__ == "__main__":
    report = clients_policies_report()
    print(report)
    for client in report:
        print(f"\n{client['client']} ({client['email']}):")
        if client['policies']:
            for policy in client['policies']:
                print(f"  - {policy['numer']}: {policy['typ']} = {policy['wartosc']} PLN")
        else:
            print("  (brak polis)")