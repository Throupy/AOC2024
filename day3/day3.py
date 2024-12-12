import re
import ast

def solution_a():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
            for match in matches:
                tuple_value = ast.literal_eval(match[3::])
                total += tuple_value[0] * tuple_value [1]
    
    return total


def solution_b():
    with open("input.txt", "r") as f:
        total = 0
        disabled = False
        for line in f:
            matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", line)
            print(matches)
            for match in matches:
                if match == "don't()":
                    disabled = True
                elif match == "do()":
                    disabled = False
                else: #mul operations
                    if not disabled:
                        tuple_value = ast.literal_eval(match[3::])
                        total += tuple_value[0] * tuple_value[1]
    
    return total


print(solution_a())