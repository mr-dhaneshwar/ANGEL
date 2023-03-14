import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')  # Initializes the pyttsx3 module. The SAPI5 helps to convert text to speech.
voices = engine.getProperty('voices')  # Gets the list of voices available.
engine.setProperty('voice', voices[1].id)  # Sets the voice to the second option in the list.

def error(query):
    '''
    function that checks if the query is blank or not and returns either True or False.

    '''
    if query == '':  # checks if the query is blank or not
        speak('I did not understand, please Say That again.... ')
        return True
    return False

def speak(audio):
    '''
    function that takes an audio string and plays it back using the pyttsx3 module.
    '''
    try:
        print('Angel: ' + audio)
        engine.setProperty('rate', 195)
        engine.say(audio)
        engine.runAndWait()

    except Exception as e:
        print('speak problem....\n', e)


def takeCommand():
    '''
    function that listens to the microphone and recognizes the speech using Google Speech Recognition.

    '''

    r = sr.Recognizer()  # creates an instance of the SpeechRecognizer class from the SpeechRecognition library
    try:
        with sr.Microphone() as source:
            print('Listning....')
            r.adjust_for_ambient_noise(source)
            r.phrase_threshold = 1
            r.energy_threshold = 600
            audio = r.listen(source)
        try:
            print('Recognizing....')
            query = r.recognize_google(audio, language='hi')
            print(f'you: {query}')

        except Exception as e:
            query = ''
            return query
        return query
    except Exception as e:
        print('listen problem......', e)

speak('हेलो, मेरा नाम एंजेल है। आज मैं आपकी मदद किस तरह कर सकता हूँ?')