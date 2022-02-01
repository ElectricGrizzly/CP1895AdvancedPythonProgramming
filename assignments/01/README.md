# Assignment 1
## 12-1: Game Stats
Create a program that allows you to view the statistics for a player of a game.
### Console
```
Game Stats Program

ALL PLAYERS:
Elizabeth
Joel
Mike

Enter a player name: elizabeth
Wins:    41
Losses:  3
Ties:    22

Continue? (y/n): y

Enter a player name: john
There is no player named John.

Continue? (y/n): y

Enter a player name: joel
Wins:    32
Losses:  14
Ties:    17

Continue? (y/n): y

Enter a player name: mike
Wins:    8
Losses:  19
Ties:    11

Continue? (y/n): n

Bye!
```
### Specifications
- The program should use a dictionary of dictionaries to store the stats (wins, losses, and ties) for each player. You can code this dictionary of dictionaries at the beginning of the program using any names and statistics that you want. Make sure to provide stats for at least three players.
- The program should begin by displaying an alphabetical list of the names of the players.
- The program should allow the user to view the stats for the specified player.
---
## 12-2: Bird Counter
Create a program for birdwatchers that stores a list of birds along with a count of the number of times each bird has been spotted.
### Console
```
Bird Counter Program

Enter 'x' to exit

Enter name of bird: red-tailed hawk
Enter name of bird: killdeer
Enter name of bird: snowy plover
Enter name of bird: western gull
Enter name of bird: killdeer
Enter name of bird: western gull
Enter name of bird: x

Name            Count
=============== ===============
Killdeer        2
Red-Tailed Hawk 1
Snowy Plover    1
Western Gull    2
```
### Specifications
- Use a dictionary to store the list of sighted birds and the count of the number of times each bird was sighted.
- Use the pickle module to read the dictionary from a file when the program starts and to write the dictionary to a file when the program ends. That way, the data that’s entered by the user isn’t lost.
---
## 12-4: Monthly Sales
Create a program that allows you to view and edit the sales amounts for each month of the current year.
### Console
```
Monthy Sales Program

COMMAND MENU
view    - View sales for specified month
edit    - Edit sales for specified month
totals  - View sales summary for year
exit    - Exit program

Command: view
Three-letter Month: jan
Sales amount for Jan is 14,317.00

Command: edit
Three-letter Month: jan
Sales Amount: 15293
Sales amount for Jan is 15,293.00

Command: totals
Yearly total:    67,855.00
Monthly average:  5,654.58

Command: view
Three-letter Month: july
Invalid three-letter month.

Command: exit
Bye!
```
### Specifications
- Download the text file named monthly_sales.txt that consists of rows that contain three-letter abbreviations for the month and the monthly sales.
- The program should read the file and store the sales data for each month in a dictionary with the month abbreviation as the key for each item.
- Whenever the sales data is edited, the program should write the changed data to the text file.
---
## 13-1: Greatest Common Divisor
Create a program that finds the greatest common divisor of two numbers.
### Console
```
Greatest Common Divisor

Number 1: 15
Number 2: 5
Greatest common divisor: 5

Continue? (y/n): y

Number 1: 15
Number 2: 6
Greatest common divisor: 3

Continue? (y/n): y

Number 1: 15
Number 2: 7
Greatest common divisor: 1

Continue? (y/n): n

Bye!
```
### Specifications
- Use the following recursive algorithm to calculate the greatest common divisor (GCD):
```
divide x by y and get the remainder
if the remainder equals 0, GCD is y (end function)
otherwise, calculate GCD again by dividing y by remainder
```
- If number 1 is less than number 2, the program should display a message that indicates that number 1 must be greater than number 2 and give the user another chance to enter the numbers.
- Assume the user will enter valid data.
---
## 13-2: Tree Pattern
Create a program that uses tree recursion to print a pattern like the one shown below.
### Console
```
Tree Pattern

Enter the number of branches: 5

1 *****
2 **********
1 *****
3 ***************
1 *****
2 **********
1 *****
4 ********************
1 *****
2 **********
1 *****
3 ***************
1 *****
2 **********
1 *****
5 *************************
1 *****
2 **********
1 *****
3 ***************
1 *****
2 **********
1 *****
4 ********************
1 *****
2 **********
1 *****
3 ***************
1 *****
2 **********
1 *****
```
### Specifications
- The program can only accept a positive number of branches in the tree. Since the number of branches increases exponentially, this program will take a long time to execute for numbers larger than 12 or so.
- Use the following recursive algorithm to generate the pattern shown above:
```dotnetcli
if number = 0, end function
otherwise,
start branch for number - 1
print number and its visual representation
start branch for number - 1
```
- To get the visual representation for a branch, you can multiply the asterisk (*) by 5. In other words, 1 is 5 asterisks, 2 is 10 asterisks, and so on.