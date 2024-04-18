import speech_recognition as sr
import pyttsx3
import datetime

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Dataset of questions and answers
qa_dataset = {
    "how are you": "I'm fine, thank you!",
    "what is your name": "I'm your virtual assistant!",
    "what can you do": "I can tell you the time and date, and answer simple questions. You can ask me anything!",
    "what is the time": datetime.datetime.now().strftime("%H:%M"),
    "what is the date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "goodbye": "Goodbye! Have a great day!",
    "who created you": "I was created by a team of developers at OpenAI.",
    "where are you from": "I exist in the digital realm, but my creators are from various parts of the world.",
    "what is the weather today": "I'm sorry, I don't have access to real-time weather data at the moment.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the capital of France": "The capital of France is Paris.",
    "who is the president of the United States": "As of my last update, the president of the United States is Joe Biden.",
    "how far is the moon": "The average distance from Earth to the Moon is about 384,400 kilometers.",
    "what is the meaning of life": "That's a deep question! Philosophers have debated it for centuries, but there's no definitive answer.",
    "can you sing a song": "I'm sorry, but I'm not programmed to sing. How about I tell you a fun fact instead?",
    "what is the population of China": "As of the latest data, the population of China is over 1.4 billion.",
    "what is the tallest mountain in the world": "Mount Everest is the tallest mountain in the world, with a height of over 8,848 meters.",
    "what is the boiling point of water": "The boiling point of water at sea level is 100 degrees Celsius or 212 degrees Fahrenheit.",
    "what is the currency of Japan": "The currency of Japan is the Japanese yen.",
    "what is the largest ocean in the world": "The largest ocean in the world is the Pacific Ocean.",
    "what is the capital of Australia": "The capital of Australia is Canberra.",
    "who wrote the play 'Romeo and Juliet'": "The play 'Romeo and Juliet' was written by William Shakespeare.",
    "what is the speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
    "what is the national flower of Japan": "The national flower of Japan is the cherry blossom, also known as Sakura.",
    "what is the main ingredient in guacamole": "The main ingredient in guacamole is avocado.",
    "how many continents are there": "There are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia (Oceania), and South America.",
    "what is the largest desert in the world": "The largest desert in the world is the Sahara Desert in Africa.",
    "who painted the Mona Lisa": "The Mona Lisa was painted by Leonardo da Vinci.",
    "what is the speed limit on highways": "Speed limits vary by location, but on many highways, the speed limit is typically around 65-75 miles per hour (105-120 kilometers per hour).",
    "what is the chemical symbol for gold": "The chemical symbol for gold is Au, derived from the Latin word 'aurum'.",
    "what is the tallest animal in the world": "The tallest animal in the world is the giraffe.",
    "what is the capital of Brazil": "The capital of Brazil is Brasília.",
    "what is the distance between Earth and Mars": "The distance between Earth and Mars varies depending on their positions in their orbits. On average, it's about 225 million kilometers.",
    "what is the national animal of Australia": "The national animal of Australia is the red kangaroo.",
    "what is the deepest ocean trench": "The deepest ocean trench is the Mariana Trench in the Pacific Ocean, with a depth of about 11,034 meters.",
    "who discovered penicillin": "Penicillin was discovered by Alexander Fleming in 1928.",
    "what is the capital of Italy": "The capital of Italy is Rome."
}
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("User said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def answer_question(question):
    if question in qa_dataset:
        return qa_dataset[question]
    else:
        return "I'm sorry, I don't have an answer to that question."

def main():
    greet()
    speak("How can I assist you today?")

    while True:
        query = listen()

        if query == "":
            continue

        if query in qa_dataset:
            speak(qa_dataset[query])
        elif "goodbye" in query or "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
