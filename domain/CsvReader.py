import pandas as pd

def carregaDadosDoCsv():
    dataFrame = pd.read_csv("domain\db\winequality-red.csv", encoding = "UTF-8", sep = ";")
    return dataFrame