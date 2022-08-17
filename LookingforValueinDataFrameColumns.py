#import library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load data 
#place your data in the same directory
telco = pd.read_csv('Telco-Customer-Churn.csv')

coloum_name = []

def check_space(data):
    for x in data.columns:
        if data[x].isin([' ', '-', 'nan', 'n/a']).any():
            coloum_name.append(x)
        else:
            pass

    print(coloum_name)