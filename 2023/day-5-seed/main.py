# destination range start - source range start - range length
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

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


# map:
# seed-to-soil map:
# 50 98 2
# 52 50 48

# map = [50, 98, 2]
# for step in map[2]:
#     map[1] + [step - 1] maps to map[0] + [step -1]

# 98 -> 50
# 99 -> 51


class Mapping:
    def ___init___(self, destinationStart, sourceStart, length):
        self.destinationStart = destinationStart
        self.sourceStart = sourceStart
        self.length = length


def parse_mapping_data(input):
    mappings = []
    for row in input:
        mapping = Mapping(int(row[0]), int(row[1]), int(row[2]))
        mappings.append(mapping)

    return mappings
