with open("input.txt", "r") as file:
    grid = file.read().splitlines()  # Read file content into a list of lines
    # print("Grid Content:")
    # print(grid)  # Check if the file content is correctly read into the grid variable


# this will give us the coordinates of the first digit of every part number
def get_coordinate_set(grid):
    coordinate_set = set()

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue
            for dr in range(r - 1, r + 2):
                for dc in range(c - 1, c + 2):
                    # checking for out of bounds
                    if (
                        dr < 0
                        or dr >= len(grid)
                        or dc < 0
                        or dc >= len(grid[dr])
                        or not grid[dr][dc].isdigit()
                    ):
                        continue
                    while dc > 0 and grid[dr][dc - 1].isdigit():
                        dc -= 1
                    coordinate_set.add((dr, dc))

    return coordinate_set


# tracks and sums the total of the integers found
def get_sum_of_part_numbers(grid, coordinate_set):
    number_set = []

    for r, c in coordinate_set:
        string_of_part_numbers = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            string_of_part_numbers += grid[r][c]
            # Add 1 to the column so we keep moving rightwards
            c += 1
        if (
            string_of_part_numbers
        ):  # Check if the string_of_part_numbers is not empty before converting
            number_set.append(int(string_of_part_numbers))

    return sum(number_set)


# this will give us the coordinate set for integers adjacent to "*"
def get_gear_set(grid):
    total = 0

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue

            cs = set()

            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if (
                        cr < 0
                        or cr >= len(grid)
                        or cc < 0
                        or cc >= len(grid[cr])
                        or not grid[cr][cc].isdigit()
                    ):
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

            if len(cs) != 2:
                continue

            ns = []

            for cr, cc in cs:
                s = ""
                while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                    s += grid[cr][cc]
                    cc += 1
                ns.append(int(s))

            total += ns[0] * ns[1]

    return total


resulting_coordinate_set = get_coordinate_set(grid)
# print(resulting_coordinate_set)

part_1_result = get_sum_of_part_numbers(grid, resulting_coordinate_set)
print(f"Part One: {part_1_result}")

part_2_result = get_gear_set(grid)
print(f"Part Two:{part_2_result}")
