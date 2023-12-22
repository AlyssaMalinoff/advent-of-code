import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Change the working directory to the script directory
os.chdir(script_dir)

with open("input.txt", "r") as file:
    input_text = file.read().splitlines()

times, distances = [list(map(int, line.split(":")[1].split())) for line in input_text if ":" in line]

TotalRecord = 1

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1
    TotalRecord *= margin

print(f"Part 1: {TotalRecord}")