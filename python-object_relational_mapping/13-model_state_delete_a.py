#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def delete_states():
    # Ensure proper number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>")
        return
    
    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the states with a name containing 'a' and delete them
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    delete_states()
