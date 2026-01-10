"""Class representing a N-dimensional vector with basic operations."""

from typing import List, Tuple


class Vector:
    """A class to represent a N-dimensional vector."""

    def __init__(self, components: List[float]):
        self._components = tuple(components)
        self._magnitude = None

    @property
    def components(self) -> Tuple[float, ...]:
        """Get the components of the vector as a tuple."""
        return self._components

    @property
    def magnitude(self) -> float:
        """Compute and return the magnitude of the vector."""
        if self._magnitude is None:
            self._magnitude = sum(a**2 for a in self._components) ** 0.5
        return self._magnitude

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot add Vector with {type(other).__name__}")
        if len(self._components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add.")
        return Vector([a + b for a, b in zip(self._components, other.components)])

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot subtract Vector with {type(other).__name__}")
        if len(self._components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to subtract.")
        return Vector([a - b for a, b in zip(self._components, other.components)])

    def dot(self, other: "Vector") -> float:
        """Compute the dot product of this vector with another vector."""
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot compute dot product with {type(other).__name__}")
        if len(self._components) != len(other.components):
            raise ValueError(
                "Vectors must be of the same dimension to compute dot product."
            )
        return sum(a * b for a, b in zip(self._components, other.components))

    def __repr__(self) -> str:
        return f"Vector({self._components})"


# Example usage:
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 . v2:", v1.dot(v2))
    print("|v1|:", v1.magnitude)
    print("|v2|:", v2.magnitude)
