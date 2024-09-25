import json

# import postfinance
import streamlit as st

st.set_page_config(layout="wide")

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
# mongo_storage = postfinance.mongo_storage_from_uri(st.secrets.mongodb_atlas.uri)

# Select box
call_id = st.selectbox(
    "Review your transcript",
    # mongo_storage.call_ids,
    [
        "pf_cc_call01",
        "pf_cc_call02",
        "pf_cc_call03",
    ],
    help="Select a transcript for human review",
)

# Get call
# call = mongo_storage.get_call_by_id(call_id)
call = {
    "detected_language": "German",
    "transcript": "placeholder for transcript",
    "translation": "placeholder for translation",
}

# Tabs
tab1, tab2 = st.tabs(["📖 Translate", "📝 Annotate"])

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
        detected_language = call["detected_language"]
        st.markdown(f"**{detected_language}**")
        st.markdown(call["transcript"])

    with col2:
        translation = call["translation"]
        if edit:
            st.markdown("**English**")
            updated_translation = st.text_area(
                "⚠️ Please modify the translation but keep the same Markdown formatting",
                value=translation,
                height=1800,
            )
        else:
            st.markdown("**English**")
            st.markdown(translation)

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
        st.markdown("**Translation**")
        st.markdown(call["translation"])

    with col2:
        # TODO: Display transcript annotation with Markdown formatting
        annotation = json.dumps(
            {"summary": call["summary"], "details": call["details"]},
            indent=4,
            ensure_ascii=False,
        )
        if edit:
            st.markdown("**Annotation**")
            updated_annotation = st.text_area(
                "⚠️ Please modify the annotation but keep the same JSON formatting",
                value=annotation,
                height=1800,
            )
        else:
            st.markdown("**Annotation**")
            st.markdown(f"```json\n{annotation}\n```")

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
