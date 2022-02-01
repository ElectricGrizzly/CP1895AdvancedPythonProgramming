# 12-2: Bird Counter
Create a program for birdwatchers that stores a list of birds along with a count of the number of times each bird has been spotted.
## Console
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
## Specifications
- Use a dictionary to store the list of sighted birds and the count of the number of times each bird was sighted.
- Use the pickle module to read the dictionary from a file when the program starts and to write the dictionary to a file when the program ends. That way, the data that’s entered by the user isn’t lost.