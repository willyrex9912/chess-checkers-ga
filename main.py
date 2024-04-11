# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from model.population_generator import PopulationGenerator
from model.aptitude_calculator import AptitudeCalculator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    populationGenerator = PopulationGenerator(10)
    aptitudeCalculator = AptitudeCalculator()
    populationGenerator.generate_population()
    aptitudeCalculator.calculate_aptitudes(populationGenerator.population)
    populationGenerator.generate_population_by_roulette()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
