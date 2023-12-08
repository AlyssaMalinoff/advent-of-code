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


def formatting_input_data():
    game_data = []
    with open("input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(":")
            game_id = int(parts[0].split()[1])
            game_rounds = parts[1].split(";")

            rounds_info = []
            for round_info in game_rounds:
                cube_list = round_info.strip().split(", ")
                cube_counts = {}
                for cube in cube_list:
                    count, color = cube.split()
                    cube_counts[color] = cube_counts.get(color, 0) + int(count)
                rounds_info.append(cube_counts)

            game_data.append((game_id, rounds_info))

    return game_data


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


game_data = formatting_input_data()
valid_games(game_data)
