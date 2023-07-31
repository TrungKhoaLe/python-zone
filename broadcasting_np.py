import numpy as np
import math

img = np.random.randint(0, 10, (2, 2, 3)) # a random image with 2 rows, 2 columns and 3 channels
scale_values = np.array([1, 2, 3])

"""
Broadcasting steps:
    1. Dimensions of arrays;
        img.shape = (2, 2, 3), having three dimentions
        scale_values.shape = (3,), having one dimension

    2. Broadcasting rule:
        Broadcasting is possible when the dimensions (ranks or the number of
        axes of an array) are either equal or one of them has a dimension of
        size 1.
    3. Broadcasting process:
        To perform broadcasting, NumPy will compare the dimensions of the two
        arrays element-wise from right to left (trailing dimensions). It will 
        try to match or extend the dimensions until both arrays have the same 
        number of dimensions.

        Since img has three dimensions and scale_values has one dimension,
        NumPy will add new dimension to scale_values with sizes of 1 to make it
        compatible with img. These new dimensions will be added to the front of
        scale_values, resulting in the shape (1, 1, 3).

        Now, the two arrays have the same number of dimensions (3), and their
        shapes are (2, 2, 3) and (1, 1, 3).

        After broadcasting, NumPy will perform element-wise operations between
        the two arrays, matching the dimensions based on broadcasting rules.
        The final result's shape will be (2, 2, 3).
"""

result = img * scale_values

assert result.shape == (2, 2, 3)
