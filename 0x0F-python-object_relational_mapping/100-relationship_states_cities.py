#!/usr/bin/python3
"""
Creates a State and a City in the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Create the tables
    Base.metadata.create_all(engine)
    
    # Create a State and City
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    
    # Add the state and city to the session
    session.add(california)
    session.add(san_francisco)
    
    # Commit the transaction
    session.commit()
    
    # Print the results
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    
    # Close the session
    session.close()
