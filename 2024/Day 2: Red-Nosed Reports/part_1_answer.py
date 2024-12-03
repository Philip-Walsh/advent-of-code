def get_data():
    ''''''
    filename = "2024/Day 2: Red-Nosed Reports/input.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
        return [line.strip().split() for line in lines]


def is_line_safe(line):
    '''
    a report only counts as safe if both of the following are true:
        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    '''
    items = line
    is_increasing = True
    is_decreasing = True
    is_diff_correct = True

    for i in range(len(items) - 1):
        if is_increasing and not int(items[i]) < int(items[i + 1]):
            # print('line is not increasing:')
            is_increasing = False
        if is_diff_correct:
            diff = abs(int(items[i]) - int(items[i + 1]))
            if diff < 1 or diff > 3:
                # print('level difference is not between 1 and 3:')
                is_diff_correct = False
        if is_decreasing and not int(items[i]) > int(items[i + 1]):
            # print('line is not decreasing:')
            is_decreasing = False

    return (is_increasing or is_decreasing) and is_diff_correct


def main():
    ''''''
    data = get_data()
    safe = 0
    for line in data:
        is_safe = is_line_safe(line)
        if is_safe:
            safe += 1
        print(line, "safe" if is_safe else "unsafe")
    print(f'Safe Reports: {safe}')


if __name__ == "__main__":
    main()
