#!/usr/bin/env python3

from model import User
from model import Address
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#############################
# MySQL Database Settings
#############################
USERNAME = 'root'
PASSWORD = 'password123'
HOST = 'localhost'
PORT = 3306
DATABASE = 'demo'

#############################
# Main
#############################
if __name__ == '__main__':
    # Create an MySQL database in memory
    engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}', echo=False)

    # Create all tables defined in the model
    from model import Base

    Base.metadata.create_all(engine)

    # Create a new session
    with Session(engine) as session:
        # Create new User and Address instances
        alice = User(
            name='alice',
            age=30,
            addresses=[Address(email_address='alice@example.com')]
        )
        bob = User(
            name='bob',
            age=25,
            addresses=[Address(email_address='bob@example.com')]
        )
        charlie = User(
            name='charlie',
            age=35,
            addresses=[Address(email_address='charlie@example.com')]
        )

        # Add the instances to the session and commit
        session.add_all([alice, bob, charlie])
        session.commit()

        # auto close session

    # Query users aged 30 or older
    with Session(engine) as session:
        stmt = session.query(User).filter(User.age >= 30)
        for user in stmt:
            print(user)
            for address in user.addresses:
                print('  ', address)

        # auto close session
