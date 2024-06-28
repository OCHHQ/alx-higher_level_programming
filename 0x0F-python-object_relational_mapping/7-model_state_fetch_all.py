#!/usr/bin/python3
""" Lists all State objects from the database hbtn_0e_6_usa """

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

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
