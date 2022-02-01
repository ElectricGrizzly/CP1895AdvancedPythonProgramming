"""Greatest Common Divisor Program"""

def find_gcd(number1: int, number2: int) -> int:
    """Returns the greatest common divisor of number1 and number2."""
    remainder: int = number1 % number2
    return number2 if remainder == 0 else find_gcd(number2, remainder)

def gcd_splash() -> None:
    """GCD start or splash."""
    print('Greatest Common Divisor')

def gcd_loop() -> None:
    """Primary loop of GCD program."""
    continue_char: str = 'y'
    while continue_char != 'n':
        print()
        integer1: int = int(input('Number 1: '))
        integer2: int = int(input('Number 2: '))
        if integer1 < integer2:
            print('\nNumber 1 must be greater than number 2!')
        else:
            gcd: int = find_gcd(integer1, integer2)
            print('Greatest common divisor:', gcd)
        continue_char: str = input('\nContinue? (y/n): ')
    print('\nBye!')

def main() -> None:
    """Greatest Common Divisor (GCD) main control function."""
    gcd_splash()
    gcd_loop()

if __name__ == '__main__':
    main()