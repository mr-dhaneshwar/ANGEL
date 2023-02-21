# import datetime
# from speech import speak,current_time
# from operation import task

# def wishMe():
#     '''
#     function that says a greeting according to the current time.

#     '''
#     hour = int(datetime.datetime.now().hour)    #getting hours
#     if hour>=0 and hour<12:     #check current time is AM or PM
#         speak('Good Morning sir!')
#     elif hour>=12 and hour<18:
#         speak('Good Afternoon sir!')
#     else:
#         speak('Good Evening sir!')
#     speak(current_time())       

#     speak('I am Angel, Please tell me how may i help you')
#     task()