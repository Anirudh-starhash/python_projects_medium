import smtplib

# if(float(price)<100):
#     from email.mime.text import MIMEText
#     answer="Yo! The price of your required item is less than your Target Price go grab it!"
#     msg=MIMEText(answer)
#     receipient="ap22csb0a10@student.nitw.ac.in"
#     sender="anirudhpabbaraju1103@gmail.com"
#     password='atnipcvnvvxvcghn'
#     msg['Subject']="Amazon Offer!"
#     msg['From']=sender
#     msg['To']=receipient
#     with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
#         smtp_server.login(sender,password)
#         smtp_server.sendmail(sender,receipient,msg.as_string())