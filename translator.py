import streamlit as st
from mtranslate import translate
import pandas as pd
import os
import base64
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# read language dataset
df = pd.read_csv(r"C:\Users\Tharuni\Desktop\NIT\sept month\23rd_NLP Project\simple language translator\language.csv")
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist = tuple(lang)
langcode = df['iso'].to_list()

lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# Layout
st.title("🌍 Language Translator with Voice Options")

# Input
inputtext = st.text_area("Enter text here to translate", height=100)

# Sidebar Options
choice = st.sidebar.radio('🎯 Select Output Language', langlist)
voice_choice = st.sidebar.radio("🗣️ Choose Voice", ("Female", "Male"))
speed_choice = st.sidebar.radio("⚡ Select Speed", ("Normal", "Slow", "Fast"))

# Utility function for file download
def get_binary_file_download_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">📥 Download {file_label}</a>'
    return href

c1, c2 = st.columns([3, 3])

if len(inputtext) > 0:
    try:
        # Translation
        output = translate(inputtext, lang_array[choice])
        with c1:
            st.text_area("✅ Translated Text", output, height=200)

            # Download text file
            with open("translated.txt", "w", encoding="utf-8") as f:
                f.write(output)
            st.markdown(get_binary_file_download_html("translated.txt", "Translated Text"), unsafe_allow_html=True)

        # TTS (Voice with pitch/speed adjustments)
        with c2:
            tts = gTTS(text=output, lang=lang_array[choice], slow=(speed_choice == "Slow"))
            tts.save("lang.mp3")

            # Modify pitch & speed for male/female effect
            sound = AudioSegment.from_file("lang.mp3", format="mp3")

            # Simulate male voice (lower pitch)
            if voice_choice == "Male":
                sound = sound._spawn(sound.raw_data, overrides={
                    "frame_rate": int(sound.frame_rate * 0.8)  # lower pitch
                }).set_frame_rate(sound.frame_rate)

            # Speed control
            if speed_choice == "Fast":
                sound = sound.speedup(playback_speed=1.25)
            elif speed_choice == "Slow":
                sound = sound.speedup(playback_speed=0.85)

            sound.export("final_lang.mp3", format="mp3")

            # Play in Streamlit
            with open("final_lang.mp3", "rb") as f:
                st.audio(f.read(), format="audio/mp3")

            st.markdown(get_binary_file_download_html("final_lang.mp3", "Audio File"), unsafe_allow_html=True)

    except Exception as e:
        st.error(e)
