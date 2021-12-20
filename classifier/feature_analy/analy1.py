
"""
Feasture Analysis. Ref issue #2
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


#Read data set
glass= pd.read_csv("dataset\glass.csv")

na_count=glass.isna().sum()
print(f"Found NA values.\n {na_count}")
#No NA values found

#Checking for Outliers. Plotting box plots
figs=[]
for col in glass[0:]:
    figs.append(plt.figure())
    sns.boxplot(glass[col])
    plt.savefig(f"classifier/boxplots/{col}.png")

print(f"Outliers were Detected in BoxPlots at location classifier/boxplots")

 
#plt.show()






