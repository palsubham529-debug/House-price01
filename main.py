import streamlit as st
import numpy as np
import joblib
#Uploding the model
model = joblib.load("rf.pkl")
st.title("House Price Prediction")
st.markdown("_ _ _")

bedroom = st.number_input("Enter the number of bedroom", min_value=0,value=0)
bathroom = st.number_input("Enter the number of bathroom", min_value=0,value=0)
living_area = st.number_input("Enter the number of living area",min_value=0,value=2000)
condition_of_the_house = st.number_input("Enter the condition", min_value=0,value=0)
Number_of_schools_nearby = st.number_input("Enter the number of school", min_value=0,value=0)

X = [[bedroom,bathroom,living_area,condition_of_the_house,Number_of_schools_nearby]]

pred=st.button("Predict")

    
if pred==True:
    
    if (
        bedroom == 0 or
        bathroom == 0 or
        condition_of_the_house == 0 or
        Number_of_schools_nearby == 0
    ):
        st.warning("⚠️ Please enter the values for all required fields.")
    else:
        np_array = np.array(X)
        price = int(model.predict(np_array)[0])
        st.success(f"🏠 Predicted House Price = {price}")
else:
    st.info("Please click the **Predict** button.")