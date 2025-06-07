import speech_recognition as sr
import time, os
from gtts import gTTS
from playsound import playsound

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
    answer_text=''
    if 'hello' in input_text:
        answer_text = 'Hi, nice to meet you.'
    elif 'stop' in input_text:
        answer_text = 'See you next time.'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = 'Can you say it again?'
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

while True:
    time.sleep(0.1)
