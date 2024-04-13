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
st.title("💡 Annotate")
st.caption("👁️🐝Ⓜ️ Powered by IBM watsonx.ai")

# File uploader
# uploaded_file = st.file_uploader("Upload your transcript", type=("txt", "md"))


# Text area
text = st.text_area(
    "Enter your transcript",
    height=200,
)

if text:
    # Get PostFinance agent
    if not api_key:
        st.info("Please enter your IBM watsonx.ai API key to continue")
        st.stop()
    agent = Agent(api_key=api_key)


# Submit button
submitted = st.button("Submit", type="primary")
if submitted:
    with st.spinner("Please wait ..."):
        response = agent.annotate(
            model="ibm-mistralai/mixtral-8x7b-instruct-v01-q",
            params={"max_new_tokens": 1000},
            content=text,
        )

    if response:
        st.info(response)
