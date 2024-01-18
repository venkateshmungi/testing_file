import streamlit as st

# Set the title of the app
st.title("Chatbot: A Bhaarathi-ai powered Coding Assistant")

# Add a subtitle
st.subheader("Your helpful coding companion")

# Add a background image
st.markdown("""
<style>
body {
background-image: url("https://wallpaperaccess.com/full/2718668.jpg");
background-size: cover;
}
</style>
""", unsafe_allow_html=True)

# Create a text input field
user_input = st.text_input("Enter some text:")

# Display the user input back to the user
st.write("You entered:", user_input)
