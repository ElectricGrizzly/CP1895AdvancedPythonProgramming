"""Customer class."""

class Customer:
    def __init__(self, id: str, first_name: str, last_name: str, company: str, street: str, city: str, state: str, zip: str) -> None:
        """Create a customer from given ID, name, company, and address components. Company can be empty string."""
        self._id: str = id
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._street: str = street
        self._city: str = city
        self._state: str = state
        self._zip: str = zip
        if company == '':
            self._company = None
        else:
            self._company: str = company
    
    def __repr__(self) -> str:
        """Show the customer ID and address."""
        return self.id + '\n' + self.address
    
    @property
    def id(self) -> str:
        """GET the customer ID."""
        return self._id
    
    @property
    def first_name(self) -> str:
        """GET the customer first name."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """GET the customer last name."""
        return self._last_name

    @property
    def street(self) -> str:
        """GET the customer street address."""
        return self._street
    
    @property
    def city(self) -> str:
        """GET the customer city."""
        return self._city
    
    @property
    def state(self) -> str:
        """GET the customer state."""
        return self._state
    
    @property
    def zip(self) -> str:
        """GET the customer zip."""
        return self._zip
    
    @property
    def company(self) -> str | None:
        """GET the customer company."""
        return self._company
    
    @property
    def address(self) -> str:
        """GET the customer address."""
        address: str = f'{self._first_name} {self._last_name}\n{self._street}\n{self._city}, {self._state} {self._zip}'
        if self._company is None:
            return address  
        else:
            post_name_index: int = address.find('\n')
            return address[:post_name_index] + '\n' + self._company + address[post_name_index:]