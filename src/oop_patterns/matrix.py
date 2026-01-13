"""Class representing a matrix with basic operations."""

from typing import List


class Matrix:
    """A class to represent a mathematical matrix and perform basic operations."""

    def __init__(self, data: List[List[float]]):
        """Initialize the matrix with a 2D list."""
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same number of columns.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other: "Matrix"):
        """A method to add two matrices."""
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot add Matrix with {type(other).__name__}")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add.")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other: "Matrix"):
        """A method to subtract two matrices."""
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot subtract Matrix with {type(other).__name__}")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract.")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __repr__(self) -> str:
        """Return a string representation of the matrix."""
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __str__(self) -> str:
        """Return a user-friendly string representation of the matrix."""
        return "\n".join(["[" + " ,".join(map(str, row)) + "]" for row in self.data])


if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    B = Matrix([[7, 8, 9], [10, 11, 12]])

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    print("A + B:\n", A + B)
    print("A - B:\n", A - B)

    print("A repr:\n", repr(A))
    print("B repr:\n", repr(B))
