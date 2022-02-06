"""Rectangle Calculator Program."""

from rectangle import Rectangle

def display_splash() -> None:
    """Display program start/splash screen."""
    print('Rectangle Calculator\n')

def display_exit() -> None:
    """Display program exit/quit screen."""
    print('Bye!')

def display_results(rectangle: Rectangle) -> None:
    """Display the perimeter, area, and representation of Rectangle object."""
    print(f'Perimeter:\t{rectangle.perimeter}')
    print(f'Area:\t\t{rectangle.area}')
    print(rectangle)

def calculator() -> None:
    """Create Rectangle object from user height and width, then display results. Continue until user enters 'n'."""
    continue_character: str = 'y'
    while continue_character != 'n':
        height: int = int(input('Height:\t\t'))
        width: int = int(input('Width:\t\t'))
        rectangle: Rectangle = Rectangle(height, width)
        display_results(rectangle)
        continue_character: str = input('Continue? (y/n): ').lower()
        print()

def main() -> None:
    """Control of Rectangle Calculator."""
    display_splash()
    calculator()
    display_exit()

if __name__ == '__main__':
    main()