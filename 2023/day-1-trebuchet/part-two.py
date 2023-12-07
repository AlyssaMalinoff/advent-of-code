def convert_text_numbers(string):
    word_to_digit = {
        "oneight": "18",
        "twone": "21",
        "threeight": "38",
        "fiveight": "58",
        "sevenine": "79",
        "eightwo": "82",
        "eighthree": "83",
        "nineight": "98",
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for word, digit in word_to_digit.items():
        string = string.replace(word, digit)

    numbers = "".join(filter(str.isdigit, string))
    return numbers


def calculate_calibration_values():
    total_sum = 0
    calibration_values = []

    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = convert_text_numbers(line)  # Process textual numbers
        first_digit = 0
        last_digit = 0

        for char in line:
            if char.isdigit():
                if first_digit == 0:
                    first_digit = int(char)
                last_digit = int(char)

        if first_digit != 0 and last_digit != 0:
            calibration_value = int(str(first_digit) + str(last_digit))
            calibration_values.append(calibration_value)

    total_sum = sum(calibration_values)
    return total_sum


if __name__ == "__main__":
    result = calculate_calibration_values()
    print(result)
