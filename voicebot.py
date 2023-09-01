import streamlit as st
from elevenlabs import set_api_key, generate, play

# Set your Eleven Labs API key
ELEVEN_KEY = st.secrets[""]
set_api_key(ELEVEN_KEY)

# Create a function to stream audio response
def stream_audio_response(input, voice="Bella"):
    audio = generate(
        text=input,
        voice=voice,
        model="eleven_multilingual_v2",
    )
    play(audio)

# Create the Streamlit app
st.title("Text-to-Speech Demo")

# Add a button to trigger the voice output
if st.button("Test Voice Output", key="voice_button"):
    stream_audio_response("This is a test")
    stream_audio_response("이것은 테스트입니다")
    stream_audio_response("The Korean word for cat is 고양이!")
    stream_audio_response("The Korean word for cat is")
    stream_audio_response("고양이!")
