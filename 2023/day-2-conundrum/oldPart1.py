# Check the cube counts and compare them to the specified limits
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


def weird_elf_game():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        game_sum = 0

        for line in lines:
            parts = line.strip().split(":")
            game_id = int(parts[0].split()[1])
            game_rounds = parts[1].split(";")
            # print(game_rounds)

            valid_game = True
            for round_info in game_rounds:
                cube_list = round_info.strip().split(", ")
                print(cube_list)
                cube_counts = {}

                for cube in cube_list:
                    count, color = cube.split()
                    cube_counts[color] = cube_counts.get(color, 0) + int(count)
                    # print(cube_counts)

                if not is_possible(cube_counts):
                    valid_game = False
                    break

            # Adding the valid game IDs to a running total
            if valid_game:
                # print(game_id)
                game_sum += game_id

        print(f"Sum of Game IDs for Valid Games: {game_sum}")


if __name__ == "__main__":
    weird_elf_game()
