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

        # limit the results to integer values only, as per the game rules
        if result.is_integer():
            result = int(result)
            evaluated.append((value, result))

    return evaluated

# given a formula as a string, return the count of numbers, +, -, * and / in the given formula expression
def CountFormulaElements(formula):
    numberCount = 0
    plusCount = 0
    minusCount = 0
    multiplyCount = 0
    divideCount = 0

    numbers = re.findall(r'\d+', formula)
    numberCount = len(numbers)
    plusCount = formula.count('+')
    minusCount = formula.count('-')
    multiplyCount = formula.count('*')
    divideCount = formula.count('/')

    return numberCount, plusCount, minusCount, multiplyCount, divideCount


def Analysis(targetValue, evaluatedFormulaSet):

    closestDiff=sys.maxsize
    hitCount=0

    solutions=list()

    for idx, (expr, result) in enumerate(evaluatedFormulaSet):
        if result == targetValue:
            hitCount += 1
            closestDiff=0
            closestSolution=(expr, result)
            solutions.append(expr)
        else:
            if closestDiff==0:
                continue
            diff = abs(targetValue - result)
            if diff<closestDiff:
                closestDiff=diff
                closestSolution=(expr, result)

    return closestDiff,hitCount,closestSolution,solutions  

def AnalysisTargetSet(evaluatedFormulaSet):
    hitCountMax=0
    hitCountMin=sys.maxsize
    for targetValue in range(1,1000):
        closestDiff, hitCount, closestSolution, solutions = Analysis(targetValue, evaluatedFormulaSet)

        if hitCount==0:
            print (f"{hitCount:3d} : {targetValue:4d} ~ {closestSolution} (diff {closestDiff})") 
        else:
            print (f"{hitCount:3d} : {targetValue:4d} = {closestSolution}") 

        if hitCount>hitCountMax:
            hitCountMax=hitCount
        if hitCount<hitCountMin:
            hitCountMin=hitCount

    print (f"Hit count max: {hitCountMax}, min: {hitCountMin}")


import sys
import re

def main():

    # solutions for the number set [9,7,2,4,9,25] to reach the target value 667
    # known solutions:
    # ((9*4)-7)*(25-2)=667 this solution is only found with an exhaustive search including parentheses
    # 9*9*7+4*25=667

    targetSet = [9,7,2,4,9,25]
    targetValue = 667

    verbose = True

    if verbose:
        print (f"Generating formula combination set from the number set {targetSet} ... ", end="")
        sys.stdout.flush()
    
    formulaSet = sorted(GenerateFormulaSet(targetSet), key=lambda s: (len(s), s.lower()))

    if verbose:
        print (f"Formula combinations set size that have an integer result: {len(formulaSet)}")
        print (f"Evaluating formula set ... ", end="")
        sys.stdout.flush()

    evaluatedFormulaSet = EvaluateFormulaSet(formulaSet)

    closestDiff, solutionCount, closestSolution, solutions = Analysis(targetValue, evaluatedFormulaSet)
    if solutionCount==0:
        print (f"Found {solutionCount} solutions for the target value {targetValue}, closest solution was {closestSolution} with a difference of {closestDiff} from target") 
    else:
        print (f"Found {solutionCount} solutions for the target value {targetValue}") 


    for index, solution in sorted(enumerate(solutions), key=lambda x: CountFormulaElements(x[1])):
        print (f"Solution {1+index:<4d} : {solution}")
    print()

    #AnalysisTargetSet(evaluatedFormulaSet)




if __name__ == "__main__":
    main()
