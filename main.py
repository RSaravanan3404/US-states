import turtle
import pandas

screen = turtle.Screen()
image = "images/blank_states_img.gif"
screen.addshape(image)
screen.setup(width=700, height=500)
turtle.shape(image)

states_datas = pandas.read_csv("data/50_states.csv")
all_states = states_datas.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States correct.",
                                    prompt="What's another State's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        remaining_data = pandas.DataFrame(missing_states)
        remaining_data.to_csv("data/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = states_datas[states_datas.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

