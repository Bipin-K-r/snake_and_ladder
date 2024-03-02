class Player:
    def __init__(self, name, start_position=1):
        self.name = name
        self.position = start_position

    def move(self, steps, board):
        initial_position = self.position
        self.position += steps

        # if the new position is the start of a snake
        if self.position in board.snakes.keys():
            final_position = board.snakes[self.position]  # Move to the snake's tail
            print(
                f"{self.name} rolled a {steps} and bitten by snake at {self.position} and moved from {self.position} to {final_position}"
            )
            self.position = final_position

        # if the new position is the start of a ladder
        elif self.position in board.ladders.keys():
            final_position = board.ladders[self.position]  # Move to the top of the ladder
            print(
                f"{self.name} rolled a {steps} climbed the ladder at {self.position} and moved from {self.position} to {final_position}"
            )
            self.position = final_position

        else:  # normal roll
            print(f"{self.name} rolled a {steps} and moved from {initial_position} to {self.position}")
