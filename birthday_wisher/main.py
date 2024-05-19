# import smtplib
# from email.mime.text import MIMEText

# subject = "Email Subject"
# body = "This is the body of the text message"
# sender = "anirudhpabbaraju1103@gmail.com"
# recipients = ["ap22csb0a10@student.nitw.ac.in", "23f2002166@ds.study.iitm.ac.in"]
# password = "atnipcvnvvxvcghn"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# send_email(subject, body, sender, recipients, password)

import datetime as dt
import smtplib,random

from email.mime.text import MIMEText

now=dt.datetime.now()

week_day=now.weekday()

if week_day==5:
    with open("D:\\nitw\\academics\\demo_py\\birthday_wisher\\quotes.txt") as file:
        quotes=file.readlines()
        quote=random.choice(quotes)
        
    print(quote)
    msg=MIMEText(quote)
    sender='anirudhpabbaraju1103@gmail.com'
    receipient='ap22csb0a10@student.nitw.ac.in'
    password='atnipcvnvvxvcghn'
    msg['Subject']="Email Subject"
    msg['From']=sender
    msg['To']=receipient
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(sender,password)
        smtp_server.sendmail(sender,receipient,msg.as_string())
        
        
    
    


