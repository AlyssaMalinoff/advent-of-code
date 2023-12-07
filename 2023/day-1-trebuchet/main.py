def calculate_calibration_values():
    total_sum = 0
    # Making each lines value an entry in a list that we can sum
    calibration_values = []

    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Iterating through each entry in lines
    for line in lines:
        first_digit = 0
        last_digit = 0

        # Iterating through each character in that line to select the int
        for char in line:
            if char.isdigit():
                if first_digit == 0:
                    first_digit = int(char)
                last_digit = int(char)

        if first_digit != 0 and last_digit != 0:
            # Concatenate
            calibration_value = int(str(first_digit) + str(last_digit))
            calibration_values.append(calibration_value)

    # Calculate the total_sum by summing all values in the calibration_values list
    total_sum = sum(calibration_values)

    # return total_sum
    print(calibration_values)


if __name__ == "__main__":
    result = calculate_calibration_values()
    print(result)
