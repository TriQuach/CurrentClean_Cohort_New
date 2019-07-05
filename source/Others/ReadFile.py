import pandas as pd
import datetime

def readFile(fileName):
    df = pd.read_csv(fileName,encoding = "utf-8")
    return df

