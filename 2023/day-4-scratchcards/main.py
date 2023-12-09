# with open("input.txt", "r") as file:
#     input = file.read().splitlines()
input_text = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def split_games(input_text):
    # splitting the card games
    lines = input_text.strip().split("\n")
    cards = {}

    for line in lines:
        game_info = line.split(":")

        # card game number
        card_number = game_info[0].strip()

        # splitting the winning/my_numbers from the card game number
        numbers = game_info[1].strip().split("|")

        winning_numbers = list(map(int, numbers[0].strip().split()))
        game_numbers = list(map(int, numbers[1].strip().split()))

        cards[card_number] = {
            "winning_numbers": winning_numbers,
            "my_numbers": game_numbers,
        }

    return cards

    # for card, data in cards.items():
    #     print(f"Card Game: {card}")
    #     # print(f"Data keys: {data.keys()}")
    #     print(f"Winning Numbers: {data.get('winning_numbers')}")
    #     print(f"My Numbers: {data.get('my_numbers')}")


def compare_numbers(cards_data):
    game_point_total = {}

    for card, data in cards_data.items():
        winning_numbers = set(data["winning_numbers"])
        my_numbers = set(data["my_numbers"])

        # compares the winning numbers and the game numbers
        matching_numbers = winning_numbers.intersection(my_numbers)

        matches = len(matching_numbers)

        points = 2 ** (matches - 1) if matches > 0 else 0

        game_point_total[card] = points

        overall_point_totals = sum(points for game, points in game_point_total.items())

        print(f"Card Game: {card}")
        print(f"Winning Numbers: {winning_numbers}")
        print(f"My Numbers: {my_numbers}")
        # fixes the issue of Matching numbers displaying set()
        print(
            f"Matching Numbers: {'No Matching Numbers' if not matching_numbers else matching_numbers}"
        )
        print(f"Game Point Total: {points}")

    print(f"Summary: {game_point_total}")
    print(f"Part 1: {overall_point_totals}")

    return overall_point_totals


cards_data = split_games(input_text)
game_points = compare_numbers(cards_data)
