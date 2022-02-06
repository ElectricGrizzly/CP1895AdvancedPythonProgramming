"""Playing card deck class."""

from card import Card
import random

_RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
_SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class Deck:
    def __init__(self, ranks: list[str] = _RANKS, suits: list[str] = _SUITS) -> None:
        """Deck of cards of size ranks * suits. Defaults to standard 52 card deck with jokers omitted."""
        self._ranks = ranks
        self._suits = suits
        self._deck = [Card(rank, suit) for rank in ranks for suit in suits]
    
    def __repr__(self) -> str:
        """Provides remaining cards in deck, as well as the ranks and suits to deck consists of."""
        return f'Deck of {self.count} cards of...\nRanks: {self._ranks}\nSuits: {self._suits}'
    
    @property
    def count(self) -> int:
        """GET the number of cards in the deck."""
        return len(self._deck)
    
    def shuffle(self) -> None:
        """Shuffles the deck. Shuffles thrice for good measure."""
        for _ in range(3):
            random.shuffle(self._deck)
    
    def deal(self, amount: int) -> list[Card]:
        """Deals the number of cards from amount. Removes amount of cards from deck."""
        return [self._deck.pop() for _ in range(amount)]
