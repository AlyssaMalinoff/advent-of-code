# Data formatting for both part 1 and part 2. I wanted to create a generic function that could be reused.
def formatting_input_data():
    game_data = []
    with open("input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            # Splits games into two seperate parts, divided by ":"
            parts = line.strip().split(":")

            # This further splits part 0 into two fields, divided by whitespace. We know the game ID will always be in part[1]
            game_id = int(parts[0].split()[1])

            # This splits the original part[1] into the different rounds, divided by the ";"
            game_rounds = parts[1].split(";")

            rounds_info = []
            cube_counts = {"red": 0, "green": 0, "blue": 0}

            for round_info in game_rounds:
                # Splits the game rounds into more fields, divided by ","
                cube_list = round_info.strip().split(", ")
                cube_counts = {}
                for cube in cube_list:
                    # Takes the exact count and color of each cube and updates the running count
                    count, color = cube.split()
                    cube_counts[color] = cube_counts.get(color, 0) + int(count)
                rounds_info.append(cube_counts)

            game_data.append((game_id, rounds_info))
            # print(game_data)

    return game_data


# Check the cube counts and compare them to the specified limits for Part 1
def is_possible(cube_counts):
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    red_count = cube_counts.get("red", 0)
    green_count = cube_counts.get("green", 0)
    blue_count = cube_counts.get("blue", 0)

    return (
        0 <= red_count <= red_limit
        and 0 <= green_count <= green_limit
        and 0 <= blue_count <= blue_limit
    )


# Runs the formatted data through the is_possible function and creates a running sum of games that are valid, returns the answer for Part 1
def valid_games(game_data):
    total_sum_of_valid_games = 0

    for game_id, rounds_info in game_data:
        valid_game = True
        for cube_counts in rounds_info:
            if not is_possible(cube_counts):
                valid_game = False
                break

        if valid_game:
            total_sum_of_valid_games += game_id

    print(f"Sum of Game IDs for Valid Games: {total_sum_of_valid_games}")

    return total_sum_of_valid_games


game_data = formatting_input_data()
valid_games(game_data)


def get_cubed(game_data):
    total_power = []

    for game_id, rounds_info in game_data:
        cube_counts = {"red": 0, "green": 0, "blue": 0}

        # Iterates through colors and counts for each round and finds the max each color has, which is the minimum overall for that round. weird logic.
        for round_counts in rounds_info:
            for color, count in round_counts.items():
                cube_counts[color] = max(cube_counts[color], count)

        # Calculates the cube powers per game, made total_power a list for granularity and troubleshooting.
        game_power = cube_counts["red"] * cube_counts["green"] * cube_counts["blue"]
        total_power.append(game_power)
        total_power_sum = sum(total_power)

    print(f"Sum of Game Powers: {total_power_sum}")


game_data = formatting_input_data()
get_cubed(game_data)

if __name__ == "__main__":
    game_data = formatting_input_data()
