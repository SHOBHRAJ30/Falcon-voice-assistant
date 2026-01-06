"""
===================================================
🦅 FALCON v5.0 - Advanced AI Voice Assistant
===================================================
Author      : shobhraj bhattacharjee
Version     : 5.0
Description : Stable, upgraded voice assistant with
              YouTube, Google, apps, jokes & AI replies.
===================================================
"""

# ==========================
# IMPORTS
# ==========================
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import time
import os
import sys

# ==========================
# CONFIG
# ==========================
ASSISTANT_NAME = "Falcon"
VOICE_RATE = 175
LANG = "en-in"

# ==========================
# TEXT TO SPEECH
# ==========================
engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)

def speak(text):
    print(f"{ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()

# ==========================
# GREETING
# ==========================
def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Falcon version five. Speak your command.")

# ==========================
# LISTEN (STABLE)
# ==========================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            return ""

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language=LANG)
        print("USER SAID ➜", query)
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Internet connection problem")
        return ""

# ==========================
# JOKES
# ==========================
def tell_joke():
    jokes = [
        "Why do programmers hate nature? Too many bugs.",
        "I told my computer I needed a break, it said no problem I will freeze.",
        "Why did the developer go broke? Because he used up all his cache."
    ]
    speak(random.choice(jokes))

# ==========================
# COMMAND HANDLER
# ==========================
def handle_command(query):

    if not query:
        speak("I did not hear anything")
        return

    # TIME
    if "time" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # DATE
    elif "date" in query:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    # YOUTUBE
    elif "youtube" in query:
        speak("Opening YouTube")
        webbrowser.open_new_tab("https://www.youtube.com")

    # PLAY SONG
    elif "play" in query:
        song = query.replace("play", "").replace("on youtube", "").strip()
        if song:
            speak(f"Playing {song} on YouTube")
            webbrowser.open_new_tab(
                f"https://www.youtube.com/results?search_query={song}"
            )
        else:
            speak("What should I play")

    # GOOGLE
    elif "google" in query:
        speak("Opening Google")
        webbrowser.open_new_tab("https://www.google.com")

    # WIKIPEDIA
    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "").strip()
        if topic:
            speak("Searching Wikipedia")
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("No result found")
        else:
            speak("Say the topic name")

    # OPEN APPS
    elif "open chrome" in query:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "open vscode" in query or "open vs code" in query:
        speak("Opening Visual Studio Code")
        os.system("code")

    # JOKE
    elif "joke" in query:
        tell_joke()

    # EXIT
    elif "exit" in query or "quit" in query or "stop" in query:
        speak("Goodbye. Have a nice day.")
        sys.exit()

    # AI STYLE FALLBACK
    else:
        speak("I am still learning. Please try another command.")

# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    wish_me()
    while True:
        cmd = listen()
        handle_command(cmd)
        time.sleep(0.5)
