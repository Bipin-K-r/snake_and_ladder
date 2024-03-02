import yaml
from models.game import Game


def _parse_config(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def main():
    config_path = "config/game_config.yml"
    game_config = _parse_config(config_path)

    # configuration for taking input - fallback on game_config.yml
    ask_user_for_config = input("do you want to enter input for snakes, ladders, and players? (y/n): ").strip().lower()
    if ask_user_for_config == "y":
        # Snakes
        total_snakes = int(input("number of snakes: "))
        snake_positions = [
            list(map(int, input(f"snake {i+1} head and tail position: ").split())) for i in range(total_snakes)
        ]
        game_config["snakes"] = {"number_of_snakes": total_snakes, "snake_position": snake_positions}

        # Ladders
        total_ladders = int(input("number of ladders: "))
        ladder_positions = [
            list(map(int, input(f"ladder {i+1} start and end position: ").split())) for i in range(total_ladders)
        ]
        game_config["ladders"] = {"number_of_ladders": total_ladders, "ladder_position": ladder_positions}

        # Players
        total_players = int(input("number of players: "))
        player_names_and_positions = {}
        for i in range(total_players):
            name, position = input(f"name and starting position for player {i+1}, space separated: ").split(" ")
            player_names_and_positions[name.strip()] = int(position.strip())
        game_config["players"]["number_of_players"] = total_players
        game_config["players"]["player_names_and_positions"] = player_names_and_positions

    game = Game(game_config)
    game.start()


if __name__ == "__main__":
    main()
