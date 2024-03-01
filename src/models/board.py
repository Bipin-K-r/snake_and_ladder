class Board:
    def __init__(self, size, snakes, ladders, crocodile=None, mine=None):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders
        self.crocodile = crocodile
        self.mine = mine
