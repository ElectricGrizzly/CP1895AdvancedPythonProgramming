"""Player class."""

class Player:
    def __init__(self, first_name: str, last_name: str, position: str, at_bats: str, hits: str) -> None:
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._position: str = position
        self._at_bats: str = at_bats
        self._hits: str = hits
    
    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def position(self) -> str:
        return self._position
    
    @position.setter
    def position(self, position: str) -> None:
        self._position: str = position
    
    @property
    def at_bats(self) -> str:
        return self._at_bats
    
    @at_bats.setter
    def at_bats(self, at_bats: str) -> None:
        self._at_bats: str = at_bats
    
    @property
    def hits(self) -> str:
        return self._hits
    
    @hits.setter
    def hits(self, hits: str) -> None:
        self._hits: str = hits

    @property
    def batting_avg(self) -> float:
        try:
            avg: float = int(self._hits) / int(self._at_bats)
            return round(avg, 3)
        except ZeroDivisionError:
            return 0.0
    
    @property
    def full_name(self) -> str:
        return f'{self._first_name} {self._last_name}'