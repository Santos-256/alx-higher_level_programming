#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
     # Establishing a connection to the MySQL database using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    #  Creating all tables defined in the metadata
    Base.metadata.create_all(engine)

     # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

      # Querying the database for State objects and ordering them by their id
    for instance in session.query(State).order_by(State.id):

        # Printing the id and name of each State object
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
