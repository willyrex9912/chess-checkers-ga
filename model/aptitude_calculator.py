from typing import List

class AptitudeCalculator:

    def __init__(self):
        pass

    def calculate_aptitude(self, individual: List) -> int:
        valid_pairs = 0
        for i in range(len(individual)):
            evaluate_column = i + 1
            evaluate_value = individual[i]
            for j in range(evaluate_column, len(individual)):
                current_column = j + 1
                current_value = individual[j]
                print("Comparando valor " + str(evaluate_value) + " en columna " + str(evaluate_column) + " con valor " + str(current_value) + " en columna " + str(current_column))
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
        return valid_pairs
