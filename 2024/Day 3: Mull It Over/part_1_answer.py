import re


def get_data():
    ''''''
    filename = "2024/Day 3: Mull It Over/input.txt"
    with open(filename, "r") as f:
        return f.read()


def main():
    final_result = 0
    mulRegex = r'mul\([0-9]+,[0-9]+\)'
    data = ''.join(
                list(
                    filter(
                        lambda x: not x.startswith('n\'t()'),
                        get_data().split('do')
                    )
                )
            )
    print(data)
    matches = re.findall(mulRegex, data)
    for match in matches:

        nums = [int(i) for i in match.replace(
            'mul(', '').replace(')', '').split(',')]
        final_result += nums[0] * nums[1]

    print(final_result)


if __name__ == "__main__":
    main()
