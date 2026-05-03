import streamlit as st
import pandas as pd

st.title("🔥 Employee Engagement Dashboard")

df = pd.read_csv("final_output.csv")

# Sidebar filters
dept = st.sidebar.selectbox("Department", df['Department'].unique())
overtime = st.sidebar.selectbox("OverTime", df['OverTime'].unique())

filtered = df[
    (df['Department'] == dept) &
    (df['OverTime'] == overtime)
]

# Data show
st.subheader("Employees Data")
st.dataframe(filtered)

# Engagement Score
st.subheader("Engagement Score")
st.metric("Avg Engagement", round(filtered['EngagementIndex'].mean(), 2))

# Burnout Risk
st.subheader("Burnout Risk Distribution")
st.bar_chart(filtered['BurnoutRisk'].value_counts())

# Overtime vs Engagement
st.subheader("Overtime Impact")
st.bar_chart(df.groupby('OverTime')['EngagementIndex'].mean())