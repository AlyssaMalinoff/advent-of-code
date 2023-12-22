with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

times, distances = [list(map(int, line.split(":")[1].split())) for line in input_text if ":" in line]

total_record = 1

for time, distance in zip(times, distances):
    margin = 0
    for button_hold in range(time):
        if button_hold * (time - button_hold) > distance:
            margin += 1
    total_record *= margin

print(f"Part 1: {total_record}")