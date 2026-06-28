# synent-task9-data-science-model-purva-sakhare
End-to-End Data Science Project using Machine Learning and Streamlit for Student Performance Prediction with EDA, Model Training, Evaluation, and Deployment.
# 🎓 Student Performance Prediction System

## 📖 Overview

The Student Performance Prediction System is an End-to-End Data Science project developed using Machine Learning and Streamlit.

This application predicts a student's Math Score based on factors such as gender, race/ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score.

The project demonstrates the complete Data Science lifecycle, including data collection, preprocessing, exploratory data analysis (EDA), model development, evaluation, and deployment.

---

## 🎯 Project Objective

The main objective of this project is to build a machine learning model that can accurately predict student performance and provide predictions through an interactive web application.

---

## 📊 Dataset Information

**Dataset:** Student Performance Dataset

The dataset contains information about students and their academic-related attributes.

### Input Features

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

### Target Variable

* Math Score

---

## 🔄 Project Workflow

### 1. Data Collection

The dataset was obtained from Kaggle and imported into the project environment for analysis.

### 2. Data Cleaning & Preprocessing

* Checked for missing values
* Handled categorical variables
* Applied Label Encoding
* Prepared data for machine learning models

### 3. Exploratory Data Analysis (EDA)

Several visualizations were created to understand the dataset:

* Math Score Distribution
* Gender Distribution
* Correlation Heatmap
* Feature Relationship Analysis

These analyses helped identify patterns and relationships among variables.

### 4. Feature Selection

Relevant features were selected to improve model performance and prediction accuracy.

### 5. Model Building

A Random Forest Regressor model was trained using the processed dataset.

### 6. Model Evaluation

The model was evaluated using:

* Root Mean Squared Error (RMSE)
* R² Score

These metrics were used to measure prediction accuracy and model performance.

### 7. Deployment

The trained machine learning model was deployed using Streamlit, allowing users to enter input values and receive instant predictions.

---

## 🛠️ Technologies Used

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Programming Language       |
| Pandas       | Data Manipulation          |
| NumPy        | Numerical Operations       |
| Scikit-Learn | Machine Learning           |
| Matplotlib   | Data Visualization         |
| Seaborn      | Data Visualization         |
| Joblib       | Model Serialization        |
| Streamlit    | Web Application Deployment |

---

## 📁 Project Structure

```text
data_science_project/
│
├── app.py
├── train_model.py
├── model.pkl
├── StudentsPerformance.csv
├── requirements.txt
└── README.md
```

---

## 🚀 Features

✅ Student Math Score Prediction

✅ Interactive Streamlit User Interface

✅ Exploratory Data Analysis Visualizations

✅ Machine Learning Model Integration

✅ Real-Time Prediction Results

✅ End-to-End Data Science Workflow

---

## ▶️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/your-username/student-performance-prediction.git
```

### Move to Project Directory

```bash
cd student-performance-prediction
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📈 Model Performance

The Random Forest Regressor was trained on the processed dataset and achieved reliable prediction performance for student math scores.

Evaluation metrics such as RMSE and R² Score were used to assess model effectiveness.

---

## 🌐 Deployment

The application can be deployed using:

* Streamlit Community Cloud
* Render
* Railway
* Local Deployment

---

## 📸 Application Preview

The application allows users to:

1. Enter student information.
2. Click the Predict button.
3. Receive the predicted Math Score instantly.
4. View EDA visualizations and dataset insights.

---

## 🎓 Internship Task Coverage

This project successfully covers:

* Data Collection
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training
* Model Evaluation
* Streamlit Deployment
* User Interface Development

---

## 👩‍💻 Author

**Purva Sakhare**

Data Science Internship Project

2026
