import sounddevice as sd
from scipy.io.wavfile import write

def get_sound(seconds: int = 5, return_type: str = None):
    FREQ = 16000 # 16000 is the required freq for Whisper

    if not isinstance(seconds, int) or seconds <= 0:
        raise ValueError("The seconds parameter must be a psotive integer")
    if return_type not in (None, "array"):
        raise ValueError("The 'return_type' parameter must be either 'array' or None.")

    print("Started recording...")
    recording = sd.rec(int(seconds * FREQ), samplerate=FREQ, channels=2)
    sd.wait()
    print("Stopped recording")

    if return_type == "array":
        return recording
    else:
        try:
            write("recording.wav", FREQ, recording)
        except Exception as e:
            print(f"An error occured while attempting to write the audio recording: {e}")
            return None
    return None
