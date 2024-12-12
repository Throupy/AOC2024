def solution_a():
    with open("input.txt", "r") as f:
        rules_sec, updates_sec = f.read().strip().split("\n\n")
    
    rules = [tuple(map(int, line.split("|"))) for line in rules_sec.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_sec.splitlines()]

    valid_updates = []

    for update in updates:
        # get all relevant rules, might make it more efficient?
        relevant_rules = [(x, y) for x, y in rules if x in update and y in update]
        valid = True
        for first, second in relevant_rules:
            if update.index(first) > update.index(second):
                print(f"Rule {first}|{second} violates the update string")
                valid = False
                break
        if valid:
            valid_updates.append(update)

    return valid_updates

def solution_b():
    with open("input.txt", "r") as f:
        rules_sec, updates_sec = f.read().strip().split("\n\n")
    
    rules = [tuple(map(int, line.split("|"))) for line in rules_sec.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_sec.splitlines()]

    reordered_updates = []

    for update in updates:
        relevant_rules = [(x, y) for x, y in rules if x in update and y in update]

        valid = True
        for first, second in relevant_rules:
            if update.index(first) > update.index(second):
                valid = False
                break
        
        if not valid:
            while True:
                changes = 0
                for first, second in relevant_rules:
                    if update.index(first) > update.index(second):
                        first_idx = update.index(first)
                        second_idx = update.index(second)
                        update[first_idx], update[second_idx] = update[second_idx], update[first_idx]
                        changes += 1

                if changes == 0:
                    break
            
            reordered_updates.append(update)

    return reordered_updates




result = solution_b()
sum_of_middles = sum(update[len(update) // 2] for update in result)
print(sum_of_middles)