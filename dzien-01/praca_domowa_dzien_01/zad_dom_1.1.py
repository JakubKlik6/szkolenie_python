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
        zapytanie = "SELECT * FROM polisy where 1 = 1"

        parameters = []

        if typ:
            zapytanie += " AND typ = ?"
            parameters.append(typ)

        if min_wartosc:
            zapytanie += " AND wartosc >= ?"
            parameters.append(min_wartosc)

        if max_wartosc:
            zapytanie += " AND wartosc =< ?"
            parameters.append(max_wartosc)

        if data_od:
            zapytanie += " AND data_od => ?"
            parameters.append(data_od)

        if data_do:
            zapytanie += " AND data_do =< ?"
            parameters.append(data_do)

        if klient_nazwisko:
            zapytanie += " AND klient_nazwisko = ?"
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
                SELECT strftime('%m',data_od) as miesiac, count(numer) as liczba , sum(wartosc) as suma
                FROM polisy
                where strftime('%Y', data_od) = ?
                GROUP BY strftime('%m',data_od)
                '''
            , (str(rok),))
        return [dict(row) for row in cur.fetchall()]

def exp_to_csv(dane, sciezka, kolumny=None):
    df = pd.DataFrame(dane)
    if kolumny:
        df = df[kolumny]

    df.to_csv(sciezka + '/dane.csv', index=False)
    row_number = len(df)
    return "liczba rekordow " + str(row_number)
