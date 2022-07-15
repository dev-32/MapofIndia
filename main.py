from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("list-indian-states-and-capitals-28j.csv")
all_states = data.state.to_list()

correct_state = []
missing_state = []
s = Screen()
s.title("India States Game")
image = "map.gif"
s.addshape(image)
t1 = Turtle()
t1.shape(image)
count = 0
while count != 28:

    answer_state = s.textinput(title=f"{count}/28 Guess the State", prompt="What's the name?").title()

    if answer_state == "Exit":

        missing_state = [state for state in all_states if state not in correct_state]
        file = pandas.DataFrame(missing_state)
        file.to_csv("missing_states.csv")

        break
    if answer_state in all_states:
        correct_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        t.hideturtle()

        states = data[data["state"] == answer_state]
        t.goto(int(states.x), int(states.y))
        t.write(states.state.item(),font=("Arial", 10, "bold"))
        count += 1









s.exitonclick()