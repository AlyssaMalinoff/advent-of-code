inputs, *blocks = open("input.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seed_ranges = []

for i in range(0, len(inputs), 2):
    seed_ranges.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    block_ranges = []
    for line in block.splitlines()[1:]:
        block_ranges.append(list(map(int, line.split())))
    new_seed_ranges = []
    while len(seed_ranges) > 0:
        seed_start, seed_end = seed_ranges.pop()
        for block_start, range_start, range_length in block_ranges:
            overlap_start = max(seed_start, range_start)
            overlap_end = min(seed_end, range_start + range_length)
            if overlap_start < overlap_end:
                new_seed_ranges.append((overlap_start - range_start + block_start, overlap_end - range_start + block_start))
                if overlap_start > seed_start:
                    seed_ranges.append((seed_start, overlap_start))
                if seed_end > overlap_end:
                    seed_ranges.append((overlap_end, seed_end))
                break
        else:
            new_seed_ranges.append((seed_start, seed_end))
    seed_ranges = new_seed_ranges

print(min(seed_ranges)[0])
