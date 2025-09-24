# -Language-Translator-with-Voice-Options
A simple yet powerful **Language Translator Web App** built with **Python, Streamlit, gTTS, and pydub**.   This app lets you **translate text into multiple languages**, and then listen to it in **male or female voice** with adjustable speed (Slow, Normal, Fast).

## ✨ Features
- ✅ Translate text into 60+ languages using `mtranslate`.
- ✅ Listen to translated text in **Male** or **Female** voice.
- ✅ Control speech speed: `Slow`, `Normal`, or `Fast`.
- ✅ Download translated **text file** and **audio file**.
- ✅ Built with **Streamlit** for a clean and interactive UI.

---
## 🖼️ Demo
<img width="1823" height="828" alt="Screenshot 2025-09-24 163524" src="https://github.com/user-attachments/assets/a895f700-e896-4e41-b4f3-0028228c6bfa" />

## ⚙️ Tech Stack
- **Python**
- **Streamlit**
- **mtranslate**
- **gTTS** (Google Text-to-Speech)
- **pydub** (for pitch/speed adjustments)
- **ffmpeg** (required for audio processing)

---

## 🚀 Installation

Clone this repository
```bash
git clone https://github.com/your-username/language-translator.git
cd language-translator
```
Install dependencies
Install FFmpeg

Windows:

Install via ```winget install ffmpeg```
OR download from ffmpeg.org
 and add it to PATH.
Run the app
### 📂 Project Structure
📦 language-translator
 ┣ 📜 app.py              # Main Streamlit app
 ┣ 📜 language.csv        # Supported language codes
 ┣ 📜 demo.png            # Screenshot for README
 ┗ 📜 README.md           # Project Documentation
## 📥 Requirements
streamlit
mtranslate
gTTS
pydub
pandas
---
 🎯 Usage

Enter your text in the text box.

Choose target language from the sidebar.

Select Voice (Male/Female) and Speed (Normal/Slow/Fast).

Click Translate → get the translated text.

Click 🔊 Listen → hear the audio.

Download text or audio file for offline use.

🙌 Future Improvements

Add voice cloning for more natural male/female sounds.

Use APIs like Azure Cognitive Services / Amazon Polly / ElevenLabs for realistic voices.

Deploy on Streamlit Cloud or Heroku for public access.
