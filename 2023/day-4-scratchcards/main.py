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

    return overall_point_totals, matching_numbers, matches
    return number_of_matches
    return matches


def process_cards_with_copies(input_text):
    card_copies = {}

    # this reads the sample input, iterates over each line to give an index to the line number (game) and the content of that game
    for line_number, line in enumerate(input_text.strip().split("\n")):
        # this initializes every game in the dictionary to be at least 1, because we have 1 copy of every original card
        if line_number not in card_copies:
            card_copies[line_number] = 1

        # Takes the winning/my numbers from the line
        line_content = line.split(":")[1].strip()
        # creates two seperate lists that strip the number sequences and adds them to the lists as ints
        winning_numbers, my_numbers = [
            list(map(int, number_sequence.split()))
            for number_sequence in line_content.split(" | ")
        ]
        # Computes the number of matches between winning_numbers and my_numbers
        matches = sum(number in winning_numbers for number in my_numbers)

        for next_card_number in range(line_number + 1, line_number + matches + 1):
            card_copies[next_card_number] = (
                card_copies.get(next_card_number, 1) + card_copies[line_number]
            )

    total_cards = sum(card_copies.values())
    print(f"Part 2: {total_cards}")

    return total_cards


cards_data = split_games(input_text)
game_points = compare_numbers(cards_data)
cards_after_copies = process_cards_with_copies(input_text)
