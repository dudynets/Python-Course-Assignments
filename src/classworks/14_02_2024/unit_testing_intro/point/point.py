class Point:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("x must be of type int or float")
        self._x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("y must be of type int or float")
        self._y = value

    def move_by(self, x, y) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("x and y must be of type int or float")

        self._x += x
        self._y += y

    def move_to(self, x, y) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("x and y must be of type int or float")

        self._x = x
        self._y = y
