from tkinter import *
import pyperclip
import json
from tkinter import messagebox
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    import random
    letter_list=[random.choice(letters) for _ in range(random.randint(8,10))]
    symbol_list=[random.choice(symbols) for _ in range(random.randint(2,4))]
    number_list=[random.choice(numbers) for _ in range(random.randint(2,4))]
    z = letter_list+symbol_list+number_list
    random.shuffle(z)
    x="".join(z)
    pass_entry.insert(0,x)
    pyperclip.copy(x)


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_details():
    website=web_entry.get().lower()
    email=""
    password=""
    
    if website=="":
        messagebox.showinfo(title="website",message="First enter the website details\n")
    else:
        try:
            with open("D:\\nitw\\academics\\demo_py\\password_manager_gui\\data_file.json","r")\
            as data_file:
                web=json.load(data_file)
                
        except FileNotFoundError:
            messagebox.showinfo(title="website",message="No data in the file \n")
        else:
            if website in web:
                email=web[website]["email"]
                password=web[website]["password"]
                messagebox.showinfo(title="website",message=f"The details are :\n Email : {email}\n Password : {password}")
            else:
                 messagebox.showinfo(title="website",message=f"The website does'nt exist in our json file")
                
            
                


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    email=email_entry.get()
    web=web_entry.get()
    password=pass_entry.get()
    
    new_data={web:{
        "email":email,
        "password":password,
    }}
    
    if web=="" or password=="":
        fields=""
        if web=="" and password=="":
            fields=f"Website and Password fields are empty! Please fill Them"
        elif web=="":
            fields="Website field is empty! Please fill It"
        else:
            fields="Password field is empty! Please fill It"
        messagebox.showinfo(title="website",message=f"Oops! {fields}")
    else:
        #is_ok=messagebox.askokcancel(title="website",message=f"Is it Ok to have these \n Email : {email}\n Password : {password} \n")
        #if is_ok:
        try:
            with open("D:\\nitw\\academics\\demo_py\\password_manager_gui\\data_file.json","r") \
            as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("D:\\nitw\\academics\\demo_py\\password_manager_gui\\data_file.json","w") \
            as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("D:\\nitw\\academics\\demo_py\\password_manager_gui\\data_file.json","w")\
            as data_file:
                # saving updated file to json
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0,END)
            pass_entry.delete(0,END)
    
# ---------------------------- UI SETUP ------------------------------- #



FONT_NAME= ("Araial",12)

window=Tk()
window.title("Password Manager GUI")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
password_img=PhotoImage(file="D:\\nitw\\academics\\demo_py\\password_manager_gui\\logo.png")
canvas.create_image(100,100,image=password_img)
canvas.grid(row=0,column=1)

web_name=Label(text="Website:",font=FONT_NAME)
web_name.grid(row=1,column=0)
email_name=Label(text="Email/UserName:",font=FONT_NAME)
email_name.grid(row=2,column=0)
pass_name=Label(text="Password:",font=FONT_NAME)
pass_name.grid(row=3,column=0)

web_entry=Entry(width=21,font=FONT_NAME)
web_entry.grid(row=1,column=1)
web_entry.focus()
email_entry=Entry(width=35,font=FONT_NAME)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"anirudhpabbaraju1103@gmail.com")
pass_entry=Entry(width=21,font=FONT_NAME)
pass_entry.grid(row=3,column=1)

gen_pass=Button(text="Generate Password",font=FONT_NAME,command=generate_password)
gen_pass.grid(row=3,column=2)

search_button=Button(text="Search",width=14,font=FONT_NAME,command=search_details)
search_button.grid(row=1,column=2)



add=Button(text="add",width=36,font=FONT_NAME,command=save_password)
add.grid(row=4,column=1,columnspan=2)




window.mainloop()