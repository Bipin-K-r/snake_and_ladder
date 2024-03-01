from models.player import Player
from models.board import Board
from models.dice import Dice


class Game:
    def __init__(self, config):
        self.players = []
        for name, position in config["players"]["player_names_and_positions"].items():
            self.players.append(Player(name, position))
        self.board = Board(
            config["board_size"],
            config["snakes"],
            config["ladders"],
            config.get("crocodiles_positions", []),
            config.get("mines_positions", []),
        )
        self.dice = Dice(config["number_of_dies"], config["movement_strategy"])
        self.print_game_board = config.get("print_game_board", False)
        self.players_held_by_mines = {player.name: 0 for player in self.players}
        self.manual_dice_rolls = config.get("manual_dice_rolls", False)

    def print_board(self):
        for row in range(10, 0, -1):
            row_items = ""
            start = (row - 1) * 10 + 1
            end = row * 10 + 1
            for pos in range(start, end)[:: (-1 if row % 2 == 0 else 1)]:
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
                player_positions = [
                    f"P{index}" for index, player in enumerate(self.players, start=1) if player.position == pos
                ]
                if player_positions:
                    cell_content.extend(player_positions)

                cell = "/".join(cell_content) if cell_content else f"{pos:3}"  # padding 3
                row_items += f"{cell:7}"  # padding 7
            print(row_items)
            print("\n")

    def check_for_overlapping(self, current_player):
        for player in self.players:
            if player != current_player and player.position == current_player.position:
                player.position = 1
                print(
                    f"Overlap! {player.name} is moved back to start (position=1) because {current_player.name} rolled on the same spot"
                )

    def crocodiles_effect(self, player):
        if player.position in self.board.crocodiles:
            final_position = max(1, player.position - 5)  # can't go below 1
            print(
                f"{player.name} jumped on a crocodile and moved back 5 steps from {player.position} to {final_position}"
            )
            player.position = final_position

    def mine_effect(self, player):
        if player.position in self.board.mines:
            self.players_held_by_mines[player.name] = 2  # won't play for 2 turns
            print(f"{player.name} jumped on a mine and will be held for 2 turns at position: {player.position}")

    def start(self):
        print(f"Starting game with {len(self.players)} players")
        while True:
            for player in self.players:
                if self.players_held_by_mines[player.name] > 0:
                    print(f"{player.name} skips this turn")
                    self.players_held_by_mines[player.name] -= 1
                    continue
                
                if self.manual_dice_rolls: # playing manually
                    try:
                        roll = int(input(f"input the die roll for {player.name}: "))
                    except ValueError:
                        print("invalid input, please enter a number...")
                        continue
                else:
                    roll = self.dice.roll() # auto - default

                roll = self.dice.roll()
                player.move(roll, self.board)

                # different effects according to ruls
                self.crocodiles_effect(player)
                self.mine_effect(player)
                self.check_for_overlapping(player)

                if self.print_game_board:
                    self.print_board()

                if player.position >= self.board.size**2:  # win condition
                    print(f"{player.name} wins!")
                    return
