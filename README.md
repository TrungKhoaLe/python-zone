# PYTHON ZONE

This is a place where I document confusing concepts that I have met during my journey in the
software industry with Python.

## 1. POSITIONAL ONLY ARGUMENT "/"

It indicates that parameters before the "/" can only be passed positionally
and cannot be passed using keyword arguments.

e.g.

```python
def example_func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

example_func(1, 2, 3, 4, e=5, f=6)
```
