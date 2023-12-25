#!/usr/bin/python3
"""A Script that lists all State objects from a database."""

from model_state import Base, State


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name, search = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(host, password, name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    query = session.query(State).filter(State.name == search)
    state = query.first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
