# Shapes: Using Python `unittest`

Here is a simple example for using Python's `unittest`.


## Directory Structure

The directory structure of `shapes` is:

```text
[user@machine shapes]$ tree
.
├── README.md
├── src
│   ├── __init__.py
│   ├── misc
│   │   ├── __init__.py
│   │   └── something.py
│   ├── shapes.py
│   └── sphere.py
└── tests
    ├── __init__.py
    └── test_shapes.py
```

Note that the two empty files `src/__init__.py` and `tests/__init__.py` are important.


## The Original Code

The file `src/shapes.py` contains functions `rectangle_area(w, h)` and `rectangle_volume(w, h, d)` to calculate, respectively, the area and the volume of rectangles. We want to ensure that the results returned by these functions is correct, and that they will properly fail if they are not supplied with the correct number of parameters.


## The Tests

Our test file is `tests/test_shapes.py`. All files in `tests/` should be named `test_*.py`. We can import the functions found in `src/shapes.py` with `import src.shapes`.

All `tests/test_*.py` files should look like:

```python
import unittest

class TestSomething(unittest.TestCase):

    def test_first_thing(self):
        # Test the first thing here
        
    def test_second_thing(self):
        # Test the second thing here
```


## Imports Examples

Take a look at the imports found in `src/shapes.py` and `tests/test_shapes.py` to see how imports work in the context of `unittest`.


# Running the Tests

To run the tests, simply do:

```bash
[user@machine shapes]$ python -m unittest
```
