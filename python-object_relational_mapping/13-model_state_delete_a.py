#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL database using the provided credentials
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )

    # Create the tables if they don't already exist
    Base.metadata.create_all(eng)

    # Start a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query to find all states where the name contains the letter 'a' (case insensitive)
    states = session.query(State).filter(
        State.name.ilike('%a%')
    ).all()  # Using ilike for case-insensitive search

    # Loop through the states and delete them
    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
