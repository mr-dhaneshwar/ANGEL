'''A.N.G.E.L : Automated Network Generating Expert Logic'''

from operation import *
from threading import *
import pyautogui as p
import socket
import random


def internet_connection_status():
    try:
        socket.create_connection(("www.google.com", 80))
        return True  # "You are connected to the internet"
    except OSError:
        return False  # "You are not connected to the internet"


def wishMe():
    '''
    function that says a greeting according to the current time.

    '''
    hour = int(datetime.datetime.now().hour)  # getting hours
    if 0 <= hour < 12:  # check current time is AM or PM
        speak('Good Morning sir!')
    elif 12 <= hour < 18:
        speak('Good Afternoon sir!')
    else:
        speak('Good Evening sir!')
    speak(current_time())

    speak('I am Angel, Please tell me how may i help you')
    task()


def main():
    """
    main function and a loop that listens for the command "angel" and executes the task() function if it is said.
    The program exits if the command "goodbye angel" is said.

    """
    if internet_connection_status():

        try:
            while True:
                query = takeCommand().lower()
                # query = takeCommand()
                if query in start:
                    p.hotkey('up')
                    if query == 'angel':
                        speak(random.choice(angel_output))
                        task()
                    else:
                        wishMe()

                if 'goodbye' in query or 'bye' in query:
                    # speak('goodbye sir, Love you 3000....',love_png)
                    speak('goodbye sir, Love you 3000....', 6)
                    close()
                    return
        except Exception as e:
            print("error to start...", e)

    else:
        msg = 'You are not connected to the internet'
        speak(msg, 2)


my_window(main)

