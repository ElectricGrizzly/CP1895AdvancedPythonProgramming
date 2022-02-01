# 13-1: Greatest Common Divisor
Create a program that finds the greatest common divisor of two numbers.
## Console
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
## Specifications
- Use the following recursive algorithm to calculate the greatest common divisor (GCD):
```
divide x by y and get the remainder
if the remainder equals 0, GCD is y (end function)
otherwise, calculate GCD again by dividing y by remainder
```
- If number 1 is less than number 2, the program should display a message that indicates that number 1 must be greater than number 2 and give the user another chance to enter the numbers.
- Assume the user will enter valid data.