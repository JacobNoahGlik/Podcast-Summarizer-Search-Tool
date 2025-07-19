import streamlit as st
from components.upload_widget import upload_audio
from components.transcript_viewer import show_transcript
from components.chapter_display import show_chapters

st.set_page_config(page_title="Podcast Summarizer", layout="wide")
st.title("🎧 Podcast Summarizer & Search Tool")

file_path = upload_audio()

if file_path:
    show_transcript()
    show_chapters()
