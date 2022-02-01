"""Game Stats Program"""

def display_players(players: dict[dict]) -> None:
    """Display the players alphabetically from a dictionary of dictionaries containing player stats."""
    players: list = list(players.keys())
    players.sort()
    for player in players:
        print(player.capitalize())

def display_player_stats(player: dict) -> None:
    """Display the player statistics in order given. Key/Value pairs."""
    for stat in player:
        print(f'{stat.capitalize()}:\t{player[stat]}')

def get_player(players: dict[dict]) -> dict:
    """Get the desired player from user and confirm player exists."""
    player: str = input('\nEnter a player name: ').lower()
    try:
        player: dict = players[player]
        return player
    except KeyError as e:
        print(f'There is no player named {player}')
        return {}

def game_stats_splash() -> None:
    """The start or splash of game stats."""
    print('Game Stats Program\n')
    display_players(player_stats)

def game_stats_loop() -> None:
    """Primary loop of game stats."""
    proceed_char: str = 'y'
    while proceed_char == 'y':
        player: dict = get_player(player_stats)
        display_player_stats(player)
        proceed_char: str = input('\nContinue? (y/n): ').lower()
    print('\nBye!')

def main() -> None:
    """Game stats main control function."""
    game_stats_splash()
    game_stats_loop()

if __name__ == '__main__':
    player_stats: dict[dict] = {
        'elizabeth': {
            'wins': 41,
            'losses': 3,
            'ties': 22
        },
        'mike': {
            'wins': 8,
            'losses': 19,
            'ties': 11
        },
        'joel': {
            'wins': 32,
            'losses': 14,
            'ties': 17
        }   
    }
    main()
