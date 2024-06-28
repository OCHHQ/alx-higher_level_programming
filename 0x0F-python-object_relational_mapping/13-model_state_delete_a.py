#!/usr/bin/python3
""" Delete all State objects with a name containing the letter 'a' """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete all State objects with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
        print(f"{len(states_to_delete)} state(s) deleted successfully")
    else:
        print("No states found with names containing 'a'")

    # Close the session
    session.close()
