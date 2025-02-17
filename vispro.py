import streamlit as st
import pandas as pd
import numpy as np
from graph import Field3d
from heatmap import Heatmap
import json

z = pd.read_csv('data/barbay/barbay.csv', index_col=0).to_numpy()
config = {'displayModeBar': False, 'responsive': True}
match_plot = Field3d()
match_plot.build_graph(z)

with open('data/barval/match_data.json') as file:
    match_data = json.load(file)

team = match_data['events'][1]['teamId']
player_dict = match_data['playerIdNameDictionary']

touches_teamA = []
touches_teamB = []

for event in match_data['events']:
    if event['isTouch']:
        if event['teamId'] == team:
            touches_teamA.append(event)
        else:
            touches_teamB.append(event)



# if "selected_player" not in st.session_state:
#     st.session_state.selected_player = list(match_data['playerIdNameDictionary'].keys())[0]

#     touches_player = []
#     for touch in touches_teamA:
#         if touch['playerId'] == int(list(match_data['playerIdNameDictionary'].keys())[0]):
#             touches_player.append([touch[x] for x in ['minute', 'second', 'teamId', 'playerId', 'x', 'y']])
    
#     global touches_player_df
#     touches_player_df = pd.DataFrame(touches_player, columns=['minute', 'second', 'teamId', 'playerId', 'x', 'y'])
#     touches_player_df['x_scaled'] = touches_player_df.x - heatmap.field_length/2
#     touches_player_df['y_scaled'] = touches_player_df.y*0.7 - heatmap.field_width/2

def update_selection():
    st.session_state.selected_player = st.session_state.player_heatmap_selection
    touches_player = []
    for touch in touches_teamA:
        if touch['playerId'] == int(st.session_state.selected_player):
            touches_player.append([touch[x] for x in ['minute', 'second', 'teamId', 'playerId', 'x', 'y']])

    global touches_player_df
    touches_player_df = pd.DataFrame(touches_player, columns=['minute', 'second', 'teamId', 'playerId', 'x', 'y'])
    touches_player_df['x_scaled'] = touches_player_df.x - heatmap.field_length/2
    touches_player_df['y_scaled'] = touches_player_df.y*0.7 - heatmap.field_width/2
    print(touches_player_df.head())


###### Web Page ######

st.set_page_config(
    page_title="xT Visualization",
    page_icon=":material/sports_and_outdoors:",
    layout="wide",
    initial_sidebar_state="expanded"
    )

st.title('Expected Threat 3D Visualization')

col_left, middle, col_right = st.columns([0.1, 0.3, 0.1], vertical_alignment='top', border=True, gap='small')

with col_left:
    player_selected = st.selectbox(
        "Player Heatmap",
        options=player_dict.keys(),
        format_func=lambda x: player_dict[x],
        key='player_heatmap_selection'
        )
    heatmap = Heatmap()
    touches_player = []
    for touch in touches_teamA:
        if touch['playerId'] == int(player_selected):
            touches_player.append([touch[x] for x in ['minute', 'second', 'teamId', 'playerId', 'x', 'y']])

    touches_player_df = pd.DataFrame(touches_player, columns=['minute', 'second', 'teamId', 'playerId', 'x', 'y'])
    touches_player_df['x_scaled'] = touches_player_df.x - heatmap.field_length/2
    touches_player_df['y_scaled'] = touches_player_df.y*0.7 - heatmap.field_width/2
    heatmap.build_graph(touches_player_df)
    st.plotly_chart(heatmap.fig, config=config, use_container_width=True)

with middle:
    st.plotly_chart(match_plot.fig, config=config, use_container_width=True)

with col_right:
    st.write('Column right')
######################