from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Client(Base):
    __tablename__ = 'klienci_test'
    id = Column(Integer, primary_key=True)
    imie = Column(String(50))
    nazwisko = Column(String(50))
    policies = relationship("Policy", back_populates="client",
                         cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Client {self.imie} {self.nazwisko}>"

class Policy(Base):
    __tablename__ = 'polisy_test'
    id = Column(Integer, primary_key=True)
    numer = Column(String(20))
    typ = Column(String(10))
    wartosc = Column(Float)
    klient_id = Column(Integer, ForeignKey('klienci_test.id'))
    client = relationship("Client", back_populates="policies")

    def __repr__(self):
        return f"<Policy {self.numer}>"

# 1. Engine i sesja
engine = create_engine('sqlite:///test_orm.db', echo=False)
Base.metadata.create_all(engine) # Jezeli nie chcemy stworzyc kolejnej bazy mozna to zakomentowac
Session = sessionmaker(bind=engine)
session = Session()

try:
    # 2. CREATE - dodanie klienta z polisami
    print("=== CREATE ===")
    client = Client(imie='Zbigniew', nazwisko='Testowy')
    client.policies = [
        Policy(numer='TEST-001', typ='OC', wartosc=500),
        Policy(numer='TEST-002', typ='AC', wartosc=1200)
    ]
    session.add(client)
    session.commit()
    print(f"Dodano klienta: {client}")
    print(f"ID klienta: {client.id}")

    # 3. READ - pobranie i wyświetlenie
    print("\n=== READ ===")
    client = session.query(Client).filter_by(nazwisko='Testowy').first()
    print(f"Klient: {client.imie} {client.nazwisko}")
    print("Polisy:")
    for p in client.policies:
        print(f"  - {p.numer}: {p.typ} = {p.wartosc} PLN")

    # 4. UPDATE - aktualizacja polisy
    print("\n=== UPDATE ===")
    policy = session.query(Policy).filter_by(numer='TEST-001').first()
    old_value = policy.wartosc
    policy.wartosc = 550
    session.commit()
    print(f"Zaktualizowano polisę {policy.numer}: {old_value} -> {policy.wartosc} PLN")

    # 5. DELETE - usunięcie polisy
    print("\n=== DELETE ===")
    policy_to_delete = session.query(Policy).filter_by(numer='TEST-002').first()
    deleted_number = policy_to_delete.numer
    session.delete(policy_to_delete)
    session.commit()
    print(f"Usunięto polisę {deleted_number}")

    # Weryfikacja
    print("\n=== WERYFIKACJA ===")
    client = session.query(Client).filter_by(nazwisko='Testowy').first()
    print(f"Polisy klienta po zmianach:")
    for p in client.policies:
        print(f"  - {p.numer}: {p.wartosc} PLN")

except Exception as e:
    session.rollback()
    print(f"Błąd: {e}")
finally:
    session.close()