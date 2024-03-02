# snake_and_ladder
snake and ladder game

## symlink for running tests
    - ln -s ../src/models models

## Game Config
    - Game is taking the config from config/game_config.yml
    - There's config for players, board size, snakes, crocs, mines,
        dice as per game requirements
        - if the ladder position is given like [9,4], start point of ladder / bottom will be 4
            code swaps the value if in bottom > top in [bottom, top]  
            - rule states, ladder always takes up
    - There're extra configs too:
        - print_game_board - if enabled, it'll print the current board after each dice roll
        - manual_dice_rolls - if enabled, game will be kind of manual, user can input 
                                dice roll values (like playing offline)
                    

## Game Flow
    - when the game starts:
        - user is asked if he wants to give custom values for players,
            ladders, snakes; if he does values in game_config.yml will overwrite
        - before each dice roll, user is asked if he wants to manually change the number of dice
            for the current roll, and after the roll, it gets reset to one that was in game_config.yml
        

## win
    - whenever a player's position is greater than or equal to end position,
        i.e. game_board_size * game_board_size, player wins

## for running
    - one needs to run the main.py
    - have created a run.sh which will run that