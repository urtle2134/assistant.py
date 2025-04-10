🚀 Features

    🎙️ Speech Recognition via Google Web Speech API

    🧠 Keyword Activation: Listens for “Hey Assistant” to begin command processing

    ⚙️ Processes at least 5 voice commands:

        "What time is it?" – Returns current system time

        "Search for [query]" – Opens browser with Google search results

        "Tell me a joke" – Speaks a joke using the pyjokes library

        "What’s the weather like?" – Fetches current weather data using OpenWeatherMap API

        "Set a timer for [X] seconds" – Sets a countdown timer

    🔊 Text-to-Speech responses via pyttsx3

    🛡️ Error Handling for unrecognized input or API issues
   
    🧰 Requirements

Make sure Python 3.7+ is installed. Then install dependencies with:

pip install SpeechRecognition pyttsx3 pyjokes requests pyaudio

    If you have issues installing pyaudio, try:

        Windows: Use prebuilt wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

        Mac/Linux: brew install portaudio or sudo apt install portaudio19-dev
        🌦️ Setup Weather API (Optional)

To enable weather command, get a free API key from OpenWeatherMap and add it to the script:

API_KEY = "your_openweathermap_api_key"

You can also change the default city (CITY = "New York") to your preferred location.
🧪 Usage

    Run the script:

python assistant.py

Say “Hey Assistant” to activate the assistant.

Then speak one of the supported commands.

🏅 Bonus Features (Optional Enhancements)

    🖥️ Add a GUI using tkinter to display command history

    🔁 Implement continuous listening using background threads

    📅 Add calendar reminders or alarms

    🌐 Add multi-language support using Whisper or recognizer language settings

    🧠 Integrate Whisper for advanced transcription:

pip install openai-whisper
🤖 Example Commands

    "Hey Assistant, what time is it?"

    "Hey Assistant, search for ChatGPT"

    "Hey Assistant, tell me a joke"

    "Hey Assistant, what's the weather like?"

    "Hey Assistant, set a timer for 10 seconds"
