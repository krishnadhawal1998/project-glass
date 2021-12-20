import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


glass=pd.read_csv("dataset\\glass.csv")

#Drop 'Ba' data
glass=glass.drop(['Ba'],axis=1)
print(glass.head(10))

#Data Normalization
def norm_func(i):
    x=(i-i.min())	/ (i.max()-i.min())
    return (x)

glass_n=norm_func(glass)
print(glass_n.head(10))
glass_n.to_csv("dataset\\normalizedGlass.csv")


