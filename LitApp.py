import streamlit as st
import pandas as pd
df=pd.read_csv('Final FBRef 2022-2023.csv')



df=df[df.Min>450]

df=df[df['Main Position'].notna()]

st.title('Rising Star Scout')

st.subheader('Only players who played more than 450 minutes are shown')

age=st.radio('Which age group do you want to see',('Whole Database','U23','U21'))

st.subheader('Players are sorted by minutes played')

if age=='U23':
    df23=df[df.Age<=23]
    df23=df23.sort_values('Min',ascending=False)
    st.dataframe(df23)
elif age=='U21':
    df21=df[df.Age<=21]
    st.dataframe(df21)
elif age=='Whole Database':
    st.dataframe(df)


st.sidebar.success('Select a page from the above')
