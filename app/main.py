import numpy as np
import streamlit as st
from links import FROH, TRAURIG

# Emojis: 😎 💻 🚀 😢 😁
# mehr Emojis gibt es hier: https://apps.timwhitlock.info/emoji/tables/unicode

state = st.session_state
state["optionen"] = state.get("optionen", False)
optionen = st.button("Optionen")
if optionen:
    state["optionen"] = True

if state["optionen"]:
    musik = st.selectbox("Musik", ["Fröhlich", "Traurig"], key="abc")
    if musik == "Fröhlich":
        st.write("TATA")
    else:
        st.write("MÖÖH")

sample_rate = 44100  # 44100 samples per second
seconds = 20  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.write(True if state == "on" else False)
st.audio(note_la, sample_rate=sample_rate, key="audio")

# if st.button("toggle"):
#     if state == "on":
#         state = "off"
#     else:
#         state = "on"

