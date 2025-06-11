import whisper

model = whisper.load_model("base")  # You can change to "small", "medium", etc.

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]
