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
	numbers = [100, 75, 50, 25, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Game drawn from 2 sets of single digit numbers
	return list(combinations(numbers, 6))


# for a given game of 6 numbers, return the complete set of all the possible sequences that can be made from the 6 number numbers
def GameSolutionsPermutations(gameSet):
    from itertools import permutations

    allPermutations=list()
    
    # add all the unique gameSet numbers to the allPermutations solutions set
    for i in range(1,6):
        for number in permutations(gameSet, i):
            if number not in allPermutations:
                allPermutations.append(number)

    return allPermutations

     
from itertools import permutations, combinations

def PossibleGameSolutions(numbers):
    ops = ['+', '-', '*', '/']
    results = set()

    def build_expr(nums, exprs):
        if len(nums) == 1:
            results.add(exprs[0])
            return

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                a, b = nums[i], nums[j]
                ea, eb = exprs[i], exprs[j]

                remaining_nums = [
                    nums[k] for k in range(len(nums)) if k not in (i, j)
                ]
                remaining_exprs = [
                    exprs[k] for k in range(len(exprs)) if k not in (i, j)
                ]

                for op in ops:
                    if op == '/' and b == 0:
                        continue

                    try:
                        if op == '+':
                            val = a + b
                        elif op == '-':
                            val = a - b
                        elif op == '*':
                            val = a * b
                        elif op == '/':
                            val = a / b
                    except ZeroDivisionError:
                        continue

                    new_expr = f"({ea}{op}{eb})"
                    build_expr(
                        remaining_nums + [val],
                        remaining_exprs + [new_expr]
                    )

    # Use all subsets of size >= 2
    for r in range(2, len(numbers) + 1):
        for subset in combinations(numbers, r):
            for perm in permutations(subset):
                build_expr(list(perm), [str(x) for x in perm])

    return sorted(results)


def main():

    numberSet = [50, 4, 6, 9, 3, 8]
    targetValue = 532
    print (f"\nCalculating possible solutions for {targetValue} using number {numberSet}:\n")
    solution =  PossibleGameSolutions(numberSet)

    print("Evaluating possible solutions...\n")
    for index, value in enumerate(sorted(solution)):
        solutionResult=eval(value)
        print(f"{index:5d}  {value} = {solutionResult}")



if __name__ == "__main__":
    main()
