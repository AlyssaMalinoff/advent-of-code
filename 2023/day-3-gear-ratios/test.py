def find_number_with_adjacent_symbol(input_string):
    current_number = ""
    numbers_in_input = []
    for i, char in enumerate(input_string):
        if char.isdigit():
            current_number.append(int(numbers_in_input))
            # Check if the next character is a digit or not
            if i < len(input_string) - 1 and not input_string[i + 1].isdigit():
                print(f"Number found: {current_number}")
                return
        else:
            # If a non-digit character is encountered, reset the current_number
            current_number = ""


# Example input
engine_schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

find_number_with_adjacent_symbol(engine_schematic)
