import streamlit as st
import openai
from elevenlabs import set_api_key
from elevenlabs import generate, play

# Set your OPENAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set your Eleven Labs API key
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

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input_placeholder = st.empty()
user_input = user_input_placeholder.text_input("You:", value="")

if user_input:
    # Add the user message to the session_state messages
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Handle the LLM call
    with st.chat_message("assistant"):
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
        
        # Append the LLM response to the session_state messages
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )

    # Add the messages to the application's frontend display
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
