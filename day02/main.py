from aocd import get_data


def safe_change(a, b):
    diff = abs(a - b)
    if diff != 0 and diff >= 1 and diff <= 3:
        return True
    else:
        return False


def check_level(levels):
    isSafe = True
    ascending = descending = False
    j = 0
    while (j < len(levels) - 1) and isSafe:
        # Levels must change by 1-3
        if not safe_change(int(levels[j]), int(levels[j+1])):
            return False
        if int(levels[j]) < int(levels[j+1]):
            ascending = True
        elif int(levels[j]) > int(levels[j+1]):
            descending = True
        if ascending and descending:
            return False
        j += 1
    return True


def part_a(data):
    # Parse the input file
    items = data.split('\n')
    safeNum = 0
    for i in range(len(items)):
        # make an array
        item = items[i]
        levels = item.split(' ')
        if check_level(levels):
            safeNum += 1
    return safeNum


def part_b(data):
    # Parse the input file
    items = data.split('\n')
    safeNum = 0
    for i in range(len(items)):
        # make an array
        item = items[i]
        levels = item.split(' ')
        # Levels must be ascending or descending
        isSafe = check_level(levels)
        if not isSafe:
            # Attempt to use dampener
            # Admittedly a brute force attempt
            for n in range(len(levels)):
                dampener = levels.copy()
                dampener.pop(n)
                if check_level(dampener):
                    safeNum += 1
                    break
        else:
            safeNum += 1
    return safeNum


test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


if __name__ == "__main__":
    data = get_data(day=2, year=2024)
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4
    print(part_a(data))
    print(part_b(data))
