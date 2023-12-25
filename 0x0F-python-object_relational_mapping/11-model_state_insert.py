#!/usr/bin/python3
"""A Script that lists all State objects from a database."""

from model_state import Base, State


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
    query = session.query(State)
    new_state = State(name="Louisiana")
    session.add(new_state)
    states = query.all()
    for state in states.filter(State.name == "Louisiana"):
        print(f"{state.id}")
    session.close()
