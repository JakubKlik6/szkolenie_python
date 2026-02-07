# Zadania praktyczne - Dzień 3

## Zadanie 1: Manipulacja tablicami wielowymiarowymi

**Poziom trudności:** ⭐⭐
**Czas:** 10 minut

### Opis

Przećwicz podstawowe operacje na tablicach NumPy.

### Wymagania

1. Stwórz tablicę 4x6 z liczbami od 1 do 24
2. Wyświetl jej kształt, wymiary i typ danych
3. Pobierz trzeci wiersz
4. Pobierz drugą kolumnę
5. Pobierz wycinek 2x2 ze środka tablicy
6. Znajdź wszystkie elementy większe od 12

### Szablon

```python
import numpy as np

# 1. Stwórz tablicę 4x6 z liczbami 1-24
arr = # TODO

# 2. Wyświetl atrybuty
print(f"Kształt: {}")
print(f"Wymiary: {}")
print(f"Typ: {}")

# 3. Trzeci wiersz (indeks 2)
trzeci_wiersz = # TODO
print(f"Trzeci wiersz: {trzeci_wiersz}")

# 4. Druga kolumna (indeks 1)
druga_kolumna = # TODO
print(f"Druga kolumna: {druga_kolumna}")

# 5. Wycinek 2x2 ze środka
srodek = # TODO
print(f"Środek:\n{srodek}")

# 6. Elementy > 12
wieksze = # TODO
print(f"Elementy > 12: {wieksze}")
```

### Wskazówki

- `np.arange(start, stop).reshape(rows, cols)`
- Indeksowanie 2D: `arr[wiersz, kolumna]`
- Cała kolumna: `arr[:, indeks_kolumny]`
- Boolean indexing: `arr[arr > wartość]`

---

## Zadanie 2: Analiza danych polis bez pętli

**Poziom trudności:** ⭐⭐
**Czas:** 15 minut

### Opis

Przeprowadź analizę statystyczną portfela polis używając wyłącznie operacji wektorowych NumPy (bez pętli!).

### Wymagania

1. Wygeneruj 10,000 losowych wartości polis (200-5000 PLN)
2. Oblicz statystyki: średnia, mediana, odchylenie standardowe, min, max
3. Znajdź ile polis ma wartość powyżej średniej
4. Policz polisy w przedziałach: <1000, 1000-2000, 2000-3000, >3000
5. Podnieś wartość wszystkich polis o 5%

### Szablon

```python
import numpy as np

# Ustal seed dla powtarzalności
np.random.seed(42)

# 1. Wygeneruj 10000 wartości polis (200-5000)
polisy = # TODO

# 2. Statystyki
srednia = # TODO
mediana = # TODO
std = # TODO
minimum = # TODO
maximum = # TODO

print(f"Średnia: {srednia:.2f} PLN")
print(f"Mediana: {mediana:.2f} PLN")
print(f"Odch. std: {std:.2f} PLN")
print(f"Min: {minimum:.2f} PLN")
print(f"Max: {maximum:.2f} PLN")

# 3. Polisy powyżej średniej
powyzej_sredniej = # TODO (liczba)
print(f"\nPolisy > średniej: {powyzej_sredniej}")

# 4. Przedziały (bez pętli!)
ponizej_1000 = # TODO
od_1000_do_2000 = # TODO
od_2000_do_3000 = # TODO
powyzej_3000 = # TODO

print(f"\n<1000: {ponizej_1000}")
print(f"1000-2000: {od_1000_do_2000}")
print(f"2000-3000: {od_2000_do_3000}")
print(f">3000: {powyzej_3000}")

# 5. Podwyżka 5%
polisy_podwyzszone = # TODO
print(f"\nNowa średnia po podwyżce: {np.mean(polisy_podwyzszone):.2f} PLN")
```

### Wskazówki

- `np.random.uniform(min, max, size)`
- `np.sum(arr > wartość)` zlicza True
- Warunki łącz przez `&`: `(arr >= a) & (arr < b)`
- Mnożenie: `arr * 1.05`

---

## Zadanie 3: Macierz szkodowości

**Poziom trudności:** ⭐⭐⭐
**Czas:** 15 minut

### Opis

Analizuj macierz szkodowości (12 miesięcy x 5 lat) używając agregacji NumPy.

### Wymagania

1. Wygeneruj macierz 12x5 z losowymi szkodami (50,000 - 200,000 PLN)
2. Oblicz sumę szkód dla każdego roku
3. Oblicz średnią miesięczną szkodę (średnia z 5 lat dla każdego miesiąca)
4. Znajdź miesiąc i rok z najwyższą szkodą
5. Znajdź miesiąc z najniższą średnią szkodą
6. Oblicz trend roczny (o ile wzrosły/spadły szkody rok do roku)

### Szablon

