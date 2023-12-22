#!/usr/bin/python3
"""A Script that lists all State objects from a database."""

from model_state import Base, State


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys

    host, password, name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(host, password, name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
