#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Get the state name from the argument
    state_name = sys.argv[4]
    
    # Query the database for the state with the given name
    state = session.query(State).filter(State.name == state_name).first()
    
    # Print the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    
    # Close the session
    session.close()
