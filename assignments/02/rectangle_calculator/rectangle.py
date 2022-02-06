"""Rectangle class."""

class Rectangle:
    def __init__(self, height: int, width: int) -> None:
        """Create a rectangle of given height and width."""
        self._height: int = height
        self._width: int = width

    def __repr__(self) -> str:
        """Representation of rectangle as '*' of given height and width separated with spaces."""
        _horizontal: str = '* ' * (self._width - 1) + '*\n'
        _vertical: str = '*' + ' ' * ((self._width * 2) - 3) + '*\n'
        return _horizontal + (self._height - 2) * _vertical + _horizontal
    
    @property
    def perimeter(self) -> int:
        """GET perimeter from height and width."""
        return 2 * (self._height + self._width)
    
    @property
    def area(self) -> int:
        """GET area from height and width."""
        return self._height * self._width