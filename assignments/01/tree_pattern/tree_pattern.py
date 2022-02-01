"""Tree Pattern Program"""

def generate_tree(branch, symbol) -> None:
    """Generate a Tower of Hanoi pattern."""
    if branch == 0:
        return
    else:
        generate_tree(branch - 1, symbol)
        print(branch, (branch*5)*symbol)
        generate_tree(branch - 1, symbol)


def main(character: str) -> None:
    """Tree pattern main control."""
    print('Tree Pattern\n')
    branches: str = int(input('Enter the number of branches: '))
    print()
    generate_tree(branches, character)

if __name__ == '__main__':
    SYMBOL = '*'
    main(SYMBOL)