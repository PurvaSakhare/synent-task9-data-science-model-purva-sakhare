import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL & DATASET
# --------------------------------------------------
model = joblib.load("model.pkl")
df = pd.read_csv("StudentsPerformance.csv")

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div style="
background: linear-gradient(90deg,#4CAF50,#2196F3);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
margin-bottom:20px;
">
<h1>🎓 Student Performance Prediction System</h1>
<p>Machine Learning Powered Dashboard for Student Score Prediction 🚀</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("📥 Student Details")

gender = st.sidebar.selectbox(
    "👤 Gender",
    ["Male", "Female"]
)

race_option = st.sidebar.selectbox(
    "🌍 Race / Ethnicity",
    ["Group A", "Group B", "Group C", "Group D", "Group E"]
)

education_option = st.sidebar.selectbox(
    "🎓 Parental Education",
    [
        "High School",
        "Some High School",
        "Associate Degree",
        "Bachelor Degree",
        "Master Degree",
        "Some College"
    ]
)

lunch_option = st.sidebar.selectbox(
    "🍽 Lunch Type",
    ["Standard", "Free/Reduced"]
)

prep_option = st.sidebar.selectbox(
    "📚 Test Preparation",
    ["Completed", "None"]
)

reading = st.sidebar.slider(
    "📖 Reading Score",
    0,
    100,
    50
)

writing = st.sidebar.slider(
    "✍️ Writing Score",
    0,
    100,
    50
)

# --------------------------------------------------
# ENCODING INPUTS
# --------------------------------------------------
gender_value = 1 if gender == "Male" else 0

race_mapping = {
    "Group A": 0,
    "Group B": 1,
    "Group C": 2,
    "Group D": 3,
    "Group E": 4
}

education_mapping = {
    "High School": 0,
    "Some High School": 1,
    "Associate Degree": 2,
    "Bachelor Degree": 3,
    "Master Degree": 4,
    "Some College": 5
}

race = race_mapping[race_option]
parent_edu = education_mapping[education_option]

lunch = 1 if lunch_option == "Standard" else 0
prep = 1 if prep_option == "Completed" else 0

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2 = st.tabs(["🎯 Prediction", "📊 Analytics"])

# ==================================================
# TAB 1 : PREDICTION
# ==================================================
with tab1:

    st.subheader("Predict Student Math Score")

    if st.button("🚀 Predict Score"):

        data = np.array([
            [
                gender_value,
                race,
                parent_edu,
                lunch,
                prep,
                reading,
                writing
            ]
        ])

        prediction = model.predict(data)

        st.markdown(f"""
        <div style="
        background-color:#1f2937;
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;
        ">
        <h2>📈 Predicted Math Score</h2>
        <h1>{prediction[0]:.2f}</h1>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if prediction[0] >= 80:
            st.success("🌟 Excellent Performance Expected")

        elif prediction[0] >= 60:
            st.info("👍 Good Performance Expected")

        else:
            st.warning("📚 Student Needs More Practice")

        st.balloons()

# ==================================================
# TAB 2 : ANALYTICS
# ==================================================
with tab2:

    st.header("📊 Exploratory Data Analysis")

    col1, col2 = st.columns(2)

    # Histogram
    with col1:

        st.subheader("Math Score Distribution")

        fig1, ax1 = plt.subplots()

        sns.histplot(
            df["math score"],
            bins=20,
            kde=True,
            ax=ax1
        )

        st.pyplot(fig1)

    # Gender Count
    with col2:

        st.subheader("Gender Distribution")

        fig2, ax2 = plt.subplots()

        sns.countplot(
            x="gender",
            data=df,
            ax=ax2
        )

        st.pyplot(fig2)

    # Heatmap
    st.subheader("🔥 Correlation Heatmap")

    try:

        df_corr = df.copy()

        for col in df_corr.columns:
            if df_corr[col].dtype == "object":

                encoder = LabelEncoder()

                df_corr[col] = encoder.fit_transform(
                    df_corr[col].astype(str)
                )

        corr_matrix = df_corr.corr(
            numeric_only=True
        )

        fig3, ax3 = plt.subplots(
            figsize=(10, 6)
        )

        sns.heatmap(
            corr_matrix,
            annot=True,
            cmap="coolwarm",
            ax=ax3
        )

        st.pyplot(fig3)

    except Exception as e:

        st.warning(
            f"Heatmap Error: {e}"
        )

    # Dataset Preview
    with st.expander("📋 View Dataset Preview"):

        st.dataframe(df.head(10))

# --------------------------------------------------
# PROJECT INFO
# --------------------------------------------------
st.markdown("---")

st.subheader("📌 About This Project")

st.write("""
This project uses Machine Learning to predict student math scores based on
academic and demographic information.

### Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Matplotlib
- Seaborn

### Model
- Random Forest Regressor
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

st.markdown("""
<div style='text-align:center'>
<h4>💻 Developed by Purva Sakhare</h4>
<p>🚀 Data Science Internship Project 2026</p>
</div>
""", unsafe_allow_html=True)