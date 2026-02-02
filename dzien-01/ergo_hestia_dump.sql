-- =====================================================
-- ERGO HESTIA - Dump bazy danych do ćwiczeń
-- Dzień 1: Praca z bazą danych
-- =====================================================

-- Usunięcie istniejących tabel (jeśli istnieją)
DROP TABLE IF EXISTS polisy;
DROP TABLE IF EXISTS klienci;

-- =====================================================
-- TABELA: klienci
-- =====================================================
CREATE TABLE klienci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    email TEXT,
    telefon TEXT,
    pesel TEXT UNIQUE
);

-- =====================================================
-- TABELA: polisy
-- =====================================================
CREATE TABLE polisy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numer TEXT UNIQUE NOT NULL,
    typ TEXT NOT NULL CHECK(typ IN ('OC', 'AC', 'DOM', 'ZYCIE')),
    klient_id INTEGER NOT NULL,
    wartosc REAL NOT NULL,
    data_od DATE NOT NULL,
    data_do DATE NOT NULL,
    FOREIGN KEY (klient_id) REFERENCES klienci(id)
);

-- Indeksy dla wydajności
CREATE INDEX idx_polisy_typ ON polisy(typ);
CREATE INDEX idx_polisy_klient ON polisy(klient_id);
CREATE INDEX idx_polisy_data_do ON polisy(data_do);
CREATE INDEX idx_klienci_nazwisko ON klienci(nazwisko);

-- =====================================================
-- DANE: klienci
-- =====================================================
INSERT INTO klienci (id, imie, nazwisko, email, telefon, pesel) VALUES
(1, 'Jan', 'Kowalski', 'jan.kowalski@email.pl', '500-100-200', '80010112345'),
(2, 'Anna', 'Nowak', 'anna.nowak@email.pl', '501-200-300', '85052298765'),
(3, 'Piotr', 'Wiśniewski', 'piotr.wisniewski@email.pl', '502-300-400', '78030356789'),
(4, 'Maria', 'Kowalska', 'maria.kowalska@email.pl', '503-400-500', '90071187654'),
(5, 'Tomasz', 'Lewandowski', 'tomasz.lewandowski@email.pl', '504-500-600', '82121245678'),
(6, 'Katarzyna', 'Wójcik', 'katarzyna.wojcik@email.pl', '505-600-700', '88090912345'),
(7, 'Andrzej', 'Kamiński', 'andrzej.kaminski@email.pl', '506-700-800', '75050534567'),
(8, 'Małgorzata', 'Zielińska', 'malgorzata.zielinska@email.pl', '507-800-900', '92031198765'),
(9, 'Krzysztof', 'Szymański', 'krzysztof.szymanski@email.pl', '508-900-100', '79080823456'),
(10, 'Ewa', 'Dąbrowska', 'ewa.dabrowska@email.pl', '509-100-200', '86040467890'),
(11, 'Janusz', 'Kozłowski', 'janusz.kozlowski@email.pl', '510-200-300', '70020278901'),
(12, 'Agnieszka', 'Mazur', 'agnieszka.mazur@email.pl', '511-300-400', '91110589012'),
(13, 'Robert', 'Jankowski', 'robert.jankowski@email.pl', '512-400-500', '83060690123'),
(14, 'Joanna', 'Kwiatkowska', 'joanna.kwiatkowska@email.pl', '513-500-600', '87120701234'),
(15, 'Michał', 'Wojciechowski', 'michal.wojciechowski@email.pl', '514-600-700', '81090812345');

-- =====================================================
-- DANE: polisy
-- Różne typy, wartości i daty dla wszystkich ćwiczeń
-- =====================================================

-- Polisy OC (komunikacyjne)
INSERT INTO polisy (numer, typ, klient_id, wartosc, data_od, data_do) VALUES
('POL-OC-001', 'OC', 1, 450.00, '2024-01-15', '2025-01-14'),
('POL-OC-002', 'OC', 2, 380.00, '2024-02-01', '2025-01-31'),
('POL-OC-003', 'OC', 3, 520.00, '2024-03-10', '2025-03-09'),
('POL-OC-004', 'OC', 5, 410.00, '2024-04-20', '2025-04-19'),
('POL-OC-005', 'OC', 7, 480.00, '2024-05-15', '2025-05-14'),
('POL-OC-006', 'OC', 9, 395.00, '2024-06-01', '2025-05-31'),
('POL-OC-007', 'OC', 11, 550.00, '2024-07-20', '2025-07-19'),
('POL-OC-008', 'OC', 13, 425.00, '2024-08-10', '2025-08-09'),
('POL-OC-009', 'OC', 1, 460.00, '2025-01-15', '2026-01-14'),
('POL-OC-010', 'OC', 15, 490.00, '2025-02-01', '2026-01-31'),

