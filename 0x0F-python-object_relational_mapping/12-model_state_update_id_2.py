#!/usr/bin/python3
""" Update the name of the State object where id = 2 to "New Mexico" """

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

    # Query the State with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name of the State
        state_to_update.name = "New Mexico"
        session.commit()
        print("State name updated successfully")
    else:
        print("State with id = 2 not found")

    # Close the session
    session.close()
