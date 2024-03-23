#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
     # Create an SQLAlchemy engine object to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
     # Create the tables defined in the Base class (if they do not exist already)
    Base.metadata.create_all(engine)

     # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)
#     Instantiate a Session object
    session = Session()
     # Query the State table and retrieve the first object
    instance = session.query(State).first()
# check if the retrieved instance exists
        if instance is None:
# If no instance is retrieved, print "Nothing"
        print("Nothing")
    else:
# If an instance is retrieved, print its id and name attributes separated by ": "
        print(instance.id, instance.name, sep=": ")
