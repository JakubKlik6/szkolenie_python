"""
Zadanie 2: Wyszukiwanie polis po kryteriach
Poziom trudności:  Czas: 15 minut
Opis
Napisz funkcję wyszukującą polisy według typu i minimalnej wartości. Funkcja powinna zwracać wyniki jako listę słowników.
Wymagania
Użyj parametryzacji zapytań (ochrona przed SQL Injection)
Dynamicznie buduj zapytanie w zależności od podanych kryteriów
Zwróć wyniki jako listę słowników (użyj row_factory)Obsłuż przypadek, gdy żaden parametr nie jest podanySzablon"""

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / 'ergo_hestia.db'


def wyszukaj_polisy(sciezka_bazy, typ_polisy=None, min_wartosc=None):
    """
    Wyszukuje polisy według podanych kryteriów.

    Args:
        sciezka_bazy: ścieżka do pliku bazy SQLite
        typ_polisy: typ polisy (np. 'OC', 'AC', 'DOM') - opcjonalny
        min_wartosc: minimalna wartość polisy - opcjonalna

    Returns:
        Lista słowników z danymi polis
    """
    with sqlite3.connect(sciezka_bazy) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = "SELECT * FROM polisy WHERE 1=1"

        parameters = []

        if typ_polisy:
            query += " AND typ = ?"
            parameters.append(typ_polisy)

        if min_wartosc:
            query += " AND wartosc >= ?"
            parameters.append(min_wartosc)

        cursor.execute(query, parameters)
        results = cursor.fetchall()
        return [dict(row) for row in results]

# Test
if __name__ == "__main__":
    # Test 1: Tylko typ
    polisy_oc = wyszukaj_polisy(DB_PATH, typ_polisy='OC')
    print(f"Polisy OC: {len(polisy_oc)}")
    #
    # Test 2: Typ i minimalna wartość
    polisy_drogie = wyszukaj_polisy(DB_PATH, typ_polisy='AC', min_wartosc=1000)
    print(f"Polisy AC > 1000: {len(polisy_drogie)}")

    # Test 3: Wszystkie polisy
    wszystkie = wyszukaj_polisy(DB_PATH)
    print(f"Wszystkie polisy: {len(wszystkie)}")