import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prasaddhaneshwar09@gmail.com', 'madhuzybdejhozff')
    server.sendmail('prasaddhaneshwar09@gmail.com', to, content)
    server.close()


try:
    msg = input('Enter MSG:- ')
    to = 'mahajanghanshyam65@gmail.com'
    sendEmail(to, msg)
    print('MSG has been send to', to)

except Exception as e:
    print(e)
