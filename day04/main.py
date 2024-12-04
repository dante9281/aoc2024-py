from aocd import get_data

def part_a(data):
    items = data.split('\n')
    xmas_count = 0
    # items[x] is each line in the word search
    # items[x][y] is each letter
    for x in range(len(items)):
        # check for the letter X, then check around it
        for y in range(len(items[x])):
            if (items[x][y] == "X"):
                # yolo time, might refactor
                # up left
                if (x - 1) >= 0 and (y - 1) >= 0 and items[x-1][y-1] == "M":
                    if (x - 2) >= 0 and (y - 2) >= 0 and items[x-2][y-2] == "A":
                        if (x - 3) >= 0 and (y - 3) >= 0 and items[x-3][y-3] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # up
                if (x - 1) >= 0 and items[x-1][y] == "M":
                    if (x - 2) >= 0 and items[x-2][y] == "A":
                        if (x - 3) >= 0 and items[x-3][y] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # up right
                if (x - 1) >= 0 and (y + 1) < len(items[x]) and items[x-1][y+1] == "M":
                    if (x - 2) >= 0 and (y + 2) < len(items[x]) and items[x-2][y+2] == "A":
                        if (x - 3) >= 0 and (y + 3) < len(items[x]) and items[x-3][y+3] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # right
                if (y + 1) < len(items[x]) and items[x][y+1] == "M":
                    if (y + 2) < len(items[x]) and items[x][y+2] == "A":
                        if (y + 3) < len(items[x]) and items[x][y+3] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # down right
                if (x + 1) < len(items) and (y + 1) < len(items[x]) and items[x+1][y+1] == "M":
                    if (x + 2) < len(items) and (y + 2) < len(items[x]) and items[x+2][y+2] == "A":
                        if (x + 3) < len(items) and (y + 3) < len(items[x]) and items[x+3][y+3] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # down
                if (x + 1) < len(items) and items[x+1][y] == "M":
                    if (x + 2) < len(items) and items[x+2][y] == "A":
                        if (x + 3) < len(items) and items[x+3][y] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # down left
                if (x + 1) < len(items) and (y - 1) >= 0 and items[x+1][y-1] == "M":
                    if (x + 2) < len(items) and (y - 2) >= 0 and items[x+2][y-2] == "A":
                        if (x + 3) < len(items) and (y - 3) >= 0 and items[x+3][y-3] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
                # left
                if (y - 1) >= 0 and items[x][y-1] == "M":
                    if (y - 2) >= 0 and items[x][y-2] == "A":
                        if (y - 3) >= 0 and items[x][y-3] == "S":
                            # print("Result found at " + str(x) + "," + str(y))
                            xmas_count += 1
    # print(xmas_count)
    return xmas_count


def part_b(data):
    items = data.split('\n')
    x_mas_count = 0
    # items[x] is the row
    # items[x][y] is the letter in the row
    # why were the elves allowed to do this?
    for x in range(len(items)):
        # yolo time again
        # should be simpler?
        for y in range(len(items[x])):
            if items[x][y] == "A":
                # M is up
                if (x - 1) >= 0 and (y - 1) >= 0 and (y + 1) < len(items[x]) and items[x-1][y-1] == "M" and items[x-1][y+1] == "M":
                    if (x + 1) < len(items) and items[x+1][y-1] == "S" and items[x+1][y+1] == "S":
                        x_mas_count += 1
                # M is down
                if (x + 1) < len(items) and (y - 1) >= 0 and (y + 1) < len(items[x]) and items[x+1][y-1] == "M" and items[x+1][y+1] == "M":
                    if (x - 1) >= 0 and items[x-1][y-1] == "S" and items[x-1][y+1] == "S":
                        x_mas_count += 1
                # M is left
                if (x - 1) >= 0 and (x + 1) < len(items) and (y - 1) >= 0 and items[x-1][y-1] == "M" and items[x+1][y-1] == "M":
                    if (y + 1) < len(items[x]) and items[x-1][y+1] == "S" and items[x+1][y+1] == "S":
                        x_mas_count += 1
                # M is right
                if (x - 1) >= 0 and (x + 1) < len(items) and (y + 1) < len(items) and items[x-1][y+1] == "M" and items[x+1][y+1] == "M":
                    if (y - 1) >= 0 and items[x-1][y-1] == "S" and items[x+1][y-1] == "S":
                        x_mas_count += 1
    return x_mas_count


test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


if __name__ == "__main__":
    data = get_data(day=4, year=2024)
    assert part_a(test_data) == 18
    assert part_b(test_data) == 9
    print(part_a(data))
    print(part_b(data))
