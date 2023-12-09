import streamlit as st

st.title('Largest amongst 3 numbers')

number1 = st.number_input('Insert first number')
number2 = st.number_input('Insert second number')
number3 = st.number_input('Insert third number')

st.write('The max number is ', max(number1,number2,number3 ))