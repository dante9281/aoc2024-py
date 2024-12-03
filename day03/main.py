from aocd import get_data
import re


def part_a(data):
    # Parse the input file
    items = data.split('\n')
    # regex to find all instances of mul() that are valid
    matches = re.findall(r"mul\(\d{0,3},\d{0,3}\)", str(items))
    result = 0
    for i in range(len(matches)):
        match = matches[i]
        # Grab the numbers and multiply them
        x = match[4:match.index(",")]
        y = match[match.index(",")+1:-1]
        result += int(x) * int(y)
    return result


def part_b(data):
    items = data.split('\n')
    # Same regex, but it also finds do() and don't()
    # Unfortunately, this makes a tuple with values for every group
    # index 0 is mul()
    # index 1 is either do() or don't()
    # index 2 is the "n't"
    matches = re.findall(r"(mul\(\d{0,3},\d{0,3}\))|(do(n\'t)?\(\))",
                         str(items))
    result = 0
    enabled = True
    for i in range(len(matches)):
        match = matches[i]
        if match[1].find("don\'t") != -1:
            enabled = False
            continue
        elif match[1].find("do") != -1:
            enabled = True
            continue
        if enabled:
            x = match[0][4:match[0].index(",")]
            y = match[0][match[0].index(",")+1:-1]
            result += int(x) * int(y)
    return result


test_data1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
test_data2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


if __name__ == "__main__":
    data = get_data(day=3, year=2024)
    assert part_a(test_data1) == 161
    assert part_b(test_data2) == 48
    print(part_a(data))
    print(part_b(data))
