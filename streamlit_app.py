import streamlit as st

st.title("🎈 My new app")
st.title("BMI Calculator")
weight=st.number_input("enter your weight (kg) :",min_value=0.0, format="%2f")
height_d=st.radio("select your height unit:",["Centimeters","Meters","Feet"])
height=st.number_input(f"enter your height({height_d.lower()}):",
                       min_value=0.0,format="%.2f")
if st.button("Calculate BMI"):
    try:
        if height_d=='Centimeters':
            height_m=height/100
        elif height=="Feet":
            height_m=height/3.28
        else:
            height_m=height
        if height_m<0:
            st.error("height must be greater then 0")
        else:
            bmi=weight/(height_m ** 2)
            st.success(f"your BMI is {bmi:2f}")
        if bmi<16:
            st.error("your are extremely underweight")
        elif 16<=bmi<18.5:
            st.warning("you are underweight")
        elif 18.5<=bmi<25:
            st.success("you are Healthy")
        elif 25<=bmi<30:
            st.warning("you are over weight")
    except:
        st.error("please enter valid numerical values")
