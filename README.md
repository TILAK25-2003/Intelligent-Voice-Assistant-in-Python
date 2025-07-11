 Intelligent Voice Assistant in Python

````markdown
 🤖 Intelligent Voice Assistant using Python

This project is a Python-based intelligent voice assistant that can recognize your voice and perform useful tasks like:

- Playing YouTube videos
- Telling jokes
- Giving weather updates
- Reading latest news headlines
- Searching on Wikipedia
- Telling the current time
- Sending WhatsApp messages

Developed by: **Tilak Maity**

---

 🚀 Features

- ✅ Speech-to-Text and Text-to-Speech
- ✅ Wikipedia Search
- ✅ YouTube Music Playback
- ✅ Tell Jokes with `pyjokes`
- ✅ Live Weather Forecast using OpenWeather API
- ✅ Latest News Headlines using NewsAPI
- ✅ Send WhatsApp messages using `pywhatkit`
- ✅ Voice Interaction in Indian English

---

 🧑‍💻 How It Works

1. Listens to your voice
2. Recognizes and converts voice to text
3. Matches it with a known command
4. Performs that action and replies using speech

---

 🧱 Tech Stack & Libraries

This assistant is built in **Python 3.10+** and uses the following libraries:

```txt
SpeechRecognition
pyttsx3
wikipedia
pywhatkit
pyjokes
requests
pyaudio
````

---
 🛠️ Setup Instructions

 🔧 1. Clone or Download the Project

```bash
git clone https://github.com/TILAK25-2003/Intelligent-Voice-Assistant-in-Python.git
cd voice-assistant
```

### 📦 2. Install the Required Libraries

If you're using Python outside conda:

```bash
pip install -r requirements.txt
```

If you're using Conda:

```bash
conda install -c anaconda pyaudio
pip install -r requirements.txt
```

---

🔑 3. Configure API Keys

To enable **weather** and **news** features:

* Get a **free API key** from:

  * 🌤️ OpenWeatherMap: [https://openweathermap.org/api](https://openweathermap.org/api)
  * 📰 NewsAPI: [https://newsapi.org](https://newsapi.org)

* In `assistant.py`, replace:

```python
api_key = "your_openweather_api_key"
```

and

```python
api_key = "your_news_api_key"
```

with your actual keys.

---

 ▶️ How to Run the Project

From the terminal, run:

```bash
python assistant.py
```

---

🗣️ Sample Voice Commands You Can Try

| Say This...                    | What It Does                     |
| ------------------------------ | -------------------------------- |
| `play shape of you`            | Plays the song on YouTube        |
| `what is the weather in Delhi` | Gives live weather info          |
| `tell me a joke`               | Responds with a joke             |
| `send WhatsApp message`        | Schedules a message via WhatsApp |
| `what is Python Wikipedia`     | Searches and speaks summary      |
| `what time is it`              | Says the current time            |
| `open YouTube`                 | Opens YouTube in browser         |
| `exit` or `quit`               | Ends the assistant session       |

---
 🛑 Common Errors and Fixes

 🎤 Microphone not working?

* Make sure microphone access is **enabled in system settings**
* Use a wired headset for best results

 ❌ `No Default Input Device Available`?

* Mic is either **not connected** or **not selected** as default
* Go to Windows `Sound Settings` → Select proper input device

---

📂 Project Structure

```
voice-assistant/
│
├── assistant.py           # Main assistant logic
├── requirements.txt       # Required Python libraries
├── README.md              # This guide file
└── .env (optional)        # For API key storage (use dotenv if added)
```

---

📸 Screenshots or Demos

> You can add screenshots of your terminal or assistant running here.

---

## 📜 License

This project is made for educational purposes and is open for modification.

---
 🙋‍♂️ Created By

**Tilak Maity**
B.Tech CSE Student (haldia institute of tecghnology)
