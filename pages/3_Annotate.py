import json

# import postfinance
import streamlit as st

st.set_page_config(layout="wide")

# Sidebar
with st.sidebar:
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
            # "mistralai/mixtral-8x7b-instruct-v01",
        ],
        index=0,
        help="[Select a model for translation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-choose.html?context=wx&audience=wdp)",
    )

    # TODO: Support loading default model parameters
    if model:
        sampling = False
        temperature = 0.1
        top_p = 1.0
        top_k = 50
        random_seed = 0
        repetition_penalty = 1.0
        min_new_tokens = 0
        max_new_tokens = 1024

    custom = st.toggle(
        "Custom mode",
        help="Enable Custom mode to customize the model parameters",
    )

    if custom:
        st.divider()

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
st.title("📝 Annotate")
st.caption("👁️🐝Ⓜ️ Powered by IBM watsonx.ai")

# File uploader
# uploaded_file = st.file_uploader(
#     "Upload your transcript",
#     type=("txt", "md"),
# )
# if uploaded_file:
#     text = uploaded_file.read().decode("utf-8")

# Text area
transcript = st.text_area(
    "Enter your transcript",
    height=200,
)

if transcript:
    # if not api_key:
    #     st.warning(
    #         "Please enter your IBM watsonx.ai API key to continue",
    #         icon="⚠️",
    #     )
    #     st.stop()

    # Get PostFinanceX agent
    # annotator = postfinance.get_annotator()
    annotator = "placeholder for annotator"


# Button
submitted = st.button("Submit", type="primary")


response = None
generated = False

if submitted:
    # JSON output
    st.markdown("**JSON Output**")

    with st.spinner("Please wait ..."):
        # response = postfinance.annotate(
        #     annotator,
        #     transcript,
        #     params=(
        #         {
        #             "decoding_method": "sample",
        #             "temperature": temperature,
        #             "top_p": top_p,
        #             "top_k": top_k,
        #             "random_seed": random_seed,
        #             "repetition_penalty": repetition_penalty,
        #             "min_new_tokens": min_new_tokens,
        #             "max_new_tokens": max_new_tokens,
        #         }
        #         if sampling
        #         else {
        #             "decoding_method": "greedy",
        #             "repetition_penalty": repetition_penalty,
        #             "min_new_tokens": min_new_tokens,
        #             "max_new_tokens": max_new_tokens,
        #         }
        #     ),
        #     dumps=True,
        # )
        response = {
            "summary": "placeholder for summary",
            "details": "placeholder for details",
        }

        generated = True

    if response:
        st.markdown(f"```json\n{response}\n```")

    # Columns
    response = json.loads(response)

    if response:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Transcript**")
            st.markdown(transcript)

        with col2:
            st.markdown("**Annotation**")
            st.markdown(response["details"])

if submitted and generated:
    st.info("Please refresh the page to continue", icon="💡")
