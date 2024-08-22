import os
import streamlit as st

from groq import Groq

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"), # Ensure the GROQ_API_KEY is set in your environment variables.
)

# Function to get a response from Groq API.
def get_groq_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192", # Specify the model you want to use.
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Groq API")

user_prompt = st.text_input("**Enter your prompt**", placeholder="Type your prompt here...")

# Display response only when the user submits a prompt.
if st.button("Generate Response"):
    if user_prompt:
        with st.spinner("Generating response..."):
            response = get_groq_response(user_prompt)
        st.markdown(response)
    else:
        st.warning("Please enter a prompt before submitting.")
