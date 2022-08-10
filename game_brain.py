from turtle import Turtle
import pandas
data = pandas.read_csv("Algeria.csv")


class GameBrain:

    def __init__(self):
        self.all_cities = []
        self.cities_list = data["city"].to_list()

    def add_city(self, name):
        new_city = Turtle()
        new_city.penup()
        new_city.hideturtle()
        new_city.color("red")
        position = int(data[data["city"] == name].x), int(data[data["city"] == name].y)
        new_city.goto(position)
        new_city.write(name, align="center")
        self.all_cities.append(new_city)

    def generate_missed_cities_csv(self,list_of_answers):
        missed_cities = [city for city in self.cities_list if city not in list_of_answers]
        pandas.Series(missed_cities).to_csv("missing_cities.csv")