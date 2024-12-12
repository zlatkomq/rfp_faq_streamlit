import streamlit as st
from my_project.core import hello_world

# Set page config
st.set_page_config(
    page_title="My Project",
    page_icon="👋",
    layout="centered"
)

# Add a title
st.title("Welcome to My Project! 👋")

# Add a text input for the name
name = st.text_input("Enter your name:", "World")

# Display the greeting
greeting = hello_world(name)
st.write(greeting)

# Add some styling
st.markdown("""
    <style>
        .stTitle {
            color: #2E86C1;
        }
        .stTextInput {
            max-width: 300px;
        }
    </style>
""", unsafe_allow_html=True) 