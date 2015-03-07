"""
File: array_row_major.py

A 2-D Array mapped onto a 1-D array using row-major ordering.

Since __setitem__ and __getitem__ don't work properly for multiple
dimensions, we use setitem(r,c,v) and getitem(r,c) to simulate them.

To instantiate, use

<variable> = Array2D(<rows>, <columns>)

"""

class Array2D(object):
    """Represents a 2D array in row-major order."""

    def __init__(self, rows, cols):
        """fillValue is placed at each position."""
        self._items = list()
        self._width = cols
        self._height = rows
        for count in range(rows * cols):
            self._items.append(count)
    
    def width(self):
        return self._width
    
    def height(self):
        return self._height

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def getitem(self, r, c):
        """Subscript operator for access at index."""
        return self._items[r * self.width() + c]

    def setitem(self, r, c, newItem):
        """Subscript operator for replacement at index."""
        self._items[r * self.width() + c] = newItem

def main():
    a = Array2D(2,3)
    print("a is: " + str(a))

    # Get the value at a[1][1]
    print(a.getitem(1,1))

    # Set the value at a[1][2] = 7
    a.setitem(1,2,7)
    
    # Print the value at a[1][2]
    print(a.getitem(1,2))

    print("a is now: " + str(a))
    

main()


