import streamlit as st
st.write("My first application")
st.write("This is the app created using streamlit")
slider_val=st.slider("Select a number", 0, 100, 25)
st.write(f"You have selected {slider_val}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")