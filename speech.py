import speech_recognition as sr
from threading import*
import datetime
import pyttsx3
# from GUI import*

#Define All reply
thanks = ['i am fine sir','always stands for you sir','i am good , thanks for asking sir','fine sir','i am good']
bye =    ['goodbye angel','bye angel','bye','okay bye','okay bye angel','goodbye','chup ho jao','quit','quit Angel','wait','okay wait']
start =  ['angel','wake up angel','hey angel','hello angel']
angel_output =  ['yes boss i am here','always here for you sir','ready sir']

engine = pyttsx3.init('sapi5')      #Initializes the pyttsx3 module. The SAPI5 helps to convert text to speech.
voices = engine.getProperty('voices')       #Gets the list of voices available.
engine.setProperty('voice', voices[1].id)   #Sets the voice to the second option in the list.




def current_time():
    '''
    function that returns the current time in a string.

    '''
    strTime = datetime.datetime.now().strftime('%I:%M') #detect hours and minits
    hour = int(datetime.datetime.now().hour)        #getting hours
    if hour>=0 and hour<12:         #check current time is AM or PM 
        return(f"it's {strTime}AM")
    else:
        return(f"it's {strTime}PM")


def error(query):
    '''
    function that checks if the query is blank or not and returns either True or False.

    '''
    if query == '':     #checks if the query is blank or not
        # speak('I did not understand, please Say That again.... ', confused_png)
        speak('I did not understand, please Say That again.... ')
        return True
    return False

# def speak(audio,img=None):
def speak(audio):
    '''
    function that takes an audio string and plays it back using the pyttsx3 module.
    '''
    # global speak_status
    try:
        # if img==None:
        #     img=gotit_png
        # anime.configure(image=img)
        # t = Thread(target=write,args=('Angel: '+audio,))
        # t.start()

        # if speak_status == 1:
        #     engine.say(audio)
        #     engine.runAndWait()
        print(f'Angel: {audio}')
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print('Somthing went wrong....\n',e)

def takeCommand():
    '''
    function that listens to the microphone and recognizes the speech using Google Speech Recognition.

    '''
    
    r = sr.Recognizer()     #creates an instance of the SpeechRecognizer class from the SpeechRecognition library
    try:
        with sr.Microphone() as source:
            print('Listning....')
            # status.configure(text='Listning....')
            # anime.configure(image=smile_png)
            r.phrase_threshold = 1
            r.energy_threshold = 600
            audio = r.listen(source)
        try:
            print('Recognizing....')
            # status.configure(text='Recognizing....')
            # anime.configure(image=listening_png)
            query = r.recognize_google(audio, language='en-in')
            # write(f'you: {query}')
            print(f'you: {query}')

        except Exception as e:
            query = '' 
            return query
        return query
    except Exception as e:
        print('somthing went wrong....',e)

