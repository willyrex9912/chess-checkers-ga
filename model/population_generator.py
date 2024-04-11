from random import randint
from model.individual import Individual
from typing import List


class PopulationGenerator:

    def __init__(self, population_size: int):
        self.population: List[Individual] = []
        self.population_size = population_size

    def generate_population(self):
        for i in range(1, self.population_size + 1):
            self.population.append(self.generate_individual())

    def generate_individual(self) -> Individual:
        genes = []
        for i in range(1, 9):
            genes.append(randint(1, 8))
        return Individual(genes, 0)

    def generate_population_by_roulette(self):
        population = []
        while len(population) < self.population_size:
            first = self.select_by_roulette()
            second = self.select_by_roulette()
            population.extend(self.cross_individuals(first, second))
        self.population = population

    def cross_individuals(self, first: Individual, second: Individual) -> List[Individual]:
        print("\nCrossing:")
        print(first.genes)
        print(second.genes)
        middle = int(len(first.genes) / 2)
        new_first = Individual([], 0)
        new_second = Individual([], 0)
        new_first.genes.extend(first.genes[:middle])
        new_first.genes.extend(second.genes[middle:])
        new_second.genes.extend(second.genes[:middle])
        new_second.genes.extend(first.genes[middle:])
        print("New Individuals:")
        print(new_first.genes)
        print(new_second.genes)
        return [new_first, new_second]

    def select_by_roulette(self) -> Individual:
        s = sum(individual.aptitude for individual in self.population)
        a = randint(0, s)
        value = 0
        for individual in self.population:
            value = value + individual.aptitude
            if value > a:
                return individual
