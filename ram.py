import streamlit as st

# Set the title of the app
st.markdown(
    """
    <style>
    h1.title {
        font-size: 70px;
        color: #0070f3;
        text-align: right;
    }
    h2.subtitle {
        font-size: 30px;
        color: #333;
        text-align: right;
    }
    </style>
    <h1 class="title">BHAARATHI-AI</h1>
    <h3 class="subtitle">Wii be launching soon</h3>
    """,
    unsafe_allow_html=True
)

# Add a background image
def set_page_bg_img():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://wallpaperaccess.com/full/2718668.jpg");
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
