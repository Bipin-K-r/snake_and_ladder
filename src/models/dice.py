import random

class Dice:
    def __init__(self, number, strategy):
        self.number = number
        self.strategy = strategy

    def roll(self):
        rolls = [random.randint(1, 6) for _ in range(self.number)]
        if self.strategy == 'MAX':
            return max(rolls)
        elif self.strategy == 'MIN':
            return min(rolls)
        else: 
            return sum(rolls) # defaults to SUM -> self.strategy == 'SUM'
