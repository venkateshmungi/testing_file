import streamlit as st
import os

def save_logger_details(logger_name, log_message):
    with open("logger.txt", "a") as file:
        file.write(f"{logger_name}: {log_message}\n")

def create_password(password):
    with open("password.txt", "w") as file:
        file.write(password)

def delete_log_files(password):
    with open("password.txt", "r") as file:
        stored_password = file.read()
        if password == stored_password:
            os.remove("logger.txt")
            st.write("Log files deleted")
        else:
            st.write("Incorrect password")

def main():
    st.title("Logger Management")
    option = st.selectbox("Select an option:", ("Save Logger Details", "Create Password", "Delete Log Files"))
    
    if option == "Save Logger Details":
        logger_name = st.text_input("Enter logger name:")
        log_message = st.text_input("Enter log message:")
        if st.button("Save"):
            save_logger_details(logger_name, log_message)
            st.write("Logger details saved")
    
    elif option == "Create Password":
        password = st.text_input("Enter password:", type="password")
        if st.button("Create"):
            create_password(password)
            st.write("Password created")
    
    elif option == "Delete Log Files":
        password = st.text_input("Enter password:", type="password")
        if st.button("Delete"):
            delete_log_files(password)
    
if __name__ == "_main_":
    main()