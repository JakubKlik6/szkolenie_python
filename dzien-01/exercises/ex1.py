"""
Zadanie 1: Połączenie z bazą i pobranie danych
Poziom trudności: ⭐ Czas: 10 minut

Opis
Napisz skrypt, który połączy się z bazą SQLite i pobierze wszystkich klientów.

Wymagania
Użyj context managera (with) do zarządzania połączeniem
Pobierz wszystkie rekordy z tabeli klienci
Wyświetl dane w czytelnej formie
Szablon"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'ergo_hestia.db'

def pobierz_klientow(dir_path):
    """
    Pobiera wszystkich klientów z bazy danych.

    Args:
        sciezka_bazy: ścieżka do pliku bazy SQLite

    Returns:
        Lista krotek z danymi klientów
    """

    with sqlite3.connect(dir_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM klienci")
        results = cursor.fetchall()
        return results

# Test
if __name__ == "__main__":
    klienci = pobierz_klientow(DB_PATH)
    for klient in klienci:
        print(klient)

