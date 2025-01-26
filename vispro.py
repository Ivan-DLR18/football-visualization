import streamlit as st
import pandas as pd
import numpy as np
import ast

with open('../content_BARBAY.txt', 'r') as page_content:
    # Use BeautifulSoup to parse the page source
    soup = page_content.read()

# Split at the colon and take the second part
dict_str = soup.split("matchCentreData: ")[1]

# Use ast.literal_eval for safety
match_centre_data = ast.literal_eval(dict_str)

team = match_centre_data['events'][1]['teamId']

touches_teamA = []
touches_teamB = []

for event in match_centre_data['events']:
    if event['isTouch']:
        if event['teamId'] == team:
            touches_teamA.append(event)
        else:
            touches_teamB.append(event)

event_data = []

for touches_team in (touches_teamA, touches_teamB):
    for event in touches_team:
        if event['type']['displayName'] == 'Pass' and event['outcomeType']['displayName'] == 'Successful':
            event_data.append([event[x] for x in ['minute', 'second', 'teamId', 'playerId', 'x', 'y', 'endX', 'endY']] + \
                            [event[x]['displayName'] for x in ['period', 'type', 'outcomeType']]
                            )

event_df = pd.DataFrame(event_data, columns=['minute', 'second', 'teamId', 'playerId', 'x', 'y', 'endX', 'endY', 'period', 'type', 'outcome'])


###### Web Page ######

st.set_page_config(
    page_title="xT Visualization",
    page_icon=":material/sports_and_outdoors:",
    layout="wide",
    initial_sidebar_state="expanded")


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
######################