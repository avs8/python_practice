# asking clear about my class understanding
# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
from abc import abstractmethod


class Customer(object):
    """
    Customer of bank and have following attributes.
    1- name
    2-Account
    """

    def __init__(self, name, balance=0):
        """
        here i am trying to say customer has atwo attributes name
        and balance.
        """
        self.name = name
        self.balance = balance

    @staticmethod
    def welcome():
        print "Welcome to Our Bank. How can we help you today"

    def withdraw(self, amount):
        """
        if customer request for money first check if he had enough balance.
        make sure to

        """
        if amount < self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise RuntimeError('Requested amount is more then current balance')

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @classmethod
    def welcome_2(cls):
        """
        class method are just varient to static method and are more use
        full when we inherit the base class into child
        :return:
        """
        print "Welcome Again to our Site. How can i help you"

    @abstractmethod
    def find_address(self):
        """
        will implement later
        :return:
        """
        pass


ajita = Customer('Ajita', 50000)
print ajita.name
print ajita.welcome()
print ajita.welcome_2()
Customer('Ajita2', 50000).welcome()
Customer('Ajita3', 5000).welcome_2()
