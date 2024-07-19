import sounddevice as sd
from scipy.io.wavfile import write

def get_sound():
    freq = 16000
    dur = 2

    print("Started recording")
    recording = sd.rec(int(dur * freq), samplerate=freq, channels=2)

    sd.wait()
    print("Stopped recording")

    write("recording.wav", freq, recording)

if __name__ == "__main__":
    get_sound()
