import pandas as pd
import streamlit as st


st.title("Calculator App")
st.write("Number 1")
num1 = st.number_input("Enter Number 1:")

st.write("What operation ?")
opr = st.text_input("Enter operand")

st.write("Number 2")
num2 = st.number_input("Enter Number 2:")



if opr=='+':
    st.write(num1+num2)
elif(opr=='-'):
    st.write(num1-num2)
elif(opr=='*'):
    st.write(num1*num2)



age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")