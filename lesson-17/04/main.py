#!/usr/bin/env python3

from model import User
from pynamodb.exceptions import DoesNotExist
from pynamodb.exceptions import PutError
from pynamodb.exceptions import TableError

if __name__ == '__main__':
    try:
        # Create the table if it doesn't exist
        if not User.exists():
            print("Creating User table...")
            User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
            print("Table created successfully!")

        # Create a new user
        user = User(
            email='alice@example.com',
            name='Alice',
            age=30
        )
        user.save()
        print(f"User {user.name} saved successfully!")

        # Query the user back
        try:
            retrieved_user = User.get('alice@example.com')
            print(f"Retrieved user: {retrieved_user.name}, age: {retrieved_user.age}")
        except DoesNotExist:
            print("User not found")

    except TableError as e:
        print(f"Table error: {e}")
    except PutError as e:
        print(f"Put error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
