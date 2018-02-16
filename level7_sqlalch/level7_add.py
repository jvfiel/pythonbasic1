from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from level7_sqlalchemy import Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.sqlite')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert a Person in the person table
new_person = Person(name='new person')
session.add(new_person)
session.commit()

#QUERY ALL
persons = session.query(Person).all()
print persons
for person in persons:
    print person.id, person.name
    person.name = "John"
    # session.delete(person)

session.commit()
session.close()


DBSession = sessionmaker(bind=engine)
session = DBSession()

#QUERY ALL
persons = session.query(Person).all()
print persons
for person in persons:
    print person.id, person.name
