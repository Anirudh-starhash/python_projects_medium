from bs4 import BeautifulSoup
import lxml;


import requests

url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,te;q=0.7",
     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}


response=requests.get(url)
# print(response.raise_for_status)
soup=BeautifulSoup(response.text,"html.parser")

# print(soup.prettify)

price = soup.find(name="span",class_="a-price-whole").getText()
price2 = soup.find(name="span",class_="a-price-fraction").getText()
price+=price2
print(price)

import smtplib

if(float(price)<100):
    from email.mime.text import MIMEText
    answer="Yo! The price of your required item is less than your Target Price go grab it!"
    msg=MIMEText(answer)
    receipient="ap22csb0a10@student.nitw.ac.in"
    sender="anirudhpabbaraju1103@gmail.com"
    password='atnipcvnvvxvcghn'
    msg['Subject']="Amazon Offer!"
    msg['From']=sender
    msg['To']=receipient
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(sender,password)
        smtp_server.sendmail(sender,receipient,msg.as_string())