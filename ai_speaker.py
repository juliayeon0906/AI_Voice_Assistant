import speech_recognition as sr
import time, os
from gtts import gTTS
from playsound import playsound
from gpt import get_gpt_response

running = True

# Speech to Text
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print('[ME] ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('Recognition Failed..')
    except sr.RequestError as e:
        # API key Error or Network Error
        print('Request Failed: {0}'.format(e))

# Answer
def answer(input_text):
    global running
    if 'stop' in input_text.lower():
        answer_text = 'See you next time.'
        speak(answer_text)
        running = False
        stop_listening(wait_for_stop=False)
        return
    answer_text = get_gpt_response(input_text)
    speak(answer_text)

# Text to Speech
def speak(text):
    print('[AI] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('How may I assist you?')
stop_listening = r.listen_in_background(m, listen)

while running:
    time.sleep(0.1)
