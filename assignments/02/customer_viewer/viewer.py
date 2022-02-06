"""CSV Customer Viewer program."""

from customer import Customer
from csv import reader

def display_splash() -> None:
    """Display program start/splash screen."""
    print('Customer Viewer\n')

def display_exit() -> None:
    """Display program exit/quit screen."""
    print('Bye!')

def customers_from_file(file: str) -> list[Customer]:
    """Create a list of Customer objects from given customer CSV file."""
    customer_list: list[Customer] = []
    with open(file, 'r', encoding='utf-8') as customer_csv:
        customers = reader(customer_csv)
        next(customers) # Skip the headers of CSV
        for customer in customers:
            id: str = customer[0]
            first_name: str = customer[1]
            last_name: str = customer[2]
            company: str = customer[3]
            street: str = customer[4]
            city: str = customer[5]
            state: str = customer[6]
            zip: str = customer[7]
            customer_list.append(Customer(id, first_name, last_name, company, street, city, state, zip))
    return customer_list

def display_customer(customers: list[Customer], id: str) -> None:
    """Display the customer address as selected from ID."""
    print()
    for customer in customers:
        if customer.id == id:
            print(customer.address)
            print()
            return
    print('No customer with that ID.\n')

def viewer(customers: list[Customer]) -> None:
    """Show the customer details of selected customer by ID. Continue until user enters 'n'."""
    continue_character: str = 'y'
    while continue_character != 'n':
        customer_id = input('Enter customer ID: ')
        display_customer(customers, customer_id)
        continue_character: str = input('Continue? (y/n): ').lower()
        print()

def main() -> None:
    """Control of Customer Viewer."""
    CUSTOMER_FILE = 'customers.csv'
    display_splash()
    customers = customers_from_file(CUSTOMER_FILE)
    viewer(customers)
    display_exit()

if __name__ == '__main__':
    main()