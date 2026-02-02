# Praca domowa - Dzień 1

## Zadanie główne: System wyszukiwania polis

**Termin:** Do dnia 03.02.2026 (następne zajęcia)
**Szacowany czas:** 1-2 godziny

---

### Opis

Twoim zadaniem jest stworzenie modułu do zarządzania wyszukiwaniem polis ubezpieczeniowych. Moduł powinien umożliwiać:

1. Wyszukiwanie polis po wielu kryteriach
2. Generowanie raportów statystycznych
3. Eksport wyników do pliku CSV

### Wymagania funkcjonalne

#### 1. Funkcja `wyszukaj_polisy_zaawansowane()`

Zaimplementuj funkcję, która pozwala wyszukiwać polisy po następujących kryteriach (wszystkie opcjonalne):

- `typ` - typ polisy (OC, AC, DOM, ZYCIE)
- `min_wartosc` - minimalna wartość
- `max_wartosc` - maksymalna wartość
- `data_od` - polisy rozpoczynające się po tej dacie
- `data_do` - polisy kończące się przed tą datą
- `klient_nazwisko` - nazwisko klienta (wyszukiwanie częściowe)

```python
def wyszukaj_polisy_zaawansowane(
    sciezka_bazy,
    typ=None,
    min_wartosc=None,
    max_wartosc=None,
    data_od=None,
    data_do=None,
    klient_nazwisko=None
):
    """
    Zaawansowane wyszukiwanie polis.

    Args:
        sciezka_bazy: ścieżka do bazy SQLite
        typ: typ polisy
        min_wartosc: minimalna wartość polisy
        max_wartosc: maksymalna wartość polisy
        data_od: data początkowa (format: 'YYYY-MM-DD')
        data_do: data końcowa (format: 'YYYY-MM-DD')
        klient_nazwisko: część nazwiska klienta

    Returns:
        Lista słowników z polisami i danymi klienta
    """
    pass
```

#### 2. Funkcja `raport_miesieczny()`

Stwórz funkcję generującą raport polis według miesięcy.

```python
def raport_miesieczny(sciezka_bazy, rok=None):
    """
    Generuje raport liczby i wartości polis rozpoczętych w każdym miesiącu.

    Args:
        sciezka_bazy: ścieżka do bazy SQLite
        rok: rok do analizy (domyślnie bieżący)

    Returns:
        Lista słowników:
        [
            {'miesiac': 1, 'nazwa': 'Styczeń', 'liczba': 5, 'suma': 3200.0},
            {'miesiac': 2, 'nazwa': 'Luty', 'liczba': 3, 'suma': 1800.0},
            ...
        ]
    """
    pass
```

#### 3. Funkcja `eksportuj_do_csv()`

Zaimplementuj eksport wyników wyszukiwania do pliku CSV.

```python
def eksportuj_do_csv(dane, sciezka_pliku, kolumny=None):
    """
    Eksportuje dane do pliku CSV.

    Args:
        dane: lista słowników do eksportu
        sciezka_pliku: ścieżka do pliku wyjściowego
        kolumny: lista kolumn do eksportu (domyślnie wszystkie)

    Returns:
        Liczba wyeksportowanych rekordów
    """
    pass
```

### Wymagania techniczne

- [ ] Użyj context managera (`with`) dla wszystkich operacji na bazie
- [ ] Wszystkie zapytania muszą być parametryzowane
- [ ] Używaj `row_factory` dla czytelności kodu
- [ ] Obsłuż potencjalne błędy (np. nieistniejąca baza, błędne dane)
- [ ] Dodaj docstringi do wszystkich funkcji

### Struktura plików

```
praca_domowa_dzien_01/
├── polisy_search.py      # Główny moduł z funkcjami
├── test_polisy_search.py # Testy (opcjonalnie)
└── wyniki/               # Katalog na wyeksportowane pliki
```

### Przykład użycia

```python
from polisy_search import (
    wyszukaj_polisy_zaawansowane,
    raport_miesieczny,
    eksportuj_do_csv
)

# Wyszukaj polisy OC powyżej 400 PLN
wyniki = wyszukaj_polisy_zaawansowane(
    'ergo_hestia.db',
    typ='OC',
    min_wartosc=400
)
print(f"Znaleziono {len(wyniki)} polis")

# Wygeneruj raport miesięczny
raport = raport_miesieczny('ergo_hestia.db', rok=2024)
for m in raport:
    print(f"{m['nazwa']}: {m['liczba']} polis, suma: {m['suma']} PLN")

# Eksportuj do CSV
eksportuj_do_csv(wyniki, 'wyniki/polisy_oc.csv')
```

### Podpowiedzi

1. **Daty w SQLite** - możesz używać funkcji `strftime('%m', data_od)` do wyciągnięcia miesiąca
2. **CSV** - użyj modułu `csv` z biblioteki standardowej
3. **JOIN** - do połączenia polis z klientami użyj `JOIN`
4. **NULL safety** - pamiętaj, że niektóre pola mogą być NULL

### Rozszerzenia (dla chętnych)

- Dodaj walidację formatu daty
- Zaimplementuj sortowanie wyników (parametr `sort_by`)
- Dodaj możliwość eksportu do JSON
- Napisz testy jednostkowe z użyciem `unittest` lub `pytest`

---

### Przesłanie rozwiązania

Rozwiązanie przeslij na slacka lub umiesc w swoim repozytorium GitHub i udostępnij link trenerowi przed następnymi zajęciami.
