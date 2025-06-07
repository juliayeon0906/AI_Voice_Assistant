import speech_recognition as sr
import time, os
from gtts import gTTS
from playsound import playsound
from gpt import get_gpt_response
from constants import language_map, greetings, stop_words, stop_responses

running = True

# Speech to Text
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language=sr_lang)
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
    input_text = input_text.lower()

    if any(word in input_text for word in stop_words.get(tts_lang, [])):
        speak(stop_responses.get(tts_lang, 'See you next time.'))
        running = False
        stop_listening(wait_for_stop=False)
        return
    answer_text = get_gpt_response(input_text)
    speak(answer_text)

# Text to Speech
def speak(text):
    print('[AI] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang=tts_lang)
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

# Prompt user for language
selected = input("Select a language (English / French / Korean): ").strip().lower()
sr_lang, tts_lang = language_map.get(selected, ("en-US", "en"))  # default: English

r = sr.Recognizer()
m = sr.Microphone()

speak(greetings.get(tts_lang, "How may I assist you?"))
stop_listening = r.listen_in_background(m, listen)

while running:
    time.sleep(0.1)
