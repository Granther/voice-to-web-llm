import os
from groq import Groq
from dotenv import load_dotenv

def transcribe():
    load_dotenv()
    groq_key = os.getenv('GROQ_API_KEY')
    client = Groq(api_key=groq_key)

    filename = "recording.wav"

    with open(filename, "rb") as file:
        trans = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            language="en"
        )
    
        print(trans)

        return trans.text
    
if __name__ == "__main__":
    from sound import get_sound
    get_sound()
    transcribe()