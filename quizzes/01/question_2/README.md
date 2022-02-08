# Question 2
Convert the program from question 1 from procedural to object-oriented. This shouldn’t change the functionality of the code much, but it should make the code more modular, reusable, and easier to maintain.
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

Menu option: 2
First name: Mike
Last name: Murach
Position: c
At bats: 0
Hits: 0
Mike Murach was added.

Menu option: 7

Bye!
```
## Specifications
- Use a Player class that provides attributes that store the first name, last name, position, at bats, and hits for a player. This class should also provide methods that return the player’s full name and batting average