import streamlit as st
from utils import query_agent

# Basic UI
st.title("CSV_067 App | ready to analyze your CSV files :)")
st.header("Please upload your CSV file here:")

# Input OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Capture the CSV file
data = st.file_uploader("Upload CSV file",type="csv")
query = st.text_area("Enter your query")

# Check if OpenAI API key is available
if openai_api_key:
    # If OpenAI API key is available, show submit button
    button = st.button("Submit")

    if button:
        try:
            # Get Response
            answer = query_agent(data, query, openai_api_key=openai_api_key)
            st.write(answer)
        except Exception as e:
            st.error("OpenAI key is not valid. Please try again with a valid key.")
else:
    st.warning("Please input OpenAI API key.")
