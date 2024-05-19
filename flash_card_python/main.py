BACKGROUND_COLOR = "#B1DDC6"

#-----------------------ACTION PART---------------------#
import pandas,random
from tkinter import *
new_data={}

try:
    data=pandas.read_csv("D:\\nitw\\academics\\demo_py\\flash_card_python\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("D:\\nitw\\academics\\demo_py\\flash_card_python\\data\\french_words.csv")
    new_data=original_data.to_dict(orient="records")
else:
    new_data=data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card,fliptimer
    window.after_cancel(fliptimer)
    current_card=random.choice(new_data)
    canvas.itemconfig(img,image=front)
    canvas.itemconfig(word,text=current_card["French"],fill="black")
    canvas.itemconfig(title,text="French",fill="black")
    
    fliptimer=window.after(3000,flip_card)
    
def flip_card():
    canvas.itemconfig(word,fill="white",text=current_card["English"])
    canvas.itemconfig(title,fill="white",text="English")
    canvas.itemconfig(img,image=back)
        
def is_known():
    new_data.remove(current_card)
    data=pandas.DataFrame(new_data)
    data.to_csv("D:\\nitw\\academics\\demo_py\\flash_card_python\\data\\words_to_learn.csv",index=False)
    next_card()
    
#-----------------------UI SETUP------------------------#


window=Tk()
window.title("Flash Card Project")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

fliptimer=window.after(3000,flip_card)



canvas=Canvas(width=800,height=526,highlightthickness=0)
front=PhotoImage(file="D:\\nitw\\academics\\demo_py\\flash_card_python\\images\\card_front.png")
img=canvas.create_image(400,263,image=front)
back=PhotoImage(file="D:\\nitw\\academics\\demo_py\\flash_card_python\\images\\card_back.png")
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

title=canvas.create_text(400,150,text="",fill="black",font=("Arial",40,"italic"))
word=canvas.create_text(400,263,text="",fill="black",font=("Arial",60,"bold"))

right=PhotoImage(file="D:\\nitw\\academics\\demo_py\\flash_card_python\\images\\right.png")
wrong=PhotoImage(file="D:\\nitw\\academics\\demo_py\\flash_card_python\\images\\wrong.png")

rightb=Button(image=right,highlightthickness=0,command=is_known)
wrongb=Button(image=wrong,highlightthickness=0,command=next_card)

rightb.grid(row=1,column=1)
wrongb.grid(row=1,column=0)

next_card()
window.mainloop()