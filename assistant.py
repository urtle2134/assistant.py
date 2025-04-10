# assistant.py
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import requests
import threading
from config import OPENWEATHER_API_KEY, CITY

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print("User:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I’m having trouble accessing the speech service.")
            return ""

def start_timer(seconds):
    speak(f"Timer set for {seconds} seconds.")
    threading.Timer(seconds, lambda: speak("Time's up!")).start()

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url).json()
        temp = response['main']['temp']
        desc = response['weather'][0]['description']
        speak(f"The temperature in {CITY} is {temp}°C with {desc}.")
    except:
        speak("Unable to fetch weather information.")

def process_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "joke" in command:
        speak(pyjokes.get_joke())
    elif "weather" in command:
        get_weather()
    elif "set a timer for" in command:
        try:
            seconds = int(command.split("set a timer for")[1].strip().split()[0])
            start_timer(seconds)
        except:
            speak("I couldn't understand the timer duration.")
    else:
        speak("Sorry, I didn’t catch that.")

def assistant_loop():
    ACTIVATION = "hey assistant"
    while True:
        command = listen()
        if ACTIVATION in command:
            speak("How can I help you?")
            command = listen()
            process_command(command)

if __name__ == "__main__":
    assistant_loop()
