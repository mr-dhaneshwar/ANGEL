from requests import get
import pyautogui as p
from speech import*
import webbrowser
import random
from openapi import*

def task():
    import pywhatkit as kit
    '''
     function that contains a loop which executes tasks according to the spoken command.

    '''

    while True:
        query = takeCommand().lower()
        query_word = query.split()
        if error(query):
            continue

        #Logic for executing tasks on query
        if query in bye:
            if 'wait' in query:
                speak('ok sir i am waiting...')
                break
            else:
                speak('ok sir bye, i am going to sleep')
                break

        elif 'how are you' in query:
            speak(random.choice(thanks))
            speak('What i can do for you')

        elif 'open google' in query:
            
            webbrowser.open('google.com')
            speak('opening google')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak('opening youtube')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak('opening stack overflow')
        
        elif 'open' in query:
            query = query.replace('open','').strip()
            p.hotkey('Win')
            for i in query:
                p.hotkey(i)
            p.hotkey('enter')
            speak('opening,'+query)
        
        elif 'switch' in query:
            speak('ok sir')
            p.hotkey('Alt','Tab')

        elif 'close' in query:
            speak('ok sir')
            p.hotkey('Alt','F4')

        elif 'screenshot' in query and 'show' in query:
            p.hotkey('win','g')
            speak('here is your screenshots')

        elif 'screenshot' in query:
            speak('ok sir')
            p.hotkey('Win','Alt','writeScreen')
            speak('screenshot seved')

        elif 'sleep' in query:
            speak('ok sir')
            p.hotkey('Win','d')
            p.hotkey('Alt','F4')
            p.hotkey('up')
            p.hotkey('Enter')
            return

        elif 'shutdown' in query or 'off' in query:
            p.hotkey('win','d')
            p.hotkey('Alt','F4')
            speak('Shutting down')
            p.hotkey('Enter')

        elif 'time' in query:
            speak(current_time()+' sir')

        elif 'play music' in query:
            speak('which song ?')
            song = takeCommand()
            speak('playing on youtube')
            kit.playonyt(song)
            break
        
        elif query_word[0] == 'angel':
            query = query.replace('angel ','')+'.'
            # speak(angel(query), idea_png)
            speak(angel(query))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP Address is {ip}')

        else:
            speak('sorry.. this is not in my system')