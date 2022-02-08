# Question 1
A program, baseball_team, has been written for a baseball team. This program
- displays a welcome message and calculates a player’s batting average
- select options from a menu
- has functions to organize the code
- has error handling
- uses a list of lists to store each player in the lineup
- saves the data to a file
- formats the numbers and the strings
- displays the current date, gets the date of the game from the user, and displaying the number of days until the game
Your task is to update the program so it uses a dictionary to store the data for each player (name,position, at_bats, hits). This shouldn’t change the functionality of the program, but it should improve the readability of the code.
## Console
```
=================================================================
Baseball Team Manager
CURRENT DATE: 2016-12-19
GAME DATE:
MENU OPTIONS
1 – Display lineup
2 – Add player
3 – Remove player
4 – Move player
5 – Edit player position
6 – Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P
=================================================================

Menu option: 1
Player POS AB H AVG
-----------------------------------------------------------------
1  Denard Span                            CF   545   174   0.319
2  Brandon Belt                           1B   533   127   0.238
3  Buster Posey                            C   535   176   0.329
4  Hunter Pence                           RF   485   174   0.359
5  Brandon Crawford                       SS   532   125   0.235
6  Eduardo Nunez                          3B   477   122   0.256
7  Joe Panik                              2B   475   138   0.291
8  Jarrett Parker                         LF   215    58   0.270
9  Madison Bumgarner                       P   103    21   0.204

Menu option: 7

Bye!
```
## Specifications
- Download the zipped file baseball Quiz 1
- Use the baseball_team file to update the program as specified
- Use a dictionary to store the data for each player.
- The csv module only works with a list of lists, not a list of dictionaries. To work around this, you can modify the functions that read and write the data to the file so they work correctly with a list of dictionaries.