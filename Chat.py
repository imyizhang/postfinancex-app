import streamlit as st
from postfinance import Agent

# Sidebar
with st.sidebar:
    api_key = st.text_input(
        "IBM watsonx.ai API key",
        key="api_key",
        type="password",
    )
    "[Get your IBM watsonx.ai API key](https://cloud.ibm.com/apidocs/watsonx-ai)"

# Title
st.title("💬 Chat")
st.caption("👁️🐝Ⓜ️ Powered by IBM watsonx.ai")


# Text area
text = st.text_area(
    "Enter your transcript",
    height=200,
)


# Chat elements
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user query
if query := st.chat_input():
    # Get PostFinance agent
    if not api_key:
        st.info("Please enter your IBM watsonx.ai API key to continue")
        st.stop()
    agent = Agent(api_key=api_key)

    # Display user query
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    # Get agent response
    response = agent.chat(
        model="ibm-mistralai/mixtral-8x7b-instruct-v01-q",
        params={"max_new_tokens": 1000},
        content=query,
        messages=st.session_state.messages,
    )

    # Display agent response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
