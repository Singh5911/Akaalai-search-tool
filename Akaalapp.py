
import streamlit as st
from Akaalai_tool import ask_ai  # Ensure the file name matches exactly and is lowercase

st.title("AI Search Assistant 🔍")
st.write("Get up-to-date answers with real-time internet search and AI!")

# Input box for the user query
user_query = st.text_input("Enter your query here:")

# Button to fetch results
if st.button("Search"):
    if user_query.strip():  # Check if the query is not empty
        with st.spinner("Fetching results..."):
            try:
                response = ask_ai(user_query)
                st.subheader("AI Response:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")
