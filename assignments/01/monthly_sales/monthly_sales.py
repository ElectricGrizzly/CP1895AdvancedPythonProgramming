"""Monthly Sales Program"""

def display_options() -> None:
    """Display the programs available options."""
    print('COMMAND MENU')
    print('view\t- View sales for specified month')
    print('edit\t- Edit sales for specified month')
    print('totals\t- View sales summary for year')
    print('exit\t- Exit program')
    print()

def read_sales_data(file: str) -> dict:
    """Return a dictionary from file."""
    with open(file, 'r', encoding='utf-8') as sales_file:
        sales: list[str] = sales_file.readlines()
        return dict([sale.split() for sale in sales])

def to_formatted_list(dictionary: dict) -> list:
    """Returns a list from the given dictionary."""
    return [f'{key}\t{int(dictionary[key])}\n' for key in dictionary.keys()]

def write_sales_data(file: str, data: dict) -> None:
    """Write given data to file."""
    data: list = to_formatted_list(data)
    with open(file, 'w', encoding='utf-8') as sales_file:
        sales_file.writelines(data)

def cmd_view(sales_data: dict) -> None:
    """Provide user with "view" command option."""
    try:
        month: str = input('Three-letter Month: ').capitalize() 
        month_data: float = float(sales_data[month])
        print(f'Sales amount for {month.capitalize()} is {to_money(month_data)}.')
    except KeyError as e:
        print('Invalid three-letter month.')

def to_money(money_value: float) -> str:
    """Returns the float as a string formatted like money."""
    return '{:,.2f}'.format(money_value)

def cmd_edit(sales_data: dict, sales_file: str) -> None:
    """Provide user with "edit" command option."""
    try:
        month: str = input('Three-letter Month: ').capitalize()
        if month not in sales_data.keys(): raise KeyError
        new_sales_amount: float = float(input('Sales Amount: '))
        sales_data[month] = new_sales_amount
        write_sales_data(sales_file, sales_data)
        print(f'Sales amount for {month.capitalize()} is {to_money(new_sales_amount)}.')
    except KeyError as e:
        print('Invalid three-letter month.')

def cmd_totals(sales_data: dict) -> None:
    """Provide user with "totals" command option."""
    total: float = 0
    average: float = 0
    for sale in sales_data.keys():
        sale_amount: float = float(sales_data[sale])
        total += sale_amount
    average: float = total / len(sales_data)
    print(f'Yearly total:\t\t{to_money(total)}')
    print(f'Monthly average:\t{to_money(average)}')

def monthly_sales_splash() -> None:
    """Display monthly sales splash."""
    print('Monthly Sales Program\n')
    display_options()

def main(sales_file: str) -> None:
    """Monthly sales main control function."""
    monthly_sales_splash()
    sales_data: dict = read_sales_data(sales_file)
    command: str = ''
    while command != 'exit':
        command: str = input('Command: ').lower()
        if command == 'view': cmd_view(sales_data)
        elif command == 'edit': cmd_edit(sales_data, sales_file)
        elif command == 'totals': cmd_totals(sales_data)
        print()
    print('Bye!')

if __name__ == '__main__':
    SALES_FILE = 'monthly_sales.txt'
    main(SALES_FILE)