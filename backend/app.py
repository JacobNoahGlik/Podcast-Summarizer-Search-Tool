from flask import Flask, request, jsonify
from whisper_transcriber import transcribe_audio
from utils.file_io import save_uploaded_file

app = Flask(__name__)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    file_path = save_uploaded_file(audio_file)

    # Mock transcription for now
    transcript = transcribe_audio(file_path)
    
    return jsonify({
        "file": audio_file.filename,
        "transcript": transcript
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
