import copy
import time
from typing import Any
from main import zero_line
from main import det_minor
matrix = [[3, -3, -5, 8],
                  [-3, 2, 4, -6],
                  [2, -5, -7, 5],
                  [-4, 3, 5, -6]]
print(det_minor(matrix))
