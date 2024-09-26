import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from contextlib import contextmanager

Base = declarative_base()

# Définir la table Person
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

# Définir la table Address
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# Créer la base de données
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.create_all(engine)

# Définir la classe de requêtes avec un gestionnaire de contexte
class PersonRequests:
    def __init__(self, session):
        self.session = session

    def insert(self, name):
        new_person = Person(name=name)
        self.session.add(new_person)
        self.session.commit()
        return new_person

    def select_all(self):
        return self.session.query(Person).all()

    def select_by_name(self, name):
        return self.session.query(Person).filter_by(name=name).first()

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# Utilisation du gestionnaire de contexte pour les requêtes
DBSession = sessionmaker(bind=engine)

with session_scope() as session:
    person_requests = PersonRequests(session)
    # Insérer une nouvelle personne
    new_person = person_requests.insert(name='Dupond')
    print(f"Inserted: {new_person.name}")

    # Sélectionner toutes les personnes
    all_persons = person_requests.select_all()
    print("All persons:", [person.name for person in all_persons])

    # Sélectionner une personne par nom
    person = person_requests.select_by_name(name='Dupond')
    print(f"Selected by name: {person.name}")