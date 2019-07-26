#!/usr/bin/env python3
from random import randint

class Player:
    def __init__(self, name):
        self.dice = []
        self.name = name
    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))
    def get_dice(self):
        return self.dice
    def name(self):
        return self.name
player1 = Player("sam")
player2 = Player("bob")

player1.roll()

print(f'Player {player1.name}  rolled {player1.get_dice()}')

