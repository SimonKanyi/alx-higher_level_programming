#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    
    # Create a new State object
    new_state = State(name="Louisiana")
    
    # Add the new State object to the session
    session.add(new_state)
    
    # Commit the transaction to the database
    session.commit()
    
    # Print the new state's id
    print(f"{new_state.id}")
    
    # Close the session
    session.close()
