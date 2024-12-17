import requests
from transformers import pipeline

# Set up API keys
GOOGLE_API_KEY = "AIzaSyDfq5TNZwV7Nd4wkVX8ZxiWk9QLGWrMwlA"
SEARCH_ENGINE_ID = "e1d3fac41bae54986"

# Hugging Face model (Flan-T5 for natural language tasks)
model_name = "google/flan-t5-base"
text_generator = pipeline("text2text-generation", model=model_name)

# Function to query Google Custom Search API
def get_google_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    results = response.json()
    snippets = []
    for item in results.get("items", []):
        snippets.append(item.get("snippet", ""))
    return " ".join(snippets)

# Function to process the query with Hugging Face
def ask_ai(query):
    # Step 1: Get search results
    search_results = get_google_results(query)
    
    # Step 2: Create a prompt for Hugging Face
    prompt = f"Based on the following information from Google, answer the query:\n\n{search_results}\n\nQuery: {query}"
    
    # Step 3: Generate a response
    response = text_generator(prompt, max_length=200, do_sample=True)
    return response[0]["generated_text"]

# Test the script
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    ai_response = ask_ai(user_query)
    print("\nAI Response:")
    print(ai_response)
