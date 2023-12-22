# destination range start - source range start - range length
# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

with open("input.txt", "r") as file:
    input_text = file.read()


class Mapping:
    def ___init___(self, destinationStart, sourceStart, length):
        self.destinationStart = destinationStart
        self.sourceStart = sourceStart
        self.length = length


def parse_mapping_data(input):
    initial_mappings = []
    for row in input:
        mapping = Mapping(int(row[0]), int(row[1]), int(row[2]))
        initial_mappings.append(mapping)

    return initial_mappings


def create_mappings(initial_mappings):
    mappings = {}
    for map in initial_mappings:
        for i in range(initial_mappings.length):
            source = initial_mappings.sourceStart + i
            destination = initial_mappings.destinationStart + i
            mappings[source] = destination

    return mappings
