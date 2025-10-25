#!/usr/bin/env python3

from model import User

if __name__ == '__main__':
    user = User(name='Alice', age=30, email='alice@example.com')
    print('User Information:')
    print(f'name: {user.name}')
    print(f'age: {user.age}')
    print(f'email: {user.email}')
