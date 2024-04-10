from random import randint


class PopulationGenerator:

    def __init__(self):
        self.population = []

    def generate_population(self):
        for i in range(1, 11):
            self.population.append(self.generate_individual())
        return self.population

    def generate_individual(self):
        individual = []
        for i in range(1, 9):
            individual.append(randint(1, 8))
        return individual
