import requests
from transformers import pipeline
import streamlit as st

# Access secrets
GOOGLE_API_KEY = st.secrets["AIzaSyDfq5TNZwV7Nd4wkVX8ZxiWk9QLGWrMwlA"]
SEARCH_ENGINE_ID = st.secrets["e1d3fac41bae54986"]

# Hugging Face setup
model_name = "google/flan-t5-base"
text_generator = pipeline("text2text-generation", model=model_name)

# Google Search API
def get_google_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    snippets = [item["snippet"] for item in response.json().get("items", [])]
    return " ".join(snippets)

def ask_ai(query):
    search_results = get_google_results(query)
    prompt = f"Based on this information, answer the query:\n{search_results}\n\nQuery: {query}"
    response = text_generator(prompt, max_length=200, do_sample=True)
    return response[0]["generated_text"]

# Streamlit app
st.title("AI Search Assistant 🔍")
user_query = st.text_input("Enter your query:")
if st.button("Search"):
    with st.spinner("Searching..."):
        response = ask_ai(user_query)
        st.write(response)

    # Step 3: Generate a response
    response = text_generator(prompt, max_length=200, do_sample=True)
    return response[0]["generated_text"]

# Test the script
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    ai_response = ask_ai(user_query)
    print("\nAI Response:")
    print(ai_response)
