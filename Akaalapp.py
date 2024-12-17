import streamlit as st
from ai_tool import ask_ai

st.title("AI Search Assistant 🔍")
st.write("Get up-to-date answers with real-time internet search and AI!")

# Input box for the user query
user_query = st.text_input("Enter your query here:")

# Button to fetch results
if st.button("Search"):
    with st.spinner("Fetching results..."):
        response = ask_ai(user_query)
        st.subheader("AI Response:")
        st.write(response)
