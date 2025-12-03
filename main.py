# Create a list of all the possibilities of six numbers from 
# the set of 14 numbers consisting of 100,75,50,25,10,9,8,7,6,5,4,3,2,1
# There are 3003 combinations of choosing 6 numbers from a set of 14 numbers.
def SetOfNumbers():
    numbers = [100, 75, 50, 25, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    from itertools import combinations
    return list(combinations(numbers, 6))

def CountNumberSet():
    return len(SetOfNumbers())

# given a set of six numbers, return a set of all permutations of those numbers
def PermutationsOfSet(number_set):
    from itertools import permutations
    return list(permutations(number_set))

# 
def main():
    for combo in SetOfNumbers():
        print(combo)


if __name__ == "__main__":
    main()
