"""Baseball Team Manager file I/O."""

import csv
from player import Player

FILENAME: str = "players.txt"

def read_players() -> list[Player]:
    """Read players from player file and make list of player objects."""
    try:
        players: list = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                full_name: str = row[0]
                first_name = full_name.split(' ')[0]
                last_name = full_name.split(' ')[1]
                player: Player = Player(first_name, last_name, row[1], row[2], row[3])
                players.append(player)
        return players
    except FileNotFoundError:
        return None

def write_players(players: list[Player]) -> None:
    """Write list of players to player file."""
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list_players_to_list_list(players))

def list_players_to_list_list(players: list[Player]) -> list[list]:
    """Convert list of player objects to list of lists."""
    return [[player.full_name, player.position, player.at_bats, player.hits] for player in players]