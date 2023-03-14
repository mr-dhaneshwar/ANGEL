import smtplib

mail_list = ['ghanshyam-mahajanghanshyam65@gmail.com', 'me-prasaddhaneshwar22@gmail.com', 
             'kunal-ktmahajan2001@gmail.com', 'mahesh-www.mrsananse@gmail.com']

def check_mail(e):
    for i in mail_list:
        x = i.split('-')
        if e in x:
            return x
        else:
            continue

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prasaddhaneshwar09@gmail.com', 'nzvcnfljjylvaghv')
    server.sendmail('prasaddhaneshwar09@gmail.com', to, content)
    server.close()
