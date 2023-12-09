with open("input.txt", "r") as file:
    grid = file.read().splitlines()  # Read file content into a list of lines
    # print("Grid Content:")
    # print(grid)  # Check if the file content is correctly read into the grid variable


coordinate_set = set()

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue
        for current_row in [r - 1, r, r + 1]:
            for current_column in [c - 1, c, c + 1]:
                # checking for out of bounds
                if (
                    current_row < 0
                    or current_row >= len(grid)
                    or current_column
                    >= len(
                        grid[current_row]
                        or not grid[current_row][current_column].isdigit()
                    )
                ):
                    continue
                while (
                    current_row > 0 and grid[current_row][current_column - 1].isdigit()
                ):
                    current_column -= 1
                coordinate_set.add((current_row, current_column))

print(coordinate_set)
