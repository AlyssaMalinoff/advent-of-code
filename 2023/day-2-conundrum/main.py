# Check the cube counts and compare them to the specified limits
def is_possible(cube_counts):
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    red_count = cube_counts.get("red", 0)
    green_count = cube_counts.get("green", 0)
    blue_count = cube_counts.get("blue", 0)

    print(
        f"Red count: {red_count}, Green count: {green_count}, Blue count: {blue_count}"
    )
    print(
        f"Red limit: {red_limit}, Green limit: {green_limit}, Blue limit: {blue_limit}"
    )

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
            cubes_info = parts[1].split(";")

            valid_game = True
            for round_info in cubes_info:
                cube_list = round_info.strip().split(", ")
                cube_counts = {}

                for cube in cube_list:
                    count, color = cube.split()
                    cube_counts[color] = cube_counts.get(color, 0) + int(count)

                if not is_possible(cube_counts):
                    valid_game = False
                    break

            if valid_game:
                game_sum += game_id

        print(f"Sum of Game IDs for Valid Games: {game_sum}")


if __name__ == "__main__":
    weird_elf_game()
