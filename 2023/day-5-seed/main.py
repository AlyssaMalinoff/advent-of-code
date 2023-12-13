
def map_seeds_through_all_mappings(input):
    with open("input.txt", 'r') as file:
        input = file.read()

    seeds, *blocks = input.split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        seed_ranges = []
        for line in block.splitlines()[1:]:
            seed_ranges.append(list(map(int, line.split())))
        mapped_seeds = []
        for x in seeds:
            for first, last, range_length in seed_ranges:
                if last <= x < last + range_length:
                    mapped_seeds.append(x - last + first)
                    break
            else:
                mapped_seeds.append(x)
        seeds = mapped_seeds

    return seeds

# Use the function
final_seeds = map_seeds_through_all_mappings("input.txt")
print(f"Final Seeds: {final_seeds}")
print(f"Part 1: {min(final_seeds)}")
