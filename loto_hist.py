
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

from pandas import Series, DataFrame

# Can open csv files as a dataframe

dframe = pd.read_csv('lotto-draw-history.csv')

# Show
# print(dframe)

arr1 = np.array(dframe)

arr_num = arr1[:, 1:6]  # seleciona parcialmente um array [startline:lastline,startcolumn:lastcolumn]
arr_play = arr1[:,6:7]  # seleciona parcialmente um array - somente os numeros do play

unique_elements, counts_elements = np.unique(arr_num, return_counts=True)

print(unique_elements)
print(counts_elements)


plt.hist(unique_elements, bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
# plt.hist(unique_elements)
plt.title("Histogram - tst")
plt.show()
