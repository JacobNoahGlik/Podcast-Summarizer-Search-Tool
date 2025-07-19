import streamlit as st
from pathlib import Path

def upload_audio():
    st.header("Upload your podcast episode")
    uploaded_file = st.file_uploader("Choose a podcast audio file", type=["mp3", "wav"])

    if uploaded_file:
        file_path = Path("examples/uploads") / uploaded_file.name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Uploaded file saved as: {file_path}")
        return file_path
    else:
        st.info("Upload a file to begin.")
        return None
