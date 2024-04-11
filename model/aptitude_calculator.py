from typing import List
from model.individual import Individual


class AptitudeCalculator:

    def __init__(self):
        pass

    def calculate_aptitudes(self, population: List[Individual]):
        print("\nAptitude calculation:")
        for individual in population:
            self.calculate_aptitude(individual)
            print(str(individual.genes) + " : " + str(individual.aptitude))

    def calculate_aptitude(self, individual: Individual):
        genes = individual.genes
        valid_pairs = 0
        for i in range(len(genes)):
            evaluate_column = i + 1
            evaluate_value = genes[i]
            for j in range(evaluate_column, len(genes)):
                current_column = j + 1
                current_value = genes[j]
                first_invalid_square = evaluate_value + current_column - evaluate_column
                second_invalid_square = evaluate_value
                third_invalid_square = evaluate_value - current_column + evaluate_column
                if first_invalid_square == current_value:
                    continue
                if second_invalid_square == current_value:
                    continue
                if third_invalid_square == current_value:
                    continue
                valid_pairs = valid_pairs + 1
        individual.aptitude = valid_pairs
