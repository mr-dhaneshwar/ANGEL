from requests import get
import pyautogui as p
from openapi import *
from speech import *
import webbrowser
from mail import*
import random


def error(query):
    '''
    function that checks if the query is blank or not and returns either True or False.

    '''
    if query == '':  # checks if the query is blank or not
        speak('I did not understand, please Say That again.... ', 2)
        return True
    return False


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

        # Logic for executing tasks on query
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
            query = query.replace('open', '').strip()
            p.hotkey('Win')
            for i in query:
                p.hotkey(i)
            p.hotkey('enter')
            speak('opening,' + query)

        elif 'switch' in query:
            speak('ok sir')
            p.hotkey('Alt', 'Tab')

        elif 'close' in query:
            speak('ok sir')
            p.hotkey('Alt', 'F4')

        elif 'screenshot' in query and 'show' in query:
            p.hotkey('win', 'g')
            speak('here is your screenshots')

        elif 'screenshot' in query:
            speak('ok sir')
            p.hotkey('Win', 'Alt', 'writeScreen')
            speak('screenshot seved')

        elif 'sleep' in query:
            speak('ok sir')
            p.hotkey('Win', 'd')
            p.hotkey('Alt', 'F4')
            p.hotkey('up')
            p.hotkey('Enter')
            return

        elif 'shutdown' in query or 'off' in query:
            p.hotkey('win', 'd')
            p.hotkey('Alt', 'F4')
            speak('Shutting down')
            p.hotkey('Enter')

        elif 'time' in query:
            speak(current_time() + ' sir')

        elif 'play music' in query:
            speak('which song ?')
            song = takeCommand()
            speak('playing on youtube')
            kit.playonyt(song)
            break

        elif 'email' in query or 'mail'  in query:
            try:
                # speak('to whom you want to send')
                # to = takeCommand().lower()

                to_list = (query.split('to'))
                to = to_list[1].strip()

                if check_mail(to):
                    to = check_mail(to)
                    speak('what is the message')
                    msg = takeCommand().lower()
                    sendEmail(to, msg)
                    speak('message has been send to', to)
                else:
                    speak('email address not found',2)

            except Exception as e:
                print('problem while sending email',e)
                speak('email not send try again...',2)

        elif query_word[0] == 'angel':
            query = query.replace('angel ', '') + '.'
            speak(angel(query), 4)

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP Address is {ip}')


        else:
            speak('sorry.. this is not in my system')
