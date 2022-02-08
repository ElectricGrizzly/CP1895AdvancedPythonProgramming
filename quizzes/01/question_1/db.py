"""Baseball Team Manager file I/O."""

import csv

FILENAME: str = "players.txt"

def read_players() -> list[dict]:
    """Read players file and return a list of dictionaries."""
    try:
        players: list = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                player: dict = {}
                player['name'] = row[0]
                player['position'] = row[1]
                player['at_bats'] = row[2]
                player['hits'] = row[3]
                players.append(player)
        return players
    except FileNotFoundError:
        return None

def write_players(players: list[dict]) -> None:
    """Write player list of dictionaries to players file."""
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list_dict_to_list_list(players))

def list_dict_to_list_list(players: list[dict]) -> list[list]:
    """Convert a list of dictionaries to a list of lists."""
    new_list: list = []
    for player in players:
        stats: list = []
        for stat in player.values():
            stats.append(stat)
        new_list.append(stats)
    return new_list