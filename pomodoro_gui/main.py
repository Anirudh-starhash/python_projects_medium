
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(t,text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_time=int(WORK_MIN*60)
    short_break_time=int(SHORT_BREAK_MIN*60)
    long_break_time=int(LONG_BREAK_MIN*60)
    
    if reps%8==0:
        timer_label.config(text="LONG BREAK",fg=RED)
        count_down(long_break_time)
    elif reps%2==0:
        timer_label.config(text="SHORT BREAK",fg=PINK)
        count_down(short_break_time)
    else:
        timer_label.config(text="WORK",fg=GREEN)
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    
    if count_sec<10:
        count_sec=f"0{count_sec}"
        
    counter=f"{count_min}:{count_sec}"
    
    canvas.itemconfig(t,text=counter)
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        working_session=math.floor(reps/2)
        for _ in range(working_session):
            marks+="✔"
        
        check_mark.config(text=marks)
    
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window=Tk()

window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="D:\\nitw\\academics\\demo_py\\pomodoro_gui\\tomato.png")
canvas.create_image(100,112,image=tomato_img)
t=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)
check_mark=Label(text="",highlightthickness=0,fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check_mark.grid(column=2,row=4)

start=Button(text="START",command=start_timer)
reset=Button(text="RESET",command=reset_timer)
start.grid(row=3,column=1)
reset.grid(row=3,column=3)

timer_label=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
timer_label.grid(row=1,column=2)




window.mainloop()