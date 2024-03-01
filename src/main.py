import yaml
from models.game import Game


def _parse_config(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def main():
    config_path = "config/game_config.yml"
    game_config = _parse_config(config_path)

    game = Game(game_config)
    game.start()


if __name__ == "__main__":
    main()
