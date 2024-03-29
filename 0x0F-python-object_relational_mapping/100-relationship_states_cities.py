#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Create a connection to the MySQL server
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True
            )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a State object "California" and a City object "San Francisco"
    california = State(name="California", cities=[City(name="San Francisco")])

    # Add the State object to the session
    session.add(california)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
