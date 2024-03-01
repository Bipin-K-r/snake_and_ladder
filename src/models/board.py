class Board:
    def __init__(self, size, snakes, ladders, crocodiles=[], mines=[]):
        self.size = size
        self.snakes = {}
        for i in range(snakes['number_of_snakes']):
            start, end = snakes['snake_position'][i]
            self.snakes[start] = end
        self.ladders = {}
        for i in range(ladders['number_of_ladders']):
            bottom, top = ladders['ladder_position'][i]
            if bottom > top: # in rules it's mentioned that ladders takes you up (strictly)
                bottom, top = top, bottom
            self.ladders[bottom] = top
        self.crocodiles = crocodiles
        self.mines = mines
