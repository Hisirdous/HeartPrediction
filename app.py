import streamlit as st
from src.modeling.predict import predict_new

st.title("Dự đoán nguy cơ đau tim")

age = st.number_input("Tuổi", min_value=0, max_value=120, value=30)
gender = st.selectbox("Giới tính", ["Nam giới", "Nữ giới"])
heart_rate = st.number_input("Nhịp tim", value=70)
sbp = st.number_input("Huyết áp tâm thu", value=120)
dbp = st.number_input("Huyết áp tâm trương", value=80)
blood_sugar = st.number_input("Đường huyết", value=100)
ck_mb = st.number_input("CK-MB", value=1.0)
troponin = st.number_input("Troponin", value=0.01)

if st.button("Predict"):
    data = {
        "Age": age,
        "Gender": 1 if gender == "Male" else 0,
        "Heart rate": heart_rate,
        "Systolic blood pressure": sbp,
        "Diastolic blood pressure": dbp,
        "Blood sugar": 1 if blood_sugar > 120 else 0,
        "CK-MB": ck_mb,
        "Troponin": troponin,
    }

    result = predict_new(data)
    st.success("Nguy cơ đau tim cao" if result == 1 else "Rủi ro thấp")
