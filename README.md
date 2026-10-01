# big-integer-nth-root

Computes the integer floor of the kth root of an arbitrarily large non-negative integer.

## Usage

```python
from big_integer_nth_root import integer_nth_root

print(integer_nth_root(27, 3))       # 3
print(integer_nth_root(26, 3))       # 2
print(integer_nth_root(10**100, 10)) # 10000000000
```

## Why this library exists

Python's built-in `pow(n, 1/k)` converts to floating point and loses precision for large integers. The `math.isqrt` function handles square roots only. This library provides a general kth root using an integer-adapted Newton iteration that never leaves the integer domain.

The trade-off is that the algorithm uses repeated integer exponentiation (`x ** (k - 1)`), so for very large k it may be slower than a specialised method. In return, the code stays simple and correct for arbitrary-size inputs.

## Edge case

The function rejects negative `n` and non-positive `k` with `ValueError`. For `k == 1` it returns `n` unchanged. For `n == 0` or `n == 1` it returns `n` immediately. Non-integer inputs raise `TypeError` from Python's own arithmetic checks.

## Design notes

The window stores values eagerly rather than keeping running aggregates. Running
sums drift with floating point over long streams, and recomputing from a small
buffer is cheap enough that the drift is not worth the speed.

