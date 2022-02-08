"""Baseball Team Manager Program."""

import db
from datetime import datetime
from player import Player

POSITIONS: tuple = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def add_player(players: list[Player]) -> None:
    """Add a player object to player list."""
    first_name: str = input('First name: ')
    last_name: str = input('Last Name: ')
    position: str = get_player_position()
    at_bats: str = get_at_bats()
    hits: str = get_hits()
    
    player = Player(first_name, last_name, position, at_bats, hits)
    players.append(player)
    db.write_players(players)
    print(player.full_name + " was added.\n")

def get_player_position() -> str:
    """Get the desired position and confirm position is valid."""
    while True:
        position: str = input("Position: ")
        position: str = position.upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_positions()

def get_at_bats() -> str:
    """Get the number of at bats and confirm it is a valid integer."""
    while True:
        try:
            at_bats: int = int(input("At bats: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if at_bats >= 0 and at_bats <= 10000:
            return str(at_bats)
        else:
            print("Invalid entry. Must be from 0 to 10,000.")            

def get_hits() -> str:
    """Get the number of hits and confirm it is a valid integer."""
    while True:
        try:
            hits: int = int(input("Hits: "))
        except ValueError:
            print("Invalid integer. Try again.")
            continue

        if hits >= 0 and hits <= 10000:        
            return str(hits)
        else:
            print("Invalid entry. Must be from 0 to 10,000.")                                       

def get_lineup_number(players: list[dict], prompt: str) -> int:
    """Get the player by lineup number and confirm it is a valid lineup number."""
    while True:
        try:
            number: int = int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(players):
            print("Invalid player number. " +
                  "Please try again.")
        else:
            break

    return number

def delete_player(players: list[Player]) -> None:
    """Delete the desired player dictionary from the players list."""
    number: int = get_lineup_number(players, "Number: ")
    player: Player = players.pop(number-1)
    db.write_players(players)
    print(player.full_name + " was deleted.\n")

def move_player(players: list[dict]) -> None:
    """Move the selected player to the desired lineup location."""
    old_number: int = get_lineup_number(players, "Current lineup number: ")
    player: Player = players[old_number-1]
    print(player.full_name + " was selected.")
    new_number: int = get_lineup_number(players, "New lineup number: ")
    players.pop(old_number-1)
    players.insert(new_number-1, player)
    db.write_players(players)
    print(player.full_name + " was moved.\n")

def edit_player_position(players: list[dict]) -> None:
    """Edit the selected players position."""
    number: int = get_lineup_number(players, "Lineup number: ")
    player: Player = players[number-1]
    print("You selected " + player.full_name + " POS=" + player.position)
    position: str = get_player_position()
    player.position = position
    db.write_players(players)
    print(player.full_name + " was updated.\n")

def edit_player_stats(players: list[dict]) -> None:
    """Edit the selected players statistics."""
    number: int = get_lineup_number(players, "Lineup number: ")
    player: Player = players[number-1]
    print("You selected " + player.full_name +
          " AB=" + player.at_bats +
          " H=" + player.hits)
    at_bats: str = get_at_bats()
    hits: str = get_hits()
    player.at_bats = at_bats
    player.hits = hits
    db.write_players(players)
    print(player.full_name + " was updated.\n")

def display_lineup(players: list[Player]) -> None:
    """Display the player lineup with player statistics."""
    if players == None:
        print("There are currently no players in the lineup.")        
    else:
        header: str = "{:3}{:35}{:>6}{:>6}{:>6}{:>8}"
        line: str = "{:<3d}{:35}{:>6}{:>6}{:>6}{:8.3f}"
        print(header.format("", "Player", "POS", "AB", "H", "AVG"))
        print("-" * 64)
        i = 1
        for player in players:
            print(line.format(i, player.full_name, player.position,
                            player.at_bats, player.hits, player.batting_avg))
            i += 1
    print()    

def get_batting_avg(at_bats: str | int, hits: str | int) -> float:
    """Get the batting average from given at bats and hits."""
    try:
        avg: float = int(hits) / int(at_bats)
        return round(avg, 3)
    except ZeroDivisionError:
        return 0.0

def display_separator():
    """Display a horizontal separator"""
    print("=" * 64)

def display_title():
    """Display the program title."""
    print("                   Baseball Team Manager")

def display_dates():
    """Display the game dates."""
    print()

    now = datetime.now()    
    current_date = datetime(now.year, now.month, now.day)
    print("CURRENT DATE:    " + current_date.strftime("%Y-%m-%d"))

    game_date_str: str = input("GAME DATE:       ")
    if game_date_str == "":
        print()
        return
    game_date = datetime.strptime(game_date_str, "%Y-%m-%d")
    time_span = game_date - current_date

    if time_span.days > -1:
        print("DAYS UNTIL GAME: " + str(time_span.days))
    print()    

def display_menu():
    """Display available menu options."""
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print()

def display_positions():
    """Display available possible team positions."""
    print("POSITIONS")
    print(", ".join(POSITIONS))

def main() -> None:
    """Control of baseball team manager program."""
    display_separator()
    display_title()
    display_dates()
    display_menu()
    display_positions()

    players: list[dict] = db.read_players()
    if players == None:
        print()
        print("Team data file could not be found.")
        print("You can create a new one if you want.")
        players: list = []        
    
    display_separator()
    
    while True:
        try:
            option: int = int(input("Menu option: "))
        except ValueError:
            print("Not a valid option. Please try again.\n")
            display_menu()
            continue
            
        if option == 1:
            display_lineup(players)
        elif option == 2:
            add_player(players)
        elif option == 3:
            delete_player(players)
        elif option == 4:
            move_player(players)
        elif option == 5:
            edit_player_position(players)
        elif option == 6:
            edit_player_stats(players)
        elif option == 7:
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()
