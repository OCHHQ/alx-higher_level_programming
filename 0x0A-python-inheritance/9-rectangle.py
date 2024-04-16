#!/usr/bin/python3

class BaseGeometry:
    """
    Base class representing base geometry.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
        integer_validator(self, name, value): Validates the value to be an integer greater than 0.
    """
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.

        Args:
            name: A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle class representing a rectangle.

    Inherits from:
        BaseGeometry

    Methods:
        __init__(self, width, height): Initializes a rectangle with width and height.
        __str__(self): Returns the rectangle description.
        area(self): Computes and returns the area of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        Returns the rectangle description.

        Returns:
            A string representing the rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height
