# ANGEL
college project

1. Face_lock.py

1) face_sample():
This function captures the faces using the webcam and saves them to the 'samples' folder. It utilizes the OpenCV library to detect faces in each frame and draw a rectangle around them. The function continues to capture faces until it has taken 100 samples or the user presses the 'ESC' key. Each captured face is saved as a separate image file in the 'samples' folder with a filename that includes the face ID and a count number.

2) face_train():
This function loads the images from the 'samples' folder, converts them to grayscale, and trains a face recognition model using the LBPH (Local Binary Patterns Histograms) algorithm from OpenCV. The trained model is saved as a file named 'trainer.yml' in the 'trainer' folder.

3) face_match():
This function loads the trained face recognition model from the 'trainer.yml' file, and uses the webcam to capture frames and detect faces in real-time. It compares each detected face to the faces in the training dataset and displays the name of the person if there is a match. The function continues to detect faces until the user presses the 'ESC' key. If no match is found, the function displays 'Unknown' on the frame.

















2. GUI.py

1) change_theme(): This function changes the color theme of the GUI between "Light" and "Dark". It first checks the current theme, and then sets the background color of several widgets based on that theme. It also changes the color of the text and cursor in the output text box. If an error occurs while converting to the dark theme, an error message is printed.

2) off_speak(): This function toggles the speaking status of the chatbot between on and off. It first checks the current speaking status, and then changes the image of the silent button widget to either a sound or silence icon based on that status. It returns a Boolean value indicating whether speaking is on or off.

3) speak_check(): This function checks the current speaking status of the chatbot and returns a Boolean value indicating whether speaking is on or off.

4) write(text): This function writes a given text string to the output text box in the GUI.

5) close(): This function destroys the GUI frame and closes the program.

6) clear(): This function clears the text in the output text box.

7) change_leble(line, no): This function changes the text and image displayed in the GUI's status and anime widgets based on the given line and number.

8) new_frame(main): This function creates a new GUI frame for the ANGEL AI. It first creates several widgets for the frame, including buttons, labels, a status message, an anime image, and a text box. It then starts a new thread to run the given main function. Finally, it sets the frame's scrollbar and other configuration options.

9) my_window(main): This function creates the main window for the ANGEL AI. It first creates several widgets for the window, including buttons, labels, and an image. It then sets the window's size and title, and starts the main function.




3. speech.py

1) current_time(): Returns a string with the current time in 12-hour format.
2) speak(audio, img=1): Uses pyttsx3 to convert an audio string into speech and plays it back. It also takes an optional img argument to change the GUI display.
3) takeCommand(): Listens to the microphone using the SpeechRecognition module and recognizes the speech using Google Speech Recognition.
The script also defines several lists of possible responses, such as thanks, bye, start, and angel_output, which the program can use to generate replies to user input.



4. openapi.py

1) angel(prompt):
The angel function is defined to interact with the OpenAI API for generating natural language text.
The prompt argument is the starting text that OpenAI will use to generate a response.
The openai.Completion.create function creates a new completion request on the OpenAI API. It takes the following arguments:
engine: the language model to use. In this case, it's "text-davinci-003".
prompt: the starting text to generate a response from.
max_tokens: the maximum number of tokens (words and/or punctuation marks) the generated text can have.
n: the number of completions to generate. In this case, it's 1.
stop: a string or list of strings to indicate when the generation should stop. If None, generation continues until max_tokens is reached.
temperature: a value that controls the "creativity" of the generated text. A lower temperature generates more conservative and predictable text, while a higher temperature generates more unexpected and creative text.
The message variable is assigned the generated text returned by the API.
The function returns the message variable.




5.mail.py

1) check_mail(e) : the function takes an email address e as input and checks if it matches any of the email addresses in the mail_list variable. If a match is found, it returns the email address split by the "-" character. If no match is found, it returns None.

2) sendEmail(to, content) : the function takes two arguments: the recipient email address to, and the email content content. It establishes a connection with the Gmail SMTP server, logs in using the email and password provided, sends the email, and then closes the connection. This function is used to send emails to the recipient.


6.operation.py

1) task(), which contains a loop that listens for voice commands using the takeCommand() function from the speech module. Once a command is recognized, the function executes a task based on the user's spoken command.
Here is a brief overview of the tasks that the function can perform:
•	If the user says "bye", the function will either end immediately or wait for a few seconds before ending the program.
•	If the user says "how are you", the function will respond with a random message from a list of pre-defined messages, and then ask the user what it can do for them.
•	If the user says "open Google", "open YouTube", or "open Stack Overflow", the function will open the respective website in the user's default web browser.
•	If the user says "open" followed by a program name, the function will attempt to open the program by simulating a series of key presses.
•	If the user says "switch", the function will switch to the most recently used window.
•	If the user says "close", the function will close the currently active window.
•	If the user says "screenshot", the function will either show the user their most recent screenshot or take a new screenshot and save it.
•	If the user says "time", the function will tell the user the current time.
•	If the user says "play music", the function will ask the user which song they would like to play on YouTube, and then open the song in the user's default web browser.
•	If the user says "email" or "mail", the function will prompt the user for the recipient's email address, then the message content, and then attempt to send an email using the sendEmail() function from the mail module.
•	If the user says "sleep", the function will minimize all windows and put the computer to sleep.
•	If the user says "shutdown", the function will minimize all windows and shut down the computer.
•	If the user says "angel" followed by a question, the function will pass the question to the angel() function from the openai module and then speak the response.
•	If the user says "IP address", the function will retrieve the user's public IP address using the get() function from the requests module and then speak it.

7.Angel.py

1.	internet_connection_status(): This function checks the internet connection status by creating a connection to google.com. If the connection is successful, it returns True, otherwise it returns False.
2.	wishMe(): This function greets the user based on the current time (morning, afternoon, or evening) and speaks the current time. It also introduces itself as "Angel" and asks the user how it can help. After that, it calls the task() function to perform various operations.
3.	main(): This is the main function of the code. It has a loop that listens for the wake-up command "angel" and executes the task() function if it is said. The program exits if the command "goodbye angel" is said. The function first checks for an internet connection and then listens for the wake-up command. If the command is "angel", it speaks a random response from the angel_output list and then calls the task() function. If the command is not "angel", it calls the wishMe() function to greet the user. If the command is "goodbye angel" or "bye", it speaks a goodbye message and exits the program.
4.	my_window(main): This line of code calls the main() function inside a window created by the my_window() function, which is imported from the operation module. This allows the program to run in a separate window and not in the command line.

