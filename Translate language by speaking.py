# Say any language command to convert in any language like URDU,ENGLISH etc...(by changing language options too)
import speech_recognition as sr
from textblob import TextBlob

listener = sr.Recognizer()

with sr.Microphone() as source:
    print("listening...")
    voice = listener.listen(source, timeout=5)
    command = listener.recognize_google(voice, language='en')  # Input language option
    being_translate = TextBlob(command)
    translated= being_translate.translate(to='ur') # Output language option
    print('Input : ' + command) # Input language option
    print('Output : ' + str(translated)) # Output language option
