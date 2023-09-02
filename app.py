from elevenlabs import set_api_key
from elevenlabs import generate, play

ELEVEN_KEY = ["ELEVEN_KEY"]
set_api_key(ELEVEN_KEY)

def stream_audio_response(input, voice="Bella"):
    audio = generate(
        text=input,
        voice=voice,
        model="eleven_multilingual_v2",
    )
    play(audio)
