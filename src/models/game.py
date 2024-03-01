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

    def print_board(self):
        for row in range(10, 0, -1):
            row_items = ""
            start = (row - 1) * 10 + 1
            end = row * 10 + 1
            for pos in range(start, end)[::(-1 if row % 2 == 0 else 1)]:
                cell_content = []
                # Representing snakes and ladders - 
                # S1S: Snake 1 Start, S1E: Snake 1 End
                # L1S: Ladder 1 Start, L1E: Ladder 1 End
                for index, (s_start, s_end) in enumerate(self.board.snakes.items(), start=1):
                    if pos == s_start:
                        cell_content.append(f"S{index}S")
                    elif pos == s_end:
                        cell_content.append(f"S{index}E")
                for index, (l_start, l_end) in enumerate(self.board.ladders.items(), start=1):
                    if pos == l_start:
                        cell_content.append(f"L{index}S")
                    elif pos == l_end:
                        cell_content.append(f"L{index}E")
                # Representing players
                # P1: Player 1, P2: Player 2
                player_positions = [f"P{index}" for index, player in enumerate(self.players, start=1) if player.position == pos]
                if player_positions:
                    cell_content.extend(player_positions)

                cell = '/'.join(cell_content) if cell_content else f"{pos:3}"
                row_items += f"{cell:7}"
            print(row_items)
            print("\n")


    def start(self):
        # Game loop implementation
        print("Starting game with", len(self.players), "players.")
        self.print_board()
        # while True:
        #     for player in self.players:
        #         roll = self.roll_dice()
        #         self.update_player_position(player, roll)
        #         self.print_board()
        #         if player.position >= 100:
        #             print(f"{player.name} wins!")
        #             return
