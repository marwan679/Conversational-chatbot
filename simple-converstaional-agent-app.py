import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '...'  # Replace with your actual HuggingFace API token

# 1. Connect to HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="conversational",
    max_new_tokens=512,
)

chat_model = ChatHuggingFace(llm=llm)

# 2. Create Streamlit app
st.title("Simple Conversational Agent App")
st.header("Ask the assistant anything!")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    result = chat_model.invoke(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(result)
    return result.content

def get_text():
    user_input = st.text_input("Your question:", key="input")
    return user_input


user_input = get_text()
submit = st.button("Submit")

if submit and user_input:
    answer = load_answer(user_input)
    st.write("Assistant's answer:")
    st.write(answer)