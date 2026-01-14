"""Unit tests for the Vector class in oop_patterns.vector module."""

import pytest

from src.oop_patterns.vector import Vector


def test_components_are_tuples():
    """Test that the components of the vector are stored as a tuple."""
    v = Vector([1, 2, 3])
    assert isinstance(v.components, tuple)
    assert v.components == (1, 2, 3)


def test_components_immutable():
    """Test that the components of the vector are immutable."""
    v = Vector([1, 2, 3])
    components = v.components
    with pytest.raises(TypeError):
        components[0] = 10  # type: ignore[index]


def test_magnitude():
    """Test the magnitude property of the vector."""
    v = Vector([3, 4])
    assert v.magnitude == 5.0


def test_unit_vector():
    """Test the unit_vector property of the vector."""
    v = Vector([3, 4])
    unit_v = v.unit_vector
    expected_unit_v = Vector([0.6, 0.8])
    assert unit_v == expected_unit_v
    assert pytest.approx(unit_v.magnitude) == 1.0


def test_vector_addition():
    """Test the addition of two vectors."""
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1 + v2
    assert result.components == (5, 7, 9)


def test_vector_subtraction():
    """Test the subtraction of two vectors."""
    v1 = Vector([4, 5, 6])
    v2 = Vector([1, 2, 3])
    result = v1 - v2
    assert result.components == (3, 3, 3)


def test_dot_product():
    """Test the dot product of two vectors."""
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1.dot(v2)
    assert result == 32  # 1*4 + 2*5 + 3*6


def test_vector_length():
    """Test the length of the vector using len()."""
    v = Vector([1, 2, 3, 4])
    assert len(v) == 4


def test_vector_equality_and_hashing():
    """Test equality and hashing of vectors."""
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    v3 = Vector([4, 5, 6])

    assert v1 == v2
    assert v1 != v3
    assert hash(v1) == hash(v2)
    assert hash(v1) != hash(v3)


def test_dimension_mismatch_addition():
    """Test that adding vectors of different dimensions raises ValueError."""
    v1 = Vector([1, 2])
    v2 = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        _ = v1 + v2