```python
import numpy as np

np.random.seed(42)

miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze',
            'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']
lata = [2021, 2022, 2023, 2024, 2025]

# 1. Wygeneruj macierz szkód (12 miesięcy x 5 lat)
szkody = # TODO - wartości 50000-200000

print("Macierz szkodowości (w tys. PLN):")
print(szkody / 1000)

# 2. Suma roczna (axis=?)
sumy_roczne = # TODO
print("\nSumy roczne:")
for rok, suma in zip(lata, sumy_roczne):
    print(f"  {rok}: {suma:,.0f} PLN")

# 3. Średnia miesięczna
srednie_miesieczne = # TODO
print("\nŚrednia miesięczna (5 lat):")
# TODO: wyświetl

# 4. Najwyższa szkoda - znajdź indeksy
# TODO

# 5. Miesiąc z najniższą średnią
# TODO

# 6. Trend roczny (różnica między kolejnymi latami)
# TODO
```

### Wskazówki

- `axis=0` sumuje po wierszach (wynik: wartość per kolumna)
- `axis=1` sumuje po kolumnach (wynik: wartość per wiersz)
- `np.argmax()` zwraca płaski indeks, użyj `np.unravel_index(idx, shape)`
- `np.diff(arr)` oblicza różnice między kolejnymi elementami

---

## Zadanie 4: Normalizacja i standaryzacja danych

**Poziom trudności:** ⭐⭐⭐
**Czas:** 15 minut

### Opis

Przygotuj dane o składkach do analizy poprzez normalizację i standaryzację.

### Wymagania

1. Wygeneruj dane: 5 typów polis, każdy z 1000 składek
2. Oblicz statystyki dla każdego typu osobno
3. Wykonaj normalizację Min-Max (przeskaluj do [0, 1])
4. Wykonaj standaryzację Z-score (średnia=0, std=1)
5. Porównaj rozkłady przed i po transformacjach

### Szablon

```python
import numpy as np

np.random.seed(42)

typy = ['OC', 'AC', 'DOM', 'ZYCIE', 'NNW']

# 1. Wygeneruj dane - macierz 5x1000 (każdy typ ma inny zakres)
# OC: 300-800, AC: 800-2500, DOM: 400-1200, ZYCIE: 1000-5000, NNW: 100-400
dane = np.array([
    # TODO: wygeneruj dla każdego typu
])

print("Statystyki oryginalne:")
for i, typ in enumerate(typy):
    print(f"  {typ}: mean={np.mean(dane[i]):,.0f}, "
          f"std={np.std(dane[i]):,.0f}, "
          f"min={np.min(dane[i]):,.0f}, max={np.max(dane[i]):,.0f}")

# 2. Normalizacja Min-Max: (x - min) / (max - min)
# Dla każdego typu osobno!
dane_norm = # TODO

print("\nPo normalizacji Min-Max:")
for i, typ in enumerate(typy):
    print(f"  {typ}: min={np.min(dane_norm[i]):.2f}, max={np.max(dane_norm[i]):.2f}")

# 3. Standaryzacja Z-score: (x - mean) / std
dane_std = # TODO

print("\nPo standaryzacji Z-score:")
for i, typ in enumerate(typy):
    print(f"  {typ}: mean={np.mean(dane_std[i]):.4f}, std={np.std(dane_std[i]):.4f}")
```

### Wskazówki

- `np.random.uniform(low, high, size)` dla każdego typu osobno
- Używaj `axis=1, keepdims=True` żeby zachować wymiary przy obliczaniu mean/std per wiersz
- Sprawdź czy wyniki są poprawne: po normalizacji min=0, max=1; po standaryzacji mean~0, std~1

---

## Zadanie 5: Porównanie wydajności

**Poziom trudności:** ⭐⭐
**Czas:** 10 minut

### Opis

Zmierz różnicę w czasie wykonania między pętlami Python a operacjami NumPy.

### Wymagania

1. Stwórz tablicę 1,000,000 elementów
2. Oblicz sumę kwadratów używając pętli Python
3. Oblicz sumę kwadratów używając NumPy
4. Porównaj czasy wykonania
5. Powtórz dla operacji filtrowania (elementy > średnia)

### Szablon

```python
import numpy as np
import time

# Rozmiar danych
n = 1_000_000

# Dane
lista = list(range(n))
arr = np.arange(n)

# 1. Suma kwadratów - pętla
start = time.time()
suma_petla = # TODO: użyj pętli
czas_petla = time.time() - start
print(f"Pętla: {czas_petla:.4f}s, wynik: {suma_petla}")

# 2. Suma kwadratów - NumPy
start = time.time()
suma_numpy = # TODO: użyj NumPy
czas_numpy = time.time() - start
print(f"NumPy: {czas_numpy:.4f}s, wynik: {suma_numpy}")

print(f"\nNumPy jest {czas_petla/czas_numpy:.1f}x szybszy")

# 3. Filtrowanie - pętla vs NumPy
srednia = np.mean(arr)

start = time.time()
# TODO: filtruj pętlą
czas_filtr_petla = time.time() - start

start = time.time()
# TODO: filtruj NumPy
czas_filtr_numpy = time.time() - start

print(f"\nFiltrowanie:")
print(f"  Pętla: {czas_filtr_petla:.4f}s")
print(f"  NumPy: {czas_filtr_numpy:.4f}s")
print(f"  Przyspieszenie: {czas_filtr_petla/czas_filtr_numpy:.1f}x")
```

### Wskazówki

- Suma kwadratów: `np.sum(arr ** 2)`
- Filtrowanie: `arr[arr > srednia]`
- Wyniki powinny być identyczne (lub bardzo zbliżone dla float)
