def read_input_from_file(input):
    with open("input.txt", "r") as file:
        input_text = file.read()
    return input_text


input_text = read_input_from_file("input.txt")


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
    return cards_data

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

    return (
        overall_point_totals,
        matching_numbers,
    )
    return matches
    return number_of_matches


def process_cards(card_data):
    card_copies = {}

    for card_number, data in cards_data.items():
        matches = len(
            set(data["winning_numbers"]).intersection(set(data["my_numbers"]))
        )

        if card_num not in card_data:
            continue

        matches = len(
            set(card_data[card_num]["winning_numbers"]).intersection(
                set(card_data[card_num]["my_numbers"])
            )
        )

        if card_num not in card_copies:
            card_copies[card_num] = 0

        for next_card in range(i + 1, 219):
            if next_card not in card_copies:
                card_copies[next_card] = 0

            copies_to_add = card_copies[card_num] if matches > 0 else 0
            card_copies[next_card] += copies_to_add

            if matches == 0 or card_copies[next_card] == 0:
                break

    card_copies = {card: copies for card, copies in card_copies.items() if copies > 0}
    return card_copies


def add_copies():
    card_pile = {}


# Use your existing functions to get card data
input_text = read_input_from_file("input.txt")
cards_data = split_games(input_text)


cards_data = split_games(input_text)
game_points = compare_numbers(cards_data)
result = process_cards(cards_data)
print(result)
