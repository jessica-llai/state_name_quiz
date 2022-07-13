import pandas
import pandas as pd
import turtle
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

scoreboard = Scoreboard()


turtle.shape(image)

for i in range(50):
    tur = turtle

"""get the coor of each city, data put in the csv"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()  # = exitonclick


df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()  # convert to a list for data checkining

"""check the answer"""


guess_states = []



while len(guess_states) <= 50:

    answer_state = screen.textinput(title=f"{len(guess_states)} out of 50 states correct",
                                    prompt="What's another city's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
                learning_df = pandas.DataFrame(missing_states)
                learning_df.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = df[df.state == answer_state]
            x = state_data.x
            y = state_data.y
            t.goto(int(x), int(y))
            t.write(answer_state)
            guess_states.append(answer_state)





screen.exitonclick()


