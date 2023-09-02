import streamlit as st
from elevenlabs import set_api_key, generate, play

# Set your Eleven Labs API key

def set_api_key():
    # Get the Eleven Labs API key from the user
    api_key = st.text_input("Enter your Eleven Labs API key:")
    
    # Store the API key as a secret
    st.secrets["ELEVEN_KEY"] = api_key

def main():
    st.title("My Streamlit App")
    
    # Add a button to set the API key
    if st.button("Set Eleven Labs API Key"):
        set_api_key()
        
    # Use the API key in your app
    api_key = st.secrets["ELEVEN_KEY"]
    
    # Rest of your Streamlit app logic here
    # You can use the `api_key` variable to make API requests
    
if __name__ == "__main__":
    main()

ELEVEN_KEY = st.secrets["ELEVEN_KEY"]
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
