#!/usr/bin/python3
"""A Script that lists all State objects from a database."""

from model_city import Base, State, City


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(host, password, name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    for state in session.query(State).join(City).order_by(City.id):
        for city in state.cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
