import pandas as pd
import streamlit as st


st.title("Measurement converter App")

import streamlit as st

options_list = ["Length", "Temperature", "Time"]

option = st.selectbox(
    "What parameter need to be converted", 
    options_list                         
)

# Display the selected option
st.write("You selected:", option)

#------------------------Temperature-----------------------

if option=='Temperature':
    unit = st.radio(
        "Unit to convert",('Fahrenheit','Celsius')
)
    
    if(unit=='Fahrenheit'):
        fah_val = st.number_input("Fahrenheit")
        if fah_val !=0:
            cel_val=(fah_val-32)/(9/5)
            st.write('converted Celsius value is',cel_val)
    elif(unit=='Celsius'):
        cel_val = st.number_input("Celsius")
        if cel_val !=0:
            fah_val=(cel_val*9/5)+32
            st.write('converted Celsius value is',fah_val)
#------------------------Length-----------------------------
if option=='Length':
    unit = st.radio(
        "Unit to convert",('Meter','Centimeter')
)
    
    if(unit=='Meter'):
        Meter = st.number_input("Meter")
        if Meter !=0:
            Centimeter=Meter*100
            st.write('converted value is',Centimeter)
    elif(unit=='Centimeter'):
        Centimeter = st.number_input("Centimeter")
        if Centimeter !=0:
            Meter=Centimeter/100
            st.write('converted value is',Meter)
#-----------------------Time--------------------------------
if option=='Time':
    unit = st.radio(
        "Unit to convert",('Second','Minute')
)
    
    if(unit=='Second'):
        Second = st.number_input("Second")
        if Second !=0:
            Minute=Second/60
            st.write('converted value is',Minute)
    elif(unit=='Minute'):
        Minute = st.number_input("Minute")
        if Minute !=0:
            Second=Minute/100
            st.write('converted value is',Second)












