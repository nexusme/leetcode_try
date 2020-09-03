import numpy as np
import pandas as pd

num = [1, 20, 33, 3, 2, 1, 1, 66, 2, 3, 3, 4]
edge = [1, 2, 3, 4, 5, 999]
status = ['1', '2', '3', '4', '5+']

result = pd.cut(pd.Series(num), edge, labels=status, right=False).value_counts()
for index, value in result.items():
    print(index, value)
