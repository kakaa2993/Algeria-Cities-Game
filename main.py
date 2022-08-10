#!/usr/bin/python3
from turtle import Screen
from game_brain import GameBrain

SCORE = 0
screen = Screen()
screen.title("Algeria Cities Game")
screen.bgpic("./Algeria_maps/algerie71.gif")
screen.setup(width=713, height=720)
game_brain = GameBrain()
cities = game_brain.cities_list
answers_list = []

game_is_on = True
while game_is_on:
    answer = screen.textinput(f"{SCORE}/58 Cities Correct", prompt="What's another city name? ").strip().title()
    # print all the cities in Algeria
    if answer == "Solution":
        # Print the right solution
        screen.clear()
        screen.bgpic("./Algeria_maps/algerie73.gif")
        game_is_on = False
        screen.mainloop()
    if answer == "Exit":
        game_is_on = False

    # check in the answer is correct and print it on the map
    elif answer in cities:
        SCORE += 1
        game_brain.add_city(answer)
        answers_list.append(answer)
    # If the player guess all the 58 state then exit the game
    elif len(game_brain.all_cities) == 58:
        game_is_on = False

# Save the missing cities to a csv file
game_brain.generate_missed_cities_csv(answers_list)


