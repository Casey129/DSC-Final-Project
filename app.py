import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Mental Health & Burnout Final Project")

df = pd.read_csv("data/sample_student_mental_health_burnout_1M.csv")
st.dataframe(df.head())

#Q1 Visual
st.subheader("Q1: How do sleep hours and study hours per day influence students stress levels?")
df_sample=df.sample(200)

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
    title="Sleep vs Stress"
)

fig.update_layout(
    title="Sleep vs Stress",
    xaxis_title="Sleep Hours",
    yaxis_title="Stress Level"
)

st.plotly_chart(fig, width="stretch")

#Q2 Visual 
st.subheader("Q2: How does exam pressure influence academic performance and mental health?​")

df_sample=df.sample(200)

df_sample["pressure_group"] = pd.qcut(
    df_sample["exam_pressure"],
    3,
    labels=["Low", "Moderate", "High"],
)

df_sample["mental_health_group"] = pd.qcut(
    df_sample["mental_health_index"],
    2,
    labels=["Low","High"]
)

fig=px.box(
    df_sample,
    x="pressure_group",
    y="academic_performance",
    color="mental_health_group",
    color_discrete_sequence=["#1DE9DE", "#8D50B8"],
    category_orders={"pressure_group": ["Low", "Moderate", "High"]},
    title="Exam Pressure vs Academic Performance and Mental Health (color)"
)

fig.update_layout(
    title="Exam Pressure vs Academic Performance and Mental Health",
    xaxis_title="Exam Pressure",
    yaxis_title="Academic Performance"
)

st.plotly_chart(fig, width="stretch")

#Q3 Visual
st.subheader("Q3: How do lifestyle behaviors impact students mental health?")

df_sample=df.sample(200)

df_sample["screen_group"]= pd.qcut(
    df_sample["screen_time"],
    3,
    labels=["Low", "Medium", "High"]
)

df_sample["activity_group"] = pd.qcut(
    df_sample["physical_activity"],
    2,
    labels=["Low","High"]
)

fig=px.bar(
    df_sample,
    x="screen_group",
    y="mental_health_index",
    color="activity_group",
    category_orders={"screen_group": ["Low", "Medium", "High"]},
    barmode="group",
    color_discrete_sequence=["#05B4FF", "#0E3EFF"],
    title="Mental Health vs Screen Time and Physical Activity (color)"
)

fig.update_layout(
    title="Mental Health vs Screen Time and Physical Activity",
    xaxis_title="Screen Time",
    yaxis_title="Mental Health"
)

st.plotly_chart(fig, width="stretch")

st.subheader("Q4: Does a social support system reduce the negative effects of stress and anxiety on burnout?​")

df_sample=df.sample(200)

df_sample['support_group']=pd.qcut(
    df_sample["social_support"],
    4,
    labels=["Very Low", "Low", "High", "Very High"]
)

fig=px.histogram(
    df_sample,
    x="burnout_score",
    nbins=30,
    color= "support_group",
    histnorm="probability density",
    barmode="overlay",
    opacity=0.5,
    title= "Burnout vs Social Support Level"
)

fig.update_layout(
    title="Burnout vs Social Support Level",
    xaxis_title="Burnout Score",
    yaxis_title="Density"
)
st.plotly_chart(fig, width="stretch")

st.subheader("Q5: How does financial stress and family expectations impact mental health and academic performance?")

df_sample=df.sample(200)

fig=px.density_heatmap(
    df_sample,
    x="financial_stress",
    y="family_expectation",
    title="Financial Stress vs Family Expectations"
)

fig.update_layout(
    title="Financial Stress vs Family Expectations",
    xaxis_title="Financial Stress",
    yaxis_title="Family Expectations"
)

st.plotly_chart(fig, width="stretch")

st.subheader("Q6: Dropout Risk Distribution")
#Couldnt get this question to work for any charts 
