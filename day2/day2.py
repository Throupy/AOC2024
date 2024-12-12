def solution_a():
    with open("day2_input.txt", "r") as file:
        safe = 0
        for line in file:
            nums = list(map(int, line.strip().split()))
            
            incr = True
            decr = True
            max_diff_valid = True
            
            for i in range(len(nums) - 1):
                diff = nums[i + 1] - nums[i]

                if not (1 <= abs(diff) <= 3):
                    max_diff_valid = False

                if diff < 0:
                    incr = False
                elif diff > 0:
                    decr = False

            if max_diff_valid and (incr or decr):
                safe += 1
            
        return safe
    
def solution_b():
    with open("day2_input.txt", "r") as file:
        safe = 0
        for line in file:
            nums = list(map(int, line.strip().split()))

            # Check if the report is safe as is
            incr = True
            decr = True
            max_diff_valid = True

            for i in range(len(nums) - 1):
                diff = nums[i + 1] - nums[i]

                if not (1 <= abs(diff) <= 3):
                    max_diff_valid = False

                if diff < 0:
                    incr = False
                elif diff > 0:
                    decr = False

            if max_diff_valid and (incr or decr):
                safe += 1
                continue

            # If not safe, check if removing one level makes it safe
            found_safe = False
            for j in range(len(nums)):
                incr = True
                decr = True
                max_diff_valid = True

                modified_nums = nums[:j] + nums[j + 1:]
                for k in range(len(modified_nums) - 1):
                    diff = modified_nums[k + 1] - modified_nums[k]

                    if not (1 <= abs(diff) <= 3):
                        max_diff_valid = False

                    if diff < 0:
                        incr = False
                    elif diff > 0:
                        decr = False

                if max_diff_valid and (incr or decr):
                    found_safe = True
                    break

            if found_safe:
                safe += 1

        return safe


print(solution_b())
