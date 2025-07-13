# 🎧 Podcast Summarizer & Search Tool

A smart tool to help you **transcribe**, **summarize**, **chapterize**, and **search** podcast episodes with ease.

---

## 🚀 Project Goal

Turn long-form podcast audio into **searchable**, **structured**, and **summarized** content using AI.

### The End Product:
- 🎙 Upload a podcast episode (`.mp3`, `.wav`)
- 📝 Automatically transcribe the audio using Whisper
- 📚 Summarize and break into chapters/topics
- 🔍 Search across episodes using natural language ("When did they talk about privacy laws?")
- 🌐 Simple web UI to interact with your library

---

## 🛠️ Tech Stack

| Component        | Tool / Library                       |
|------------------|--------------------------------------|
| Transcription     | OpenAI Whisper / Faster Whisper.cpp |
| Summarization     | OpenAI GPT-3.5 / LLM API / Transformers |
| Audio Processing  | `pydub`, `ffmpeg`, `whisper`         |
| Backend           | Python + Flask / FastAPI             |
| Frontend          | Streamlit or React (TBD)             |
| Search Engine     | FAISS / Sentence Transformers / ElasticSearch (lightweight option first) |
| Storage           | Local disk (staging) → S3 optional   |

---

## 🔄 Workflow

### 1. Upload & Transcribe
- User uploads an audio file
- Audio is chunked and passed to Whisper for transcription

### 2. Split & Summarize
- Transcription is segmented (e.g., every 2–5 minutes or speaker change)
- Each segment gets a GPT-based summary
- Optional: create chapters based on semantic similarity

### 3. Index & Search
- Store all summaries in vector DB or simple keyword index
- User can enter natural-language search queries (e.g., "explain blockchain")
- Matches are shown with timestamps + excerpts

### 4. View & Export
- Full transcript with timestamps
- Chaptered view
- Download as `.txt`, `.pdf`, `.json`

---

## 📦 Planned Features (MVP → v1)

### ✅ MVP
- [ ] Upload audio
- [ ] Whisper transcription
- [ ] Chunk and summarize using GPT API
- [ ] Display full transcript and summaries
- [ ] Simple web UI

### 🔜 v1 Goals
- [ ] Chapter creation based on semantic topics
- [ ] Search via keyword + semantic embeddings
- [ ] Export options
- [ ] Save sessions / audio uploads
- [ ] Add audio player synced to transcript

---

## 👤 Target Users

- Students and researchers wanting to skim podcasts
- Content creators summarizing their own episodes
- Anyone with too many podcast episodes and not enough time

---

## 💡 Inspiration

Built to solve a real-world problem: podcasts are long, and time is short. This tool makes it easy to jump to what matters.

---

## 📁 Project Structure (planned)
```yaml
podcast-summarizer/
│
├── backend/
│ ├── app.py
│ ├── whisper_transcriber.py
│ ├── summarizer.py
│ └── search_index.py
│
├── frontend/ (optional: Streamlit or React)
│ └── ...
│
├── examples/
│ ├── sample_episode.mp3
│ └── outputs/
│ ├── transcript.txt
│ ├── summary.json
│ └── chapters.txt
│
├── README.md
└── requirements.txt
```

## ⚙️ Requirements

```bash
pip install -r requirements.txt
```
