##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt,random,smtplib,pandas

now=dt.datetime.now()
data=pandas.read_csv("D:\\nitw\\academics\\demo_py\\automated_birthday\\birthdays.csv")
new_data=data.to_dict(orient="records")

index=-1

for x in range(len(new_data)):
    if new_data[x]['day']==now.day and new_data[x]['month']==now.month:
        index=x
        
if index!=-1:
    # step2 is true
    a=random.randint(1,3)
    
    with open(f"D:\\nitw\\academics\\demo_py\\automated_birthday\\letter_templates\\letter_{a}.txt","r") as f:
        x1=f.readlines()
        new_list=[]
        for x in x1: 
            PLACEHOLDER1="[NAME]"
            PLACEHOLDER2="Angela"
            x=x.strip()
            x=x.replace(PLACEHOLDER1,new_data[index]["name"])
            x=x.replace(PLACEHOLDER2,"Anirudh")
            new_list.append(x)
            
    answer=""
    with open(f"D:\\nitw\\academics\\demo_py\\automated_birthday\\letter_templates\\letter_{a}.txt","w") as f:
        for i in new_list:
            i=i.strip()
            answer+=i+"\n"
            f.write(i+"\n")
            
    # step3 done
    
    print(answer)
    from email.mime.text import MIMEText
    msg=MIMEText(answer)
    receipient=new_data[index]["email"]
    sender="anirudhpabbaraju1103@gmail.com"
    password='atnipcvnvvxvcghn'
    msg['Subject']="Happy Birthday!"
    msg['From']=sender
    msg['To']=receipient
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(sender,password)
        smtp_server.sendmail(sender,receipient,msg.as_string())
    
    

