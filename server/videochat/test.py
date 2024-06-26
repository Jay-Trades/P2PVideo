import pandas as pd
import numpy as np
from collections import deq



mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.Series(mydataset)
df_1 = pd.DataFrame(mydataset, index = ["car1", "car2", "car3"])

print(df_1)
print("------")
print(df_1.iloc[1:])