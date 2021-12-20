import pandas as pd



def main():
    
    #Get dataset from file
    data=pd.read_csv("dataset\glass.csv")

    print(data.head(10))





if __name__ == '__main__':
    main()