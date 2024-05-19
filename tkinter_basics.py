from tkinter import *

FONT=("Arial",24,"bold")

window=Tk()
window.title("My first GUI Program")
window.minsize(width=300,height=300)


label=Label(text="I am a label", font=FONT)
label.pack()

# def add(*args):
#     sum=0
#     for x in args:
#         sum+=x
#     return sum

# print(add(3,4,5,6)==add(7,8,3))

#*args means many positional arguments

# def calculate(**kwargs):
#     for (x,y) in kwargs.items():
#         print(x,y)
    
# calculate(add=3,multiply=5)
# calculate(sub=2,div=6,add=1,a='v')

# **kwargs means many keyword arguments

label["text"]="New Text"

label.config(text="New Text Again")

#Button


def button_clicked():
    # if label["text"]=="I got Clicked":
    #     label.config(text="New Text!")
    # else:
    #     label.config(text="I got Clicked")
    
    if input.get()=="":
        pass
    else:
        label.config(text=input.get())
    
my_button=Button(text="Click Me",command=button_clicked,font=("Arial",12,"italic"))
my_button.pack()

# for input

input =Entry(width=10)
input.pack()

input.insert(END,"email")

#Text

text=Text(height=5,width=30)
text.focus()
text.insert(END,"a multiple line can be entered here")
print(text.get("1.0",END))
text.pack()

#Spinbox

def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#scale


def scale_used(value):
    print(value)
scale=Scale(from_=0,to=100,width=30,command=scale_used)
scale.pack()

#checkbutton

def checkbutton_used():
    print(checked_state.get())
    
checked_state=IntVar()
checkbutton=Checkbutton(variable=checked_state,command=checkbutton_used,text="Is On?")
print(checked_state.get())
checkbutton.pack()

#radiobutton

def radio_used():
    print(radio_state.get())
    
radio_state=IntVar()
radiobutton1=Radiobutton(text="option1",value=1,variable=radio_state,command=radio_used)
radiobutton2=Radiobutton(text="option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#ListBox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
    
listbox=Listbox(height=4)
fruits=['Apple','Banana','Pear','Orange']

for x in fruits:
    listbox.insert(fruits.index(x),x)
    
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()













window.mainloop()