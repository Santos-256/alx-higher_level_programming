#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    #  Create an SQLAlchemy engine object to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the tables defined in the Base class (if they do not exist already)
    Base.metadata.create_all(engine)

    # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)

     # Instantiate a Session object
    session = Session()

     # Query the State table, order by the id column, and iterate over the results
    for instance in session.query(State).order_by(State.id):

         # Print the id and name attributes of each State instance separated by ": "
        print(instance.id, instance.name, sep=": ")
