"""
This is a file consisting of player class
"""


class Player:

    def __init__(self, name):
        """
        :param name: Nam of the player
        :type name: str
        """
        self.name = name
        self.money = 1000

    def add_money(self, money_to_add):
        self.money += money_to_add

    def remove_money(self, money_to_remove):
        self.money -= money_to_remove

    def info(self):
        return f'{self.name}, Your account state is {self.money}$'
