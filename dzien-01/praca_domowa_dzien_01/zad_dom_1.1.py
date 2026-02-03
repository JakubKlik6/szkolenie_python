import sqlite3
from pathlib import Path
from datetime import datetime
import pandas as pd

# sciezka do bazy
db_path = Path(__file__).parent.parent / "ergo_hestia.db"

# sciezka do zapisu pliku
file_path = '/Users/jakubklik/PycharmProjects/iSA-pythonzaawansowany-ErgoHestia/dzien-01/praca_domowa_dzien_01'

def wyszukaj_polisy_zaawansowane(
        baza_danych,
        typ = None,
        min_wartosc = None,
        max_wartosc = None,
        data_od = None,
        data_do = None,
        klient_nazwisko = None
):

    with sqlite3.connect(baza_danych) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        zapytanie = "SELECT p.*,k.* FROM polisy p join klienci k on p.klient_id = k.id where 1 = 1"

        parameters = []

        if typ:
            zapytanie += " AND p.typ = ?"
            parameters.append(typ)

        if min_wartosc:
            zapytanie += " AND p.wartosc >= ?"
            parameters.append(min_wartosc)

        if max_wartosc:
            zapytanie += " AND p.wartosc =< ?"
            parameters.append(max_wartosc)

        if data_od:
            zapytanie += " AND p.data_od => ?"
            parameters.append(data_od)

        if data_do:
            zapytanie += " AND p.data_do =< ?"
            parameters.append(data_do)

        if klient_nazwisko:
            zapytanie += " AND k.nazwisko = ?"
            parameters.append(klient_nazwisko)

    cur.execute(zapytanie, parameters)
    results = cur.fetchall()
    return [dict(row) for row in results]

def raport_miesieczny(
        baza_danych,
        rok = None
):
    if rok is None:
        rok = datetime.now().strftime("%Y")

    with sqlite3.connect(baza_danych) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(
            '''
                SELECT strftime('%m',data_od) as miesiac, 
                           CASE strftime('%m', data_od)
                            WHEN '01' THEN 'styczen'
                            WHEN '02' THEN 'luty'
                            WHEN '03' THEN 'marzec'
                            WHEN '04' THEN 'kwiecien'
                            WHEN '05' THEN 'maj'
                            WHEN '06' THEN 'czerwiec'
                            WHEN '07' THEN 'lipiec'
                            WHEN '08' THEN 'sierpien'
                            WHEN '09' THEN 'wrzesien'
                            WHEN '10' THEN 'pazdziernik'
                            WHEN '11' THEN 'listopad'
                            WHEN '12' THEN 'grudzien'
                           END AS nazwa,
                       count(numer) as liczba , 
                       sum(wartosc) as suma
                FROM polisy
                where strftime('%Y', data_od) = ?
                GROUP BY strftime('%m',data_od)
                '''
            , (str(rok),))

        return [dict(row) for row in cur.fetchall()]

def eksportuj_do_csv(dane, sciezka, kolumny=None):
    df = pd.DataFrame(dane)
    if kolumny:
        df = df[kolumny]

    df.to_csv(sciezka + '/dane.csv', index=False)
    row_number = len(df)
    return "liczba rekordow " + str(row_number)

# Wyszukaj polisy OC powyżej 400 PLN
wyniki = wyszukaj_polisy_zaawansowane(
    db_path,
    typ='OC',
    min_wartosc=400,
    klient_nazwisko='Kowalski'
)
print(f"Znaleziono {len(wyniki)} polis")

# Wygeneruj raport miesięczny
raport = raport_miesieczny(db_path, rok=2024)
for m in raport:
    print(f"{m['nazwa']}: {m['liczba']} polis, suma: {m['suma']} PLN")

# Eksportuj do CSV
eksportuj_do_csv(wyniki, file_path)