-- Polisy wygasające w najbliższych 30 dniach (dla scenariusza raportowania)
('POL-OC-011', 'OC', 4, 430.00, '2025-02-01', '2026-02-15'),
('POL-OC-012', 'OC', 6, 470.00, '2025-02-10', '2026-02-20');

-- Polisy AC (autocasco)
INSERT INTO polisy (numer, typ, klient_id, wartosc, data_od, data_do) VALUES
('POL-AC-001', 'AC', 1, 1200.00, '2024-01-15', '2025-01-14'),
('POL-AC-002', 'AC', 2, 950.00, '2024-02-01', '2025-01-31'),
('POL-AC-003', 'AC', 3, 1450.00, '2024-03-10', '2025-03-09'),
('POL-AC-004', 'AC', 5, 1100.00, '2024-04-20', '2025-04-19'),
('POL-AC-005', 'AC', 7, 1350.00, '2024-05-15', '2025-05-14'),
('POL-AC-006', 'AC', 9, 980.00, '2024-06-01', '2025-05-31'),
('POL-AC-007', 'AC', 11, 1600.00, '2024-07-20', '2025-07-19'),
('POL-AC-008', 'AC', 13, 1250.00, '2024-08-10', '2025-08-09'),
('POL-AC-009', 'AC', 15, 1550.00, '2024-09-15', '2025-09-14'),
('POL-AC-010', 'AC', 2, 1050.00, '2025-02-01', '2026-01-31');

-- Polisy DOM (mieszkaniowe/domowe)
INSERT INTO polisy (numer, typ, klient_id, wartosc, data_od, data_do) VALUES
('POL-DOM-001', 'DOM', 1, 320.00, '2024-01-01', '2025-12-31'),
('POL-DOM-002', 'DOM', 4, 450.00, '2024-02-15', '2025-02-14'),
('POL-DOM-003', 'DOM', 6, 380.00, '2024-03-20', '2025-03-19'),
('POL-DOM-004', 'DOM', 8, 520.00, '2024-04-10', '2025-04-09'),
('POL-DOM-005', 'DOM', 10, 290.00, '2024-05-01', '2025-04-30'),
('POL-DOM-006', 'DOM', 12, 410.00, '2024-06-15', '2025-06-14'),
('POL-DOM-007', 'DOM', 14, 350.00, '2024-07-01', '2025-06-30'),
('POL-DOM-008', 'DOM', 3, 480.00, '2024-08-20', '2025-08-19'),
('POL-DOM-009', 'DOM', 5, 560.00, '2024-09-10', '2025-09-09'),
('POL-DOM-010', 'DOM', 7, 420.00, '2024-10-01', '2025-09-30');

-- Polisy ZYCIE (na życie)
INSERT INTO polisy (numer, typ, klient_id, wartosc, data_od, data_do) VALUES
('POL-ZYC-001', 'ZYCIE', 1, 2400.00, '2024-01-01', '2034-12-31'),
('POL-ZYC-002', 'ZYCIE', 2, 1800.00, '2024-02-01', '2034-01-31'),
('POL-ZYC-003', 'ZYCIE', 4, 3600.00, '2024-03-15', '2034-03-14'),
('POL-ZYC-004', 'ZYCIE', 6, 2100.00, '2024-04-01', '2034-03-31'),
('POL-ZYC-005', 'ZYCIE', 8, 4200.00, '2024-05-20', '2034-05-19'),
('POL-ZYC-006', 'ZYCIE', 10, 1500.00, '2024-06-10', '2034-06-09'),
('POL-ZYC-007', 'ZYCIE', 12, 2700.00, '2024-07-01', '2034-06-30'),
('POL-ZYC-008', 'ZYCIE', 14, 3000.00, '2024-08-15', '2034-08-14');

-- Dodatkowe polisy z 2025 roku dla raportu miesięcznego
INSERT INTO polisy (numer, typ, klient_id, wartosc, data_od, data_do) VALUES
('POL-OC-013', 'OC', 8, 440.00, '2025-01-05', '2026-01-04'),
('POL-OC-014', 'OC', 10, 510.00, '2025-01-20', '2026-01-19'),
('POL-AC-011', 'AC', 4, 1150.00, '2025-01-10', '2026-01-09'),
('POL-DOM-011', 'DOM', 9, 390.00, '2025-01-25', '2026-01-24'),
('POL-ZYC-009', 'ZYCIE', 3, 2550.00, '2025-01-15', '2035-01-14');

-- =====================================================
-- WERYFIKACJA DANYCH
-- =====================================================

-- Sprawdzenie liczby rekordów
-- SELECT 'Klienci:' as tabela, COUNT(*) as liczba FROM klienci
-- UNION ALL
-- SELECT 'Polisy:', COUNT(*) FROM polisy;

-- Statystyki polis według typu
-- SELECT typ, COUNT(*) as liczba, SUM(wartosc) as suma, ROUND(AVG(wartosc), 2) as srednia
-- FROM polisy GROUP BY typ ORDER BY typ;
