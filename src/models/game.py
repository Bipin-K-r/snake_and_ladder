from models.player import Player
from models.board import Board
from models.dice import Dice


class Game:
    def __init__(self, config):
        self.players = []
        for name, position in config["players"]["player_names_and_positions"].items():
            self.players.append(Player(name, position))
        self.board = Board(config["board_size"], config["snakes"], config["ladders"])
        self.dice = Dice(config["number_of_dies"], config["movement_strategy"])

    def start(self):
        # Game loop implementation
        print("Starting game with", len(self.players), "players.")
