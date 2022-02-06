"""Playing card class."""

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        """Creates a card of given rank and suit."""
        self._rank: str = rank
        self._suit: str = suit.capitalize()
    
    def __repr__(self) -> str:
        """Provides card details."""
        return f'{self._rank} of {self._suit}'
    
    @property
    def rank(self) -> str:
        """GET the cards rank."""
        return self._rank
    
    @property
    def suit(self) -> str:
        """GET the cards suit."""
        return self._suit