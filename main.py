from ecosystem import Ecosystem
from organism import Organism
from utils import event

def main():
    # Создание 3-х объектов
    eco = Ecosystem()
    
    # Добавление
    eco.add_organism(Organism("Растение", 30))
    eco.add_organism(Organism("Лиса", 30))
    eco.add_organism(Organism("Заяц", 20))
    
    event()
    
    # Старт симуляции
    eco.simulate_day()

if __name__ == "__main__":
    main()