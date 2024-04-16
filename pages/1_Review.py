import postfinance
import streamlit as st

# Sidebar
with st.sidebar:
    st.header("Settings")

    edit = st.toggle(
        "Edit mode",
        help="Enable Edit mode to modify the transcript records",
    )

    # TODO: Add link to our documentation
    "[Learn more]()"

# Title
st.title("🔎 Review")
st.caption("👁️🐝Ⓜ️ Powered by IBM watsonx.ai")

# Get PostFinanceX agent
agent = postfinance.Agent(
    st.secrets.ibm_watsonx.api_key,
    st.secrets.mongodb_atlas.uri,
)

# Select box
transcript_id = st.selectbox(
    "Review your transcript",
    agent.storage.list_transcripts(),
    help="Select a transcript for human review",
)

# Get transcript
transcript = agent.storage.get_by_transcript_id(transcript_id)

# Tabs
tab1, tab2 = st.tabs(["📝 Translate", "💭 Annotate"])

with tab1:

    # Caption
    # TODO: Display by transcript translation verification status
    # st.caption("✅ Translation was verified by PostFinance Human Reviewer 💪")
    st.caption(
        "❗ Translation was automatically done by PostFinanceX Vitual Assistant 🦾"
    )

    # Columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(transcript["transcript"]["markdown"])

    with col2:
        if edit:
            updated_translation = st.text_area(
                "⚠️ Please modify the translation but keep the same Markdown formatting",
                value=transcript["translation"]["markdown"],
                height=1800,
            )
        else:
            st.markdown(transcript["translation"]["markdown"])

    # Button
    if edit:
        submitted = st.button(
            "Submit",
            key="translation_submission",
            type="primary",
        )
        if submitted:
            # TODO: Update transcript translation and reflect on transcript annotation

            st.info("💡 Please refresh the page to continue")
    else:
        verified = st.button(
            "Well Done!",
            key="translation_verification",
            type="primary",
        )
        if verified:
            # TODO: Update transcript translation verification status

            st.balloons()

with tab2:

    # Caption
    # TODO: Display by transcript annotation verification status
    # st.caption("✅ Translation was verified by PostFinance Human Reviewer 💪")
    st.caption(
        "❗ Annotation was automatically done by PostFinanceX Vitual Assistant 🦾"
    )

    # Columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(transcript["translation"]["markdown"])

    with col2:
        if edit:
            updated_annotation = st.text_area(
                "⚠️ Please modify the annotation but keep the same Markdown formatting",
                value=transcript["annotation"]["markdown"],
                height=1800,
            )
        else:
            st.markdown(transcript["annotation"]["markdown"])

    # Button
    if edit:
        submitted = st.button(
            "Submit",
            key="annotation_submission",
            type="primary",
        )
        if submitted:
            # TODO: Update transcript annotation

            st.info("💡 Please refresh the page to continue")
    else:
        verified = st.button(
            "Well Done!",
            key="annotation_verification",
            type="primary",
        )
        if verified:
            # TODO: Update transcript annotation verification status

            st.balloons()
