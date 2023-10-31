#!/usr/bin/python3
"""Import NumPy module."""

import numpy as np

"""Multiply two matrices using NumPy."""


def lazy_matrix_mul(m_a, m_b):
    try:
        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)
        result = np.matmul(matrix_a, matrix_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a or m_b can't be empty")
    except TypeError:
        raise TypeError("m_a and m_b must be lists of lists of integers or floats")
    except Exception:
        raise TypeError("m_a and m_b can't be multiplied")
