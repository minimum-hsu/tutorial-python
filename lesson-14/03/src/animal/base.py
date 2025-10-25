class Animal():

    def __init__(self, kind: str, name: str, legs: int):
        '''
        The first step when creating a new object
        '''

        self.__kind = kind
        self.name = name
        self.legs = legs

    def hello(self):
        print('My name is {}. I am {}.'.format(self.name, self.__kind))

    def run(self):
        print('no defined action')
