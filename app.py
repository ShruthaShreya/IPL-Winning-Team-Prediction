import streamlit as st
import pickle
import pandas as pd

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]
cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.markdown("<h1 style='text-align: center;'>🏆 IPL Win Predictor</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('🏏 Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('🎾 Select bowling team', sorted(teams))
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    selected_city = st.selectbox('📍 Select host city', sorted(cities))
with col2:
    target = st.number_input('🎯 Target')
st.markdown("<br>", unsafe_allow_html=True)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('🎰 Score')
with col4:
    overs = st.number_input('⏱️ Overs completed')
with col5:
    wickets_out = st.number_input('🚩 Wickets out')
st.markdown("<br>", unsafe_allow_html=True)

if st.button('🔮 Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets_out
    crr = score / overs if overs else 0
    rrr = ((runs_left * 6) / balls_left) if balls_left else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"<h3>🥇 {batting_team}: {round(win * 100)}%</h3>"
        f"<h3>🥈 {bowling_team}: {round(loss * 100)}%</h3>",
        unsafe_allow_html=True
    )
