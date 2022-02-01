# 12-4: Monthly Sales
Create a program that allows you to view and edit the sales amounts for each month of the current year.
## Console
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
## Specifications
- Download the text file named monthly_sales.txt that consists of rows that contain three-letter abbreviations for the month and the monthly sales.
- The program should read the file and store the sales data for each month in a dictionary with the month abbreviation as the key for each item.
- Whenever the sales data is edited, the program should write the changed data to the text file.