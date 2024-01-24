import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

dates = pd.date_range('20220226', periods=6)

df = pd.DataFrame(np.random.randn(6,5), index=dates, columns=['a','b','c','d','e'])

print(df)