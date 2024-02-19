#!/usr/bin/python3
"""
A script that prints all City objects from the database.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name)

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(
            City, State).join(State).order_by(City.id.asc()).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
