def solution_a():
    with open("input.txt", "r") as file:
        # load text into 2d arr
        content_raw = file.read()
    
    lines_raw = content_raw.splitlines()    
    total = 0

    # 2d arr e.g. arr[0][1] is second char of first line
    arr = [list(line) for line in lines_raw]

    # getting forward and back will be easy (.count(XMAS/SAMX))
    # we can do same for up and down, just make each col a row
    for x in range(140):
        vert_col = ""
        for y in range(140):
            vert_col += arr[y][x]
        total += (vert_col.count("XMAS") + vert_col.count("SAMX"))
    
    # get forward and backward
    total += (content_raw.count("XMAS") + content_raw.count("SAMX"))
    print(len(arr[0]))
    # get diags
    for x in range(140 - 3):
        for y in range(140 - 3):
            diag_1 = ''.join(
                [
                    arr[x][y],
                    arr[x+1][y+1],
                    arr[x+2][y+2],
                    arr[x+3][y+3]
                ]
            )
            diag_2 = ''.join(
                [
                    arr[x+3][y],
                    arr[x+2][y+1],
                    arr[x+1][y+2],
                    arr[x][y+3]
                ]
            )

            if diag_1 == "XMAS" or diag_1 == "SAMX":
                total += 1

            if diag_2 == "XMAS" or diag_2 == "SAMX":
                total += 1
    
    return total

def solution_b():
    with open("input.txt", "r") as file:
        content_raw = file.read()
    lines_raw = content_raw.splitlines()
    total = 0


    arr = [list(line) for line in lines_raw]

    for x in range(1, 139):  
        for y in range(1, 139):
            if arr[x][y] == "A":  
                if (
                    # top-left -> bottom-right
                    (arr[x-1][y-1] == "M" and arr[x+1][y+1] == "S" and arr[x+1][y-1] == "S" and arr[x-1][y+1] == "M") or
                    (arr[x-1][y-1] == "M" and arr[x+1][y+1] == "S" and arr[x+1][y-1] == "M" and arr[x-1][y+1] == "S") or
                    (arr[x-1][y-1] == "S" and arr[x+1][y+1] == "M" and arr[x+1][y-1] == "M" and arr[x-1][y+1] == "S") or
                    (arr[x-1][y-1] == "S" and arr[x+1][y+1] == "M" and arr[x+1][y-1] == "S" and arr[x-1][y+1] == "M") or
                    
                    # top-right -> bottom-left
                    (arr[x-1][y+1] == "M" and arr[x+1][y-1] == "S" and arr[x-1][y-1] == "M" and arr[x+1][y+1] == "S") or
                    (arr[x-1][y+1] == "M" and arr[x+1][y-1] == "S" and arr[x-1][y-1] == "S" and arr[x+1][y+1] == "M") or
                    (arr[x-1][y+1] == "S" and arr[x+1][y-1] == "M" and arr[x-1][y-1] == "M" and arr[x+1][y+1] == "S") or
                    (arr[x-1][y+1] == "S" and arr[x+1][y-1] == "M" and arr[x-1][y-1] == "S" and arr[x+1][y+1] == "M")
                ):
                    total += 1

    return total


print(solution_a())
print(solution_b())