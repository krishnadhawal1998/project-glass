import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def main():
    glass_n=pd.read_csv("dataset\\normalizedGlass.csv")

    #Separating dependent and independent data
    X=np.array(glass_n.iloc[:,0:8])
    Y=np.array(glass_n['Type'])
    
    X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2)

if __name__ == '__main__':
    main()