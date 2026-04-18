from organism import Organism

class Ecosystem:
    """ Класс симулирующий экосистему """
    def __init__(self):
        self.organisms = []

    """ Добавление организма в экосистему """
    def add_organism(self, organism: Organism):
        self.organisms.append(organism)

    """ Симуляция дня, проверка жив ли организм """ 
    def simulate_day(self):
        for org in self.organisms:
            if org.is_alive():
                org.eat(10)
            else:
                print(f"{org.name} мёртв.")
