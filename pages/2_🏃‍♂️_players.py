import streamlit as st

# Page config
st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide",
)

df_data = st.session_state['data']

clubs = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Club', sorted(clubs))

df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Name', sorted(players))

player_selected = df_data[df_data['Name'] == player].iloc[0]

st.image(player_selected['Photo'])
st.title(player_selected['Name'])

st.markdown(f"**Club:** {player_selected['Club']}")
st.markdown(f"**Position:** {player_selected['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Age:** {player_selected['Age']}")
col2.markdown(f"**Height:** {player_selected['Height(cm.)']/100}")
col3.markdown(f"**Weight:** {player_selected['Weight(lbs.)']*0.453:.2f}")

st.divider()

st.subheader(f"Overall {player_selected['Overall']}")
st.progress(int(player_selected['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Market Value", value=f"£ {player_selected['Value(£)']}")
col2.metric(label="Weekly", value=f"£ {player_selected['Wage(£)']}")
col3.metric(label="Release Clause", value=f"£ {player_selected['Release Clause(£)']}")
