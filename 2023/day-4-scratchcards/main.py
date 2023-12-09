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


def split_games():
    # splitting the card games
    lines = input_text.strip().split("\n")

    cards = {}

    for line in lines:
        game_info = line.split(":")

        # card game number
        card_number = game_info[0].strip()

        # splitting the numbers from the card game number
        numbers = game_info[1].strip().split("|")

        winning_numbers = list(map(int, numbers[0].strip().split()))
        game_numbers = list(map(int, numbers[1].strip().split()))

        cards[card_number] = {
            "winning_numbers": winning_numbers,
            "my_numbers": game_numbers,
        }

    for card, data in cards.items():
        print(f"Card Game: {card}")
        # print(f"Data keys: {data.keys()}")
        print(f"Winning Numbers: {data.get('winning_numbers')}")
        print(f"My Numbers: {data.get('my_numbers')}")


split_games()
