# 13-2: Tree Pattern
Create a program that uses tree recursion to print a pattern like the one shown below.
## Console
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
## Specifications
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