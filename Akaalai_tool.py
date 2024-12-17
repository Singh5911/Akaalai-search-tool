import requests
from transformers import pipeline

# Access secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
SEARCH_ENGINE_ID = st.secrets["SEARCH_ENGINE_ID"]

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
