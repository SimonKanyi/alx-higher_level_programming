#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
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
    
    # Create a Session
    session = Session()
    
    # Query all State objects that contain the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
