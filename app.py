import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Mental Health & Burnout Final Project")

df=pd.read_csv("data/student_mental_health_burnout_1M.csv")
st.dataframe(df.head())

#Q1 Visual
st.subheader("Q1: How do sleep hours and study hours per day influence students stress, anxiety, and depression levels?​")

df_sample=df.sample(10000)

df_sample["sleep_group"] = pd.cut(
    df_sample["sleep_hours"],
    bins=5,
    labels=["Very Low", "Low", "Moderate", "High", "Very High"]
)

fig = px.scatter(
    df_sample,
    x="sleep_hours",
    y="stress_level",
    opacity=0.3,
    color="sleep_group",
    title="Relationship Between Sleep and Stress"
)

st.plotly_chart(fig, use_container_width=True)

