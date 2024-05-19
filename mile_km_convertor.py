from tkinter import *

window=Tk()
window.title("Mile to Km convertor")
window.config(padx=20,pady=20)

def cal():
    if value.get()=="":
        km_value.config(text="Nothing is entered")
    else:
        answer=float(value.get())
        km_value.config(text=str(answer*1.609))

miles=Label(text="Miles")
km=Label(text="Km")
is_equal=Label(text="is equal to")
value=Entry(width=10)
km_value=Label(text="0")
calculate=Button(text="Calculate",command=cal)

miles.grid(row=1,column=3)
km.grid(row=2,column=3)
is_equal.grid(row=2,column=1)
value.grid(row=1,column=2)
km_value.grid(row=2,column=2)
calculate.grid(row=3,column=2)


    

window.mainloop()