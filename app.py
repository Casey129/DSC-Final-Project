import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Mental Health & Burnout Final Project")

df = pd.read_csv("student_mental_health_burnout_200.csv")
st.dataframe(df.head())
st.caption("**Data Source:** Student Lifestyle, Mental Health & Burnout Insight — [Kaggle](https://www.kaggle.com/datasets/ayeshasiddiqa123/student-health)")
layout_defaults=dict(
    plot_bgcolor='white',
    paper_bgcolor= 'white',
    font=dict(color='black')
)

sleep_color_map={
    "Very Low":  "#d73027",
    "Low":       "#fc8d59",
    "Moderate":  "#fee090",
    "High":      "#91bfdb",
    "Very High": "#4575b4"
}

two_group_colors = {
    "Low":  "#fc8d59", 
    "High": "#4575b4"   
}

four_group_colors = {
    "Very Low":  "#d73027",
    "Low":       "#fc8d59",
    "High":      "#91bfdb",
    "Very High": "#4575b4"
}

st.sidebar.header("Dashboard Controls")
sample_size = st.sidebar.slider("Sample Size", min_value=100, max_value=1000, value=200, step=100)

year_filter = st.sidebar.multiselect(
    "Filter by Academic Year",
    options=sorted(df["academic_year"].unique()),
    default=sorted(df["academic_year"].unique())
)
df = df[df["academic_year"].isin(year_filter)]

#Q1 Visual
<<<<<<< HEAD
st.subheader("Q1: How do sleep hours and study hours per day influence students stress levels?")
=======
st.subheader("How do sleep hours and study hours per day influence students stress levels?")
df_sample=df.sample(sample_size)
>>>>>>> 4260e2a (Cohesive colors and captions)


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
    color_discrete_map=sleep_color_map,
    category_orders={"sleep_group": ["Very Low", "Low", "Moderate", "High", "Very High"]},
    title="Sleep vs Stress"
)

fig.update_layout(
    title="Sleep vs Stress",
    xaxis_title="Sleep Hours",
    yaxis_title="Stress Level"
)

st.plotly_chart(fig, width="stretch")
st.caption(
    "The graph is showing a negative relationship between sleep and stress, meaning as sleep increases, stress tends to decrease. While there is some variation, overall students who get more sleep experience lower stress on average. "
)

#Q2 Visual 
st.subheader("How does exam pressure influence academic performance and mental health?​")

df_sample=df.sample(sample_size)


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
   color_discrete_map=two_group_colors,
    category_orders={
        "pressure_group": ["Low", "Moderate", "High"],
        "mental_health_group": ["Low", "High"]
    },
    title="Exam Pressure vs Academic Performance and Mental Health (color)"
)

fig.update_layout(
    title="Exam Pressure vs Academic Performance and Mental Health",
    xaxis_title="Exam Pressure",
    yaxis_title="Academic Performance",
)

st.plotly_chart(fig, width="stretch")
st.caption(
    "Exam pressure alone does not define how students perform, mental health plays a key role in how students handle pressure and the outcome of their performance. Students with lower mental health are more negatively affected, especially as pressure increases. Pressure isn’t a bad thing, it can be motivational, but mental health is what determines how well students can handle pressure."
           )
#Q3 Visual
st.subheader("How do lifestyle behaviors impact students mental health?")

<<<<<<< HEAD
st.markdown("""
Upon analyzing the relationship between lifestyle and well-being, our graph reveals a compelling reality. Rest is the foundation, but physical activity is the enhancer.
""")
df['sleep_category'] = df['sleep_hours'].apply(
    lambda x: 'Sufficient (+7h)'if x>= 7 else 'Insufficient (<7h)'
=======
df_sample=df.sample(sample_size)

df_sample["screen_group"]= pd.qcut(
    df_sample["screen_time"],
    3,
    labels=["Low", "Medium", "High"]
>>>>>>> 4260e2a (Cohesive colors and captions)
)
df['activity_level']= df['physical_activity'].apply(
    lambda x: 'Active' if x>=3 else 'Sedentary'
)
df_grouped = df.groupby(['sleep_category','activity_level'])['mental_health_index'].mean().reset_index()

fig=px.bar(
    df_grouped,
    x="sleep_category",
    y="mental_health_index",
<<<<<<< HEAD
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
=======
    color="activity_group",
   color_discrete_map=two_group_colors,
    category_orders={
        "screen_group": ["Low", "Medium", "High"],
        "activity_group": ["Low", "High"]
    },
    barmode="group",
    title="Mental Health vs Screen Time and Physical Activity (color)"
)

fig.update_layout(
    title="Mental Health vs Screen Time and Physical Activity",
    xaxis_title="Screen Time",
    yaxis_title="Mental Health Index"
)

>>>>>>> 4260e2a (Cohesive colors and captions)
st.plotly_chart(fig, width="stretch")
st.info("""
We observed that students who sleep less than 7 hours exhibit the lowest mental health scores, regardless of whether or not they exercise. However, upon moving to the 'Sufficient Sleep' (+7h) column, we see a significant jump in well-being. This demonstrates that getting good sleep is not enough; students who combine sufficient sleep with an active lifestyle achieve the highest levels of mental health in our study. Conversely, sedentary students with insufficient sleep represent the group at highest risk for burnout.
""")

<<<<<<< HEAD

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
=======
#Q4
st.subheader("Does a social support system reduce the negative effects of stress and anxiety on burnout?​")

df_sample=df.sample(sample_size)
>>>>>>> 4260e2a (Cohesive colors and captions)

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
<<<<<<< HEAD
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
=======

fig=px.histogram(
    df_sample,
    x="burnout_score",
    nbins=30,
    color= "support_group",
    color_discrete_map=four_group_colors,
    category_orders={"support_group": ["Very Low", "Low", "High", "Very High"]},
    histnorm="probability density",
    barmode="overlay",
    opacity=0.6,
    title= "Burnout vs Social Support Level"
)

fig.update_layout(
    title="Burnout vs Social Support Level",
    xaxis_title="Burnout Score",
    yaxis_title="Density",
>>>>>>> 4260e2a (Cohesive colors and captions)
)

st.plotly_chart(fig, width="stretch")

<<<<<<< HEAD
st.info("""
Our analysis reveals that social support doesn't just improve 
well-being—it fundamentally changes the statistical distribution of burnout. 
While stress levels might be similar, the support system flattens the curve, 
preventing students from reaching a point of total academic exhaustion.
""")

#Q5 Visual 
st.subheader("Q5: How does financial stress and family expectations impact mental health and academic performance?")

=======
#Q5
st.subheader("How does financial stress and family expectations impact mental health and academic performance?")

df_sample=df.sample(sample_size)

>>>>>>> 4260e2a (Cohesive colors and captions)
fig=px.density_heatmap(
    df,
    x="financial_stress",
    y="family_expectation",
    color_continuous_scale="RdYlBu_r",
    title="Financial Stress vs Family Expectations"
)

fig.update_layout(
    title="Financial Stress vs Family Expectations",
    xaxis_title="Financial Stress",
    yaxis_title="Family Expectations"
)

st.plotly_chart(fig, width="stretch")
 
