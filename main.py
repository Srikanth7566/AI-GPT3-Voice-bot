import openai
import pyttsx3
import speech_recognition as sr
from api_secrets import API_KEY

openai.api_key = API_KEY

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

conversation = " "
user_name = "srikanth"
bot_name = "jarvis"

while True:
    with mic as source:
        print("listening....")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("not listening")

    try:
        user_input = r.recognize_google(audio)

    except:
        continue

    prompt = user_name + ":" + user_input + "\nbot:"
    conversation += prompt

    response = openai.Completion.create(engine="text-davinci-001", prompt=conversation, max_tokens=50)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ":", 1)[0].split("Ava: ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
