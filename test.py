from random import randint
from model.population_generator import PopulationGenerator
from model.aptitude_calculator import AptitudeCalculator

populationGenerator = PopulationGenerator()
aptitudeCalculator = AptitudeCalculator()
population = populationGenerator.generate_population()
for individual in population:
    print("-----------------------------------------")
    print(individual)
    print("Parejas que no se atacan: " + str(aptitudeCalculator.calculate_aptitude(individual)))
