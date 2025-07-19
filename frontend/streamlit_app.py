import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Podcast Summarizer", layout="wide")
st.title("🎧 Podcast Summarizer & Search Tool")

# --- Upload Section ---
st.header("Upload your podcast episode")
uploaded_file = st.file_uploader("Choose a podcast audio file", type=["mp3", "wav"])

if uploaded_file:
    file_path = Path("examples/uploads") / uploaded_file.name
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Uploaded file saved as: {file_path}")

    # Placeholder response
    st.header("📄 Transcript (placeholder)")
    st.markdown("""
    **00:00 - 02:00**: Welcome to the show!
    
    **02:01 - 05:00**: Discussing the rise of AI in 2024.
    
    **05:01 - 08:00**: Interview with Dr. Smith on LLM security.
    
    **08:01 - 10:00**: Closing thoughts and next episode teaser.
    """)

    st.header("📚 Chapters")
    st.markdown("""
    1. Introduction
    2. AI Landscape
    3. Expert Interview
    4. Conclusion
    """)

else:
    st.info("Upload a file to begin.")
