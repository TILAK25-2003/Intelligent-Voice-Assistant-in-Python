import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speech rate

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your intelligent assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, phrase_time_limit=5)
        except Exception as e:
            print(f"[DEBUG] Listening failed: {e}")
            return None

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        command = command.lower().strip()
        print(f"[DEBUG] You said: {command}")
        return command
    except sr.UnknownValueError:
        print("[DEBUG] Could not understand audio.")
        speak("Sorry, I didn't understand.")
        return None
    except sr.RequestError:
        print("[DEBUG] Recognition service error.")
        speak("Sorry, the service is unavailable.")
        return None

def get_weather(city):
    api_key = "your_openweather_api_key"  # Replace with your OpenWeather API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response['cod'] == 200:
            temp = response['main']['temp']
            description = response['weather'][0]['description']
            speak(f"The temperature in {city} is {temp}°C with {description}.")
        else:
            speak("City not found.")
    except Exception as e:
        print(f"[DEBUG] Weather API error: {e}")
        speak("Unable to get weather details.")

def get_news():
    api_key = "67d633722e6d48c2bd7a9c1e86e0c3a6"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        response = requests.get(url).json()
        articles = response['articles'][:5]
        for i, article in enumerate(articles, 1):
            speak(f"News {i}: {article['title']}")
    except Exception as e:
        print(f"[DEBUG] News API error: {e}")
        speak("Couldn't fetch news at the moment.")

def send_whatsapp_message():
    speak("Please say the phone number with country code.")
    number = take_command()
    if not number:
        speak("Invalid phone number.")
        return
    number = number.replace(" ", "")
    
    speak("What message should I send?")
    message = take_command()
    if not message:
        speak("No message given.")
        return

    try:
        speak("At what hour? (24 hour format)")
        hour = int(take_command())
        speak("At what minute?")
        minute = int(take_command())
        pywhatkit.sendwhatmsg(f"+{number}", message, hour, minute)
        speak("Message scheduled successfully.")
    except Exception as e:
        print(f"[DEBUG] WhatsApp error: {e}")
        speak("Couldn't schedule the message.")

def main():
    wish_me()
    while True:
        query = take_command()
        if not query:
            print("[DEBUG] Empty or None input received.")
            continue

        # Wikipedia
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except Exception as e:
                print(f"[DEBUG] Wikipedia error: {e}")
                speak("No results found on Wikipedia.")

        # Open websites
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Play music
        elif "play" in query:
            song = query.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        # Time
        elif "time" in query or "what time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        # Joke
        elif "joke" in query or "make me laugh" in query:
            speak(pyjokes.get_joke())

        # Weather
        elif "weather" in query:
            speak("Which city?")
            city = take_command()
            if city:
                get_weather(city)

        # News
        elif "news" in query or "headlines" in query:
            speak("Fetching top news headlines.")
            get_news()

        # WhatsApp
        elif "send whatsapp" in query or "whatsapp message" in query:
            send_whatsapp_message()

        # Exit
        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a nice day.")
            break

        # Fallback
        else:
            print(f"[DEBUG] Command not matched: '{query}'")
            speak("Sorry, I don't understand that.")

if __name__ == "__main__":
    main()
