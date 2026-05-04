import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Mental Health & Burnout Final Project")

df = pd.read_csv("student_mental_health_burnout_200.csv")
st.dataframe(df.head())

#Q1 Visual
st.subheader("Q1: How do sleep hours and study hours per day influence students stress levels?")


df["sleep_group"] = pd.cut(
    df["sleep_hours"],
    bins=5,
    labels=["Very Low", "Low", "Moderate", "High", "Very High"]
)

fig = px.scatter(
    df,
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


df["pressure_group"] = pd.qcut(
    df["exam_pressure"],
    3,
    labels=["Low", "Moderate", "High"],
)

df["mental_health_group"] = pd.qcut(
    df["mental_health_index"],
    2,
    labels=["Low","High"]
)

fig=px.box(
    df,
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

st.markdown("""
Upon analyzing the relationship between lifestyle and well-being, our graph reveals a compelling reality. Rest is the foundation, but physical activity is the enhancer.
""")
df['sleep_category'] = df['sleep_hours'].apply(
    lambda x: 'Sufficient (+7h)'if x>= 7 else 'Insufficient (<7h)'
)
df['activity_level']= df['physical_activity'].apply(
    lambda x: 'Active' if x>=3 else 'Sedentary'
)
df_grouped = df.groupby(['sleep_category','activity_level'])['mental_health_index'].mean().reset_index()

fig=px.bar(
    df_grouped,
    x="sleep_category",
    y="mental_health_index",
    color="activity_level",
    barmode="group",
    text_auto= '.2f',
    title="Average Mental Health Index by Sleep and Activity",
    labels = {
        'sleep_category': "Sleep Habits",
        'mental_health_index': "Avg Mental Health Index", 
        'activity_level': 'Lifestyle Type'
    },
    color_discrete_sequence = ["#A8E6CF", "#FF8B94"]
)
st.plotly_chart(fig, width="stretch")
st.info("""
We observed that students who sleep less than 7 hours exhibit the lowest mental health scores, regardless of whether or not they exercise. However, upon moving to the 'Sufficient Sleep' (+7h) column, we see a significant jump in well-being. This demonstrates that getting good sleep is not enough; students who combine sufficient sleep with an active lifestyle achieve the highest levels of mental health in our study. Conversely, sedentary students with insufficient sleep represent the group at highest risk for burnout.
""")


#Q4 Visual 
st.subheader("Q4: Does a social support system reduce the negative effects of stress and anxiety on burnout?​")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🛡️")
    st.markdown("**Protective Buffer**")
    st.write(
        "Students with Strong Support show a distribution concentrated in "
        "low burnout levels, creating a safety net against academic pressure."
    )

with col2:
    st.markdown("### 📊")
    st.markdown("**Median Reduction**")
    st.write(
        "The marginal box plot confirms a significant downward shift in the "
        "median burnout score for students with active social networks."
    )

with col3:
    st.markdown("### 🚨")
    st.markdown("**Extreme Risk**")
    st.write(
        "Critical burnout levels (scores >7) are predominantly found in students "
        "with Weak Support, highlighting their vulnerability."
    )
df['support_level'] = df['social_support'].apply(
    lambda x: 'Strong Support' if x>= 5 else "Weak Support"         
)
fig = px.histogram(
    df, 
    x= "burnout_score",
    color = 'support_level',
    marginal = 'rug',
    barmode = 'overlay',
    title = "Distribution of Burnout Scores by Support Level",
    labels= {
        'burnout_score': "Burnour Score (Higher is more severe)",
        'support_level': "Social Support"
    },
    color_discrete_sequence = ["#A2CFFE", "#FFD8B1"],
)
st.plotly_chart(fig, width="stretch")

st.info("""
Our analysis reveals that social support doesn't just improve 
well-being—it fundamentally changes the statistical distribution of burnout. 
While stress levels might be similar, the support system flattens the curve, 
preventing students from reaching a point of total academic exhaustion.
""")

#Q5 Visual 
st.subheader("Q5: How does financial stress and family expectations impact mental health and academic performance?")

fig=px.density_heatmap(
    df,
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
