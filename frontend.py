# Step 1: Setup UI with Streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st
import requests

st.set_page_config(page_title="Langraph Agent UI", layout="wide")
st.title("AI Chatbot Agent")
st.write("Create and write with the AI Agent")

system_prompt = st.text_area(
    "Define your AI Agent:", height=70, placeholder="Type your system prompt here"
)

MODELS_NAME_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODELS_NAME_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider: ", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq models", MODELS_NAME_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI models", MODELS_NAME_OPENAI)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area(
    "Enter your query", height=150, placeholder="Ask me anything!"
)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Submit"):
    if user_query.strip():
        # Connect with backen via URL
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search,
        }
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(response_data)
