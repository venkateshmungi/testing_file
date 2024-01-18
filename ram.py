import streamlit as st

# Set the title of the app
st.markdown(
    """
    <h1 style='font-size: 50px; color: #0070f3;'>CodeBot - A Streamlit and Langchain-powered Coding Assistant</h1>
    """,
    unsafe_allow_html=True
)

# Add a subtitle
st.markdown(
    """
    <h2 style='font-size: 30px; color: #333;'>Your helpful coding companion</h2>
    """,
    unsafe_allow_html=True
)

# Add a background image
def set_page_bg_img():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://example.com/background.jpg");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_page_bg_img()

# Create a text input field
user_input = st.text_input("Enter some text:")

# Display the user input back to the user
st.write("You entered:", user_input)
