import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("disease_model.pkl")

st.title("🩺 Disease Prediction System")

age = st.number_input("Enter Age", min_value=1, max_value=100)

gender = st.selectbox("Gender",["Male","Female"])
gender_value = 1 if gender == "Male" else 0

blood_pressure = st.selectbox("Blood Pressure",["Low","Normal","High"])
if blood_pressure == "Low":
    blood_pressure_value = 0
elif blood_pressure == "Normal":
    blood_pressure_value = 1
else:
    blood_pressure_value = 2

heart_rate = st.number_input("Heart Rate (BPM)",min_value=30,max_value=200,value=120,step=1)
temperature = st.number_input("Temperature")

symptom = st.selectbox("Symptoms",["Body Pain,Fever","Chest Pain","Fever Cough","Fever,Cough,Headache,Body Pain","Headache","Sneezing","Sore Throat","Thirst,Frequent Urination","Wheezing"])
symptom_map = {"Body Pain,Fever": 0,"Chest Pain": 1,"Fever Cough": 2,"Fever,Cough,Headache,Body Pain": 3,"Headache": 4,"Sneezing": 5,"Sore Throat":6,"Thirst,Frequent Urination": 7,"Wheezing": 8}
symptoms = symptom_map[symptom]

if st.button("Predict Disease"):

    input_data = np.array([[age,gender_value,blood_pressure_value,
                            heart_rate,temperature,symptoms]])

    prediction = model.predict(input_data)
    disease_map = {0:"Allergy",1:"Asthma",2:"Common Cold",3:"Dengue",4:"Diabetes",5:"Flu",6:"Heart Disease",7:"High Blood Pressure"}
    st.success(f"Predicted Disease: {disease_map[int(prediction[0])]}")


    
        

   