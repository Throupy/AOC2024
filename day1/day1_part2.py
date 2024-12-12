# 2024
# TODO: Using collections for counting probably more efficient (faster)

import time

def read_in_data(filename: str):
    left = []
    right = []

    with open(filename, "r") as f:
        for line in f:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)

    return left, right


def solution(left: list, right: list):
    similarity_score = 0

    for number in left:
        similarity_score += (number * right.count(number))
    
    return similarity_score


if __name__ == "__main__":
    script_start = time.time()
    left, right = read_in_data("day1_input.txt")

    solution_start = time.time()
    result = solution(left, right)
    solution_end = time.time()
    print(f"Output ---> {result}")
    print("Time taken for solution function:", round(solution_end - solution_start, 8), "seconds")
    
    script_end = time.time()
    print("Total script time:", round(script_end - script_start, 8), "seconds")