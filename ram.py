import streamlit as st

# Set the title of the app
st.title("BHAARATHI-AI")

# Create a text input field
user_input = st.text_input("Enter some text:")

# Display the user input back to the user
st.write("You entered:", user_input)
