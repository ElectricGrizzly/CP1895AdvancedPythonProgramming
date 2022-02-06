# 14-3: Customer Viewer
Create an object-oriented program that reads a list of Customer objects from a CSV file and allows the user to enter the data for a customer by specifying the customer’s ID.
## Console
```
Customer Viewer

Enter customer ID: 103

Art Venere
8 W Cerritos Ave #54
Bridgeport, NJ 08014

Continue? (y/n): y

Enter customer ID: 104

Lenna Paproki
Feltz Printing
639 Main St
Anchorage, AK 99501

Continue? (y/n): y

Enter customer ID: 99

No customer with that ID.

Continue? (y/n): n

Bye!
```
## Specifications
1. Your instructor should provide a CSV file named customers.csv that contains customer data.
2. Use a Customer class to store the customer data. This class should include these attributes: id, firstName, lastName, company, address, city, state, zip.
3. In addition, this class should include a property or method that returns the full address. This address should have three lines if the company attribute is empty or four lines if the company attribute is not empty.
4. Create a function that reads the customer data from a CSV file and creates Customer objects from it.
5. To find the customer with the specified ID, you need to loop through each Customer object in the list of Customer objects and check whether the specified ID matches the ID stored in the Customer object.
6. If the specified ID isn’t found, display an appropriate message.