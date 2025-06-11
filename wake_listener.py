import pvporcupine
import pyaudio
import struct

def listen_for_wakeword():
    porcupine = pvporcupine.create(
    access_key="a6kY2Q7fFi7AiTj58HZ9ikU9hjLfUZ2xneeapT/VsDU2s06xkCDjHA==",
    keywords=["jarvis", "computer", "porcupine"]
)


    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=porcupine.sample_rate,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🎧 Listening for wake word...")  # ✅ This line must be outside any previous statements

    try:
        while True:
            audio = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, audio)

            result = porcupine.process(pcm)
            if result >= 0:
                print("✅ Wake word detected!")
                break

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

# Run it
listen_for_wakeword()
