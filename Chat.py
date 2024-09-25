# import postfinance
import streamlit as st

# from postfinance import Settings, StreamlitCallbackHandler

st.set_page_config(layout="wide")

# Settings.watsonx_api_key = st.secrets.ibm_watsonx.api_key
# Settings.watsonx_url = st.secrets.ibm_watsonx.url
# Settings.watsonx_project_id = st.secrets.ibm_watsonx.project_id
# Settings.jina_api_key = st.secrets.jina_embeddings.api_key
# Settings.neo4j_uri = st.secrets.neo4j_aura.uri
# Settings.neo4j_username = st.secrets.neo4j_aura.username
# Settings.neo4j_password = st.secrets.neo4j_aura.password
# Settings.mongo_uri = st.secrets.mongodb_atlas.uri
# Settings.persist_dir = "./.postfinancex/storage"
# # TODO: Optimize global logging for `postfinance` module
# Settings.verbose = True


def new_chat():
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you?"}
    ]


with st.sidebar:
    st.sidebar.button(
        "New chat",
        on_click=new_chat,
        help="Clear chat history and start a new chat",
    )

    st.header("Settings")

    # api_key = st.text_input(
    #     "IBM watsonx.ai API key",
    #     key="api_key",
    #     type="password",
    #     placeholder="Enter the API key",
    #     help="[Get your IBM watsonx.ai API key](https://cloud.ibm.com/apidocs/watsonx-ai)",
    # )

    # TODO: Support loading supported models
    model = st.selectbox(
        "Model",
        [
            "meta-llama/llama-3-70b-instruct",
            "mistralai/mixtral-8x7b-instruct-v01",
        ],
        index=0,
        help="[Select a model for chat](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-choose.html?context=wx&audience=wdp)",
    )

    # TODO: Support loading default model parameters
    if model:
        sampling = True
        temperature = 0.6
        top_p = 0.9
        top_k = 50
        random_seed = 0
        repetition_penalty = 1.0
        min_new_tokens = 0
        max_new_tokens = 1024

    # TODO: Support loading default tools
    tools = ["graph_qa", "vector_search"]

    custom = st.toggle(
        "Custom mode",
        help="Enable Custom mode to customize the model parameters",
    )

    if custom:
        st.divider()

        st.subheader("Tools")

        tools = st.multiselect(
            "Tools",
            [
                "translate",
                "graph_qa",
                "vector_search",
                "summarize",
            ],
            default=tools,
            help="Select tools used for the MRKL system",
        )

        st.subheader("Model parameters")

        sampling = st.toggle(
            "Sampling decoding",
            value=sampling,
            help="Enable Sampling decoding to customize the variability in how tokens are selected",
        )

        if sampling:
            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=2.0,
                value=temperature,
                help="Higher values lead to greater variability",
            )  # float

            top_p = st.slider(
                "Top P",
                min_value=0.0,
                max_value=1.0,
                value=top_p,
                help="Unless you change the value, this setting is not used",
            )  # float

            top_k = st.slider(
                "Top K",
                min_value=0,
                max_value=100,
                value=top_k,
                help="Higher values lead to greater variability",
            )  # int

            random_seed = st.number_input(
                "Random seed",
                min_value=0,
                max_value=4294967295,
                value=random_seed,
                help="To produce repeatable results, set the same random seed value every time; to disable reproducibility, set to 0",
            )  # int

        repetition_penalty = st.slider(
            "Repetition penalty",
            min_value=1.0,
            max_value=2.0,
            value=repetition_penalty,
            help="The higher the penalty, the less likely it is that the result will include repeated text",
        )  # float

        min_new_tokens = st.number_input(
            "Min tokens",
            min_value=0,
            value=min_new_tokens,
            help="Control the maximum number of tokens in the generated tokens, which must be less than or equal to Max tokens",
        )  # int

        # TODO: The maximum number of tokens that are allowed in the output differs by model
        max_new_tokens = st.number_input(
            "Max tokens",
            min_value=min_new_tokens,
            max_value=16384,
            value=max_new_tokens,
            help="Control the maximum number of tokens in the generated tokens",
        )  # int

        "[Learn more](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-parameters.html?context=wx)"

# Title
st.title("💬 Chat")
st.caption("👁️🐝Ⓜ️ Powered by IBM watsonx.ai")

# Info
# st.info(
#     "🛠️ Chat with all the PostFinance CC Call transcripts using Retrieval-Augmented Generation (RAG) is coming soon!"
# )

col1, col2, col3 = st.columns(3)
with col1:
    st.info(
        "How could I update personal information in my account, especially about name change?",
        icon="💡",
    )

with col2:
    st.info(
        "What is the most commonly used language in recorded customer calls?",
        icon="💭",
    )

with col3:
    st.info(
        "Summarize customer needs or purposes of calling in recorded customer calls.",
        icon="📌",
    )

# Text area
# transcript = st.text_area(
#     "Enter your transcript",
#     height=200,
# )

# Chat elements
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if query := st.chat_input():
    # if not api_key:
    #     st.warning(
    #         "Please enter your IBM watsonx.ai API key to continue",
    #         icon="⚠️",
    #     )
    #     st.stop()

    # Get PostFinanceX agent

    # Settings.watsonx_model_id = model

    # if sampling:
    #     Settings.watsonx_model_params.decoding_method = "sample"
    #     Settings.watsonx_model_params.top_p = top_p
    #     Settings.watsonx_model_params.top_k = top_k
    #     Settings.watsonx_model_params.temperature = temperature
    #     Settings.watsonx_model_params.random_seed = random_seed
    #     Settings.watsonx_model_params.repetition_penalty = repetition_penalty
    #     Settings.watsonx_model_params.min_new_tokens = min_new_tokens
    #     Settings.watsonx_model_params.max_new_tokens = max_new_tokens
    # else:
    #     Settings.watsonx_model_params.decoding_method = "greedy"
    #     Settings.watsonx_model_params.repetition_penalty = repetition_penalty
    #     Settings.watsonx_model_params.min_new_tokens = min_new_tokens
    #     Settings.watsonx_model_params.max_new_tokens = max_new_tokens

    # Settings.tools.translate = "translate" in tools
    # Settings.tools.graph_qa = "graph_qa" in tools
    # Settings.tools.vector_search = "vector_search" in tools
    # Settings.tools.summarize = "summarize" in tools

    # agent_executor = postfinance.get_agent_executor()

    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        # st_callback = StreamlitCallbackHandler(st.container())
        # with st.spinner("Thinking ..."):
        #     response = postfinance.chat(
        #         agent_executor,
        #         query,
        #         streamlit_callback=st_callback,
        #     )
        response = "thinking ..."
        if response:
            st.write(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
