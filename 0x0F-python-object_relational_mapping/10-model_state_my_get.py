#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
