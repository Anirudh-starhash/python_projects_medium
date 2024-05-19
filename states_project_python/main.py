import turtle,pandas

my_screen=turtle.Screen()
my_screen.title("States guessing game")
img_file='D:\\nitw\\academics\\demo_py\\states_project_python\\blank_states_img.gif'
my_screen.addshape(img_file)
guessed_states=[]

turtle.shape(img_file)
data=pandas.read_csv("D:\\nitw\\academics\\demo_py\\states_project_python\\50_states.csv")
all_states=data.state.to_list()
while len(guessed_states)<50:
    answer=my_screen.textinput(title=f"States guessed {len(guessed_states)}/50",prompt="What is the state name you wanna choose ?").title()
    if answer=="Exit":
        not_guessed_states=[x for x in all_states if x not in guessed_states]
        d2=pandas.DataFrame(not_guessed_states)
        d2.to_csv("D:\\nitw\\academics\\demo_py\\states_project_python\\not_guessed_states.csv")
        break
   

    if answer in all_states:
        guessed_states.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        required=data[data.state==answer]
        t.goto(int(required.x),int(required.y))
        t.write(answer)
    

    
        

