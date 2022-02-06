"""Card Dealer Program."""

from deck import Deck

def display_splash() -> None:
    """Display program start/splash screen."""
    print('Card Dealer\n')

def shuffle(deck: Deck) -> None:
    """Shuffle the given deck of cards and report the deck size."""
    if deck.count == 1:
        print('There is only one card remaining.')
        deck.shuffle()
    elif deck.count < 1:
        print('All cards have been dealt. No cards to shuffle.')
    else:
        deck.shuffle()
        print(f'I have shuffled a deck of {deck.count} cards.')
    print()

def deal(deck: Deck, amount: int = 1) -> None:
    """Deal the amount of cards from the deck."""
    print('Here are your cards:')
    dealt_cards: list = deck.deal(amount)
    for card in dealt_cards:
        print(card)
    print()

def display_remaining(deck: Deck) -> None:
    """Display the count of the remaining cards in the deck."""
    print(f'There are {deck.count} cards left in the deck.')
    print()

def display_well_wishes() -> None:
    """Display well wishes to the user."""
    print('Good luck!')
    print()

def display_exit() -> None:
    """Display program exit/quit screen."""
    print('Bye!')

def dealer() -> None:
    """Create a Deck object, deal the selected amount of cards and report deck statistics to user. Conintue until user enters 'n'."""
    continue_character: str = 'y'
    deck: Deck = Deck()
    shuffle(deck)
    while continue_character != 'n':
        cards_to_deal: int  = int(input('How many cards would you like?: '))
        print()
        deal(deck, cards_to_deal)
        display_remaining(deck)
        display_well_wishes()
        continue_character: str = input('Continue? (y/n): ').lower()
        print()

def main() -> None:
    """Control of Card Dealer."""
    display_splash()
    dealer()
    display_exit()

if __name__ == '__main__':
    main()