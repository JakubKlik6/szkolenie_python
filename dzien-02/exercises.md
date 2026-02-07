
## Konfiguracja PostgreSQL

**Czas:** 5-10 minut

### Opis

Przed przystąpieniem do kolejnych zadań, musimy przejść z bazy SQLite na PostgreSQL.
PostgreSQL to profesjonalna baza danych używana w środowiskach produkcyjnych.

### Kroki konfiguracji

1. **Uruchom PostgreSQL** (jeśli nie jest uruchomiony):
   ```bash
   # macOS (Homebrew)
   brew services start postgresql

   # Linux
   sudo systemctl start postgresql

   # Docker
   docker run --name postgres-szkolenie -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
   ```

2. **Utwórz bazę danych**:
   ```bash
   # Połącz się z PostgreSQL
   psql -U postgres

   # Utwórz bazę danych
   CREATE DATABASE ergo_hestia;

   # Wyjdź z psql
   \q
   ```

3. **Wgraj dump bazy danych**:
   ```bash
   psql -U postgres -d ergo_hestia -f ergo_hestia_dump_postgres.sql
   ```

4. **Zainstaluj bibliotekę psycopg2** (jeśli nie masz):
   ```bash
   pip install psycopg2-binary
   ```

5. **Sprawdź połączenie** (opcjonalnie):
   ```python
   import psycopg2

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
   ```

### Główne różnice SQLite vs PostgreSQL

| Aspekt | SQLite | PostgreSQL |
|--------|--------|------------|
| Biblioteka | `sqlite3` | `psycopg2` |
| Placeholder | `?` | `%s` |
| Połączenie | ścieżka do pliku | host, port, user, password, database |
| Row factory | `sqlite3.Row` | `RealDictCursor` |

---



## Zadanie 1: Raport klientów z polisami (PostgreSQL)

**Poziom trudności:** ⭐⭐
**Czas:** 15 minut

### Opis

Napisz funkcję, która generuje raport klientów wraz z ich polisami. Raport powinien zawierać imię, nazwisko klienta oraz listę jego polis z numerami i wartościami.

### Wymagania

- [ ] Użyj `psycopg2` do połączenia z PostgreSQL
- [ ] Użyj JOIN do połączenia tabel `klienci` i `polisy`
- [ ] Pogrupuj wyniki po kliencie
- [ ] Zwróć dane w strukturze słownikowej

### Szablon

```python
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
    # TODO: Uzupełnij kod
    # Pamiętaj o:
    # - Użyciu RealDictCursor dla wyników jako słowniki
    # - Użyciu JOIN do połączenia tabel
    # - Grupowaniu wyników po kliencie
    pass

# Test
if __name__ == "__main__":
    report = clients_policies_report()
    for client in report:
        print(f"\n{client['client']} ({client['email']}):")
        for policy in client['policies']:
            print(f"  - {policy['numer']}: {policy['typ']} = {policy['wartosc']} PLN")
```

### Wskazówki

- Użyj `cursor_factory=RealDictCursor` przy tworzeniu kursora
- Użyj `defaultdict(list)` do grupowania polis po kliencie
- Możesz użyć `ORDER BY` w SQL, aby wyniki były posortowane
- Pamiętaj o zamknięciu połączenia (lub użyj context managera)

---



## Zadanie 2: CRUD z SQLAlchemy

**Poziom trudności:** ⭐⭐
**Czas:** 15 minut

### Opis

Używając SQLAlchemy ORM, wykonaj następujące operacje:
1. Utwórz nowego klienta
2. Dodaj mu 2 polisy
3. Pobierz klienta i wyświetl jego polisy
4. Zaktualizuj wartość jednej polisy
5. Usuń jedną polisę

### Wymagania

- [ ] Zdefiniuj modele `Client` i `Policy` z relacją
- [ ] Utwórz silnik i sesję
- [ ] Wykonaj wszystkie operacje CRUD
- [ ] Wyświetl wyniki każdej operacji

### Szablon

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Client(Base):
    __tablename__ = 'klienci_test'
    id = Column(Integer, primary_key=True)
    imie = Column(String(50))
    nazwisko = Column(String(50))
    policies = relationship("Policy", back_populates="client")

class Policy(Base):
    __tablename__ = 'polisy_test'
    id = Column(Integer, primary_key=True)
    numer = Column(String(20))
    typ = Column(String(10))
    wartosc = Column(Float)
    klient_id = Column(Integer, ForeignKey('klienci_test.id'))
    client = relationship("Client", back_populates="policies")

# TODO: Uzupełnij kod
# 1. Stwórz engine i sesję
# 2. Utwórz tabele
# 3. Dodaj klienta z polisami
# 4. Pobierz i wyświetl
# 5. Zaktualizuj polisę
# 6. Usuń polisę
```