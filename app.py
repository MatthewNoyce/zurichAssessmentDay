import streamlit as st

st.title("User Information Form")

st.write("Please enter your details below:")

# Create input fields
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email Address")

# Submit button
if st.button("Submit"):
    if first_name and last_name and email:
        st.success("Thank you for submitting your information!")
        st.write(f"**Name:** {first_name} {last_name}")
        st.write(f"**Email:** {email}")
    else:
        st.error("Please fill in all fields.")
