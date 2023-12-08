import streamlit as st
import string
import random

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Password Generator")

    password_length = st.number_input("Enter password length", min_value=4, max_value=50, value=16)
    include_symbols = st.checkbox("Include Symbols")

    if st.button("Generate Password"):
        generated_password = generate_password(password_length, include_symbols)
        st.success(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
