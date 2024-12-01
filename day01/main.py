from aocd import get_data


def part_a(data):
    # Parse the input file
    items = data.split('\n')
    # instantiate empty arrays, we'll sort this later
    first = []
    second = []
    distance = 0
    # loop through input data to populate the list
    for i in range(len(items)):
        # Put the first number in the first list,
        # second number in the second list
        item = items[i]
        ids = item.split("   ")
        first.append(ids[0])
        second.append(ids[1])
    # sort the lists smallest to largest
    first.sort()
    second.sort()
    # find the difference between each list (absolute value)
    for n in range(len(first)):
        distance += abs(int(first[n]) - int(second[n]))
    # add up all the distance differences
    return distance


def part_b(data):
    items = data.split('\n')
    # First loop:
    # populate lists
    first = []
    second = []
    for i in range(len(items)):
        item = items[i]
        ids = item.split("   ")
        first.append(ids[0])
        second.append(ids[1])
    # Second loop:
    # Go through second and make a dictionary with each unique value as a key,
    # and the number of times it appears as a value
    simValues = {}
    for n in range(len(second)):
        if second[n] in simValues:
            simValues[second[n]] = simValues[second[n]] + 1
        else:
            simValues[second[n]] = 1
    # Third loop:
    # Go through first and multiply each value by simValues[item],
    # and add to the similarity score
    simScore = 0
    for n in range(len(first)):
        if first[n] in simValues:
            simScore += int(first[n]) * simValues[first[n]]
    return simScore


test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""


if __name__ == "__main__":
    data = get_data(day=1, year=2024)
    assert part_a(test_data) == 11
    assert part_b(test_data) == 31
    print(part_a(data))
    print(part_b(data))
