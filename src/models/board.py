class Board:
    def __init__(self, size, snakes, ladders, crocodile=None, mine=None):
        self.size = size
        self.snakes = {}
        for i in range(snakes['number_of_snakes']):
            start, end = snakes['snake_position'][i]
            self.snakes[start] = end
        self.ladders = {}
        for i in range(ladders['number_of_ladders']):
            bottom, top = ladders['ladder_position'][i]
            self.ladders[bottom] = top
        self.crocodile = crocodile
        self.mine = mine
