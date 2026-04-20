import random

events = [None, "Засуха", "Высокая урожайность", "Дождь", "Плохая погода"]
chances = [65, 5, 5, 18, 7]

def event():
    return random.choices(events, weights=chances, k=1)[0]
    