import streamlit as st
import pandas as pd
from soccerplots.radar_chart import Radar

df=pd.read_csv('Final FBRef 2022-2023.csv')
search= st.text_input('Look up the player you want', 'Rúben Dias')

player_df=df[df.Player==search]

st.dataframe(player_df)

df_compare=df=df[df['Main Position']==player_df['Main Position'].values[0]]

if [player_df['Main Position']=='Centre-Back']:
    params=['AerialWins','Intercepations','Tackle Won','PassBlock','Progessive Passes']

    ranges=((df.AerialWins.min(),df.AerialWins.max()),
                  (df.Int.min(),df.Int.max()),
                  (df.TklWinPoss.min(),df.TklWinPoss.max()),
                  (df.PassBlocks.min(),df.PassBlocks.max()),
                  (df.PrgP.min(),df.PrgP.max()))
    values=(player_df.AerialWins.values[0],player_df.Int.values[0],player_df.TklWinPoss.values[0]
            ,player_df.PassBlocks.values[0],player_df.PrgP.values[0])
## instantiate object -- changing fontsize
radar = Radar(label_fontsize=12, range_fontsize=7.5)   
## change in parameter value
## title values 
title = dict(
    title_name=player_df.Player.values[0],
    title_color='#000000',
    subtitle_name=player_df.Squad.values[0],
    subtitle_color='#B6282F',
    title_name_2='Radar Chart',
    subtitle_name_2=player_df['Main Position'].values[0],
    subtitle_color_2='#B6282F',
    title_fontsize=18,
    subtitle_fontsize=15,
)
## plot radar
fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values, 
                           radar_color=['#B6282F', '#FFFFFF'],title=title)
st.subheader('Player compared to all players in this position: '+ player_df['Main Position'].values[0])

st.pyplot(fig)