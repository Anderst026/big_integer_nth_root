"""Core implementation of integer nth root.

The algorithm uses an integer-adapted Newton iteration. For k >= 1 we
start from an initial estimate and refine until the result stops
changing. The update step is

    x_{n+1} = ((k - 1) * x_n + n // x_n ** (k - 1)) // k

which is the standard Newton step for solving x**k - n = 0, converted
to floor division so that every intermediate value is an integer.

For k == 1 the root is n itself. For k == 2 this reduces to the
well-known integer square root iteration. We use bit_length to get a
reasonable starting estimate that never overflows and is never less
than the true root.
"""

from __future__ import annotations


def integer_nth_root(n: int, k: int) -> int:
    """Return the largest integer r such that r ** k <= n.

    Args:
        n: Non-negative integer whose root is desired.
        k: Positive integer degree of the root.

    Returns:
        The floor of the kth root of n.

    Raises:
        ValueError: If k is less than 1 or n is negative.

    Examples:
        >>> integer_nth_root(27, 3)
        3
        >>> integer_nth_root(26, 3)
        2
        >>> integer_nth_root(10**100, 10)
        10000000000
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k < 1:
        raise ValueError("k must be a positive integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return n
    if k == 1:
        return n

    # Initial estimate. Using bit_length gives a tight upper bound and
    # avoids floating-point imprecision for very large integers. The
    # expression is equivalent to ceil(n.bit_length() / k) without
    # importing math.
    shift = (n.bit_length() + k - 1) // k
    x = 1 << shift

    while True:
        # Newton update for f(x) = x**k - n.
        y = ((k - 1) * x + n // x ** (k - 1)) // k
        if y >= x:
            break
        x = y

    # Correct any overshoot from the initial high estimate.
    while x ** k > n:
        x -= 1
    return x
