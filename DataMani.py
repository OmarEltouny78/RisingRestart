import pandas as pd

df=pd.read_csv('Final FBRef 2022-2023.csv')

df['Min'] = df['Min'].replace(',','', regex=True)
df.Min=df.Min.astype(int)
#df['Age']=df['Age'].str[0:2]
df = df[df['Age'].notna()]
df.Age=df.Age.astype(int)

#df.dropna(how='all', axis=1,inplace=True)
df.rename(columns={"": "pid"},inplace=True)


def Uage(dataframe,age=23):
    dataframe=dataframe[dataframe.Age<age]
    return dataframe