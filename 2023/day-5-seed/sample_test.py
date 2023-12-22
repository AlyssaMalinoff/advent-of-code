input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


class Mapping:
    def __init__(self, destinationStart, sourceStart, length):
        self.destinationStart = destinationStart
        self.sourceStart = sourceStart
        self.length = length


def parse_mapping_data(input):
    initial_mappings = []
    for row in input:
        # Skip lines that contain headers
        if len(row) >= 3 and row[0].isdigit():
            mapping = Mapping(int(row[0]), int(row[1]), int(row[2]))
            initial_mappings.append(mapping)

    return initial_mappings


def create_mappings(initial_mappings):
    mappings = {}
    for mapping in initial_mappings:
        for i in range(mapping.length):
            source = mapping.sourceStart + i
            destination = mapping.destinationStart + i
            mappings[source] = destination

    return mappings


# collects the specific seeds we need to find the values for
def extract_seeds(input):
    seeds_line = [line for line in input.split("\n") if line.startswith("seeds:")][0]
    seeds = list(map(int, seeds_line.split()[1:]))
    return seeds


def generate_mappings(input):
    sections = input.strip().split("\n\n")
    result = {}
    for section in sections:
        lines = section.split("\n")
        if lines:
            section_name = lines[0]
            mappings_data = lines[1:]
            parsed_mappings = parse_mapping_data(
                [line.split() for line in mappings_data]
            )
            mappings = create_mappings(parsed_mappings)
            result[section_name] = mappings

    return result


mappings = generate_mappings(input)
print(f"Mappings: {mappings}")
seeds = extract_seeds(input)
print(f"Seeds: {seeds}")
