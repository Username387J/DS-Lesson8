#Handle Missing Values by replacing with mean avg
#Remove Duplicates
import pandas as pd
from sklearn.preprocessing import LabelEncoderimport 

df = pd.read_csv("titanic.csv")
print(df.head())
mean_age = df['Age'].mean()