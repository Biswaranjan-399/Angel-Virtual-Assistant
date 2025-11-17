import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import time
import google.genai as genai


recognizer = sr.Recognizer()

newsApi = "YOUR_NEWS_API_KEY_HERE"


def speak(text):
    engine = pyttsx3.init()

    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
    except Exception as e:
        print(f"could not set voice: {e}")

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def aiprocess(command):
    # 1. Define the System Instruction (The Core Change)
    system_instruction = (
        "You are ANGEL, a helpful and friendly virtual assistant, similar to Alexa or Siri.Your responses should be concise, helpful, and polite.Do not refer to yourself as a large language model.You are working inside a Python script, and your purpose is to answer the user's queries.Never mention you are an AI model."
    )
    client = genai.Client(api_key="YOUR_GEMINI_API_KEY_HERE")
    print("✅ Gemini client initialized successfully with direct API key.")

    config = genai.types.GenerateContentConfig(
        system_instruction=system_instruction)

    chat = client.chats.create(model='gemini-2.5-flash', config=config)
    MODEL = 'gemini-2.5-flash'

    try:
        response = chat.send_message(command)

        return response.text

    except Exception as e:
        print(f"An error occurred during content generation: {e}")
        return "I encountered an error while processing that command."


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("Opening linkedin")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
        speak("Opening instagram")
    elif "news" in c.lower():
        speak("fetching the top 3 headlines for you.")
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}")
        if r.status_code == 200:
            # parse the json format
            data = r.json()

            # extract the articles
            articles = data.get('articles', [])

            headlines_to_read = []

            # read only for the first 3 headlines
            for i, article in enumerate(articles):
                if i < 3:
                    title = article.get('title')
                    if title:
                        headlines_to_read.append(title)
                    else:
                        break

            if headlines_to_read:
                full_news_text = "The headlines are: " + \
                    ". ".join(headlines_to_read)
                speak(full_news_text)
            else:
                speak("sorry, I could not find anything right now")

    else:
        speak("wait for a while")
        output = aiprocess(c)
        print(output)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Angel......")
    while True:
        # listen from the wake word "Angel"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if ("angel" in word.lower()):
                time.sleep(0.1)
                speak("Yes, how can I help you?")
                # listen for command
                with sr.Microphone() as source:
                    print("Angel Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except sr.WaitTimeoutError:
            print("No speech Detected within timeout")
        except Exception as e:
            print("Error; {0}".format(e))
