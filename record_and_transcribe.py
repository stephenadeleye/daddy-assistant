# record_and_transcribe.py

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from modules.speech_to_text import transcribe_audio

def record(duration=5, fs=44100):
    print("🎤 Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write("output.wav", fs, audio)
    print("✅ Recording complete. Transcribing...")
    return transcribe_audio("output.wav")

if __name__ == "__main__":
    print(record())
