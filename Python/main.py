# Copyright (C) 2025 Anthony Ransley
# https://github.com/Software101DotNet
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


def SetOfAllSixNumberCombinations():
    from itertools import combinations
    # Game drawn from 2 sets of numbers 1..10, and a single set of numbers 25, 50, 75, 100
    numbers = [100, 75, 50, 25, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  
    return list(combinations(numbers, 6))


# for a given game of 6 numbers, return the complete set of all the possible sequences that can be made from the 6 number numbers
def GenerateNumberCombinationSet(gameSet):
    from itertools import permutations

    allPermutations=list()
    
    # add all the unique gameSet numbers to the allPermutations solutions set
    for i in range(1, 7):
        for number in permutations(gameSet, i):
            allPermutations.append(number)

    return allPermutations


def GenerateFormulaSet(numberSet):
    from itertools import product, permutations

    operators = ['+', '-', '*', '/']
    formulaSet = set()  
    
    # start with the numbers themselves
    for number in numberSet:
        formulaSet.add(str(number))

    # generate all possible formulas using the numbers and operators
    for r in range(2, len(numberSet) + 1):
        for numberCombo in permutations(numberSet, r):
            for operatorCombo in product(operators, repeat=r - 1):
                # build the formula string
                formula = ""
                for i in range(r - 1):
                    formula += str(numberCombo[i]) + operatorCombo[i]
                formula += str(numberCombo[-1])
                formulaSet.add(formula)

    return formulaSet


def EvaluateFormulaSet(solutions):
    evaluated = []
    for value in solutions:
        result = eval(value)
        # rounding error at 945925: 6/5/3*1*4-2 = -0.40000000000000013, so filter to 4 decimal places
        #result = round(result, 4)

        # limit the results to integer values only
        #if result.is_integer():
        #    result = int(result)
        evaluated.append((value, result))

    return evaluated


# calculate a histogram of results
def calculate_histogram(evaluated_solutions):
    histogram = {}
    for expr, result in evaluated_solutions:
        if result not in histogram:
            histogram[result] = 0
        histogram[result] += 1
    return histogram

import sys
import logging

def main():

    # Configure logging with a timestamp (%(asctime)s)
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.ERROR)
    verbose = False

    targetSet = [50,4,6,9,3,8]
    targetValue = 532

    print (f"Generating the set of all possible formulas combinations from the number set {targetSet}")
    formulaSet = sorted(GenerateFormulaSet(targetSet), key=lambda s: (len(s), s.lower()))

    if verbose:
        print (f"Formula set size is {len(formulaSet)} :")
        for idx, s in enumerate(formulaSet):
            print(f"{1+idx:5d}: {s}")
        print()

    print (f"Evaluating formula set ...", end="")
    sys.stdout.flush()
    evaluatedFormulaSet = EvaluateFormulaSet(formulaSet)
    print(f" Evaluation of {len(evaluatedFormulaSet)} formulas completed.")

    if verbose:
        for idx, (expr, result) in enumerate(evaluatedFormulaSet):
            print(f"{1+idx:5d}: {expr} = {result}")
        
    min=0
    max=0
    closestDiff=sys.maxsize
    hitCount=0
    for idx, (expr, result) in enumerate(evaluatedFormulaSet):
        if min>result:
            min=result
        if max<result:
            max=result
        if result == targetValue:
            hitCount += 1
        else:
            diff = abs(targetValue - result)
            if diff<closestDiff:
                closestDiff=diff
                closestSolution=(expr, result)

    if hitCount==0:
        print (f"Found {hitCount} solutions for the target value {targetValue}, closest solution was {closestSolution} with a difference of {closestDiff} from target") 
    else:
        print (f"Found {hitCount} solutions for the target value {targetValue}")   


if __name__ == "__main__":
    main()
