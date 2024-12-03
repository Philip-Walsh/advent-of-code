def main():
    filename = "2024/Day 1: Historian Hysteria/input.txt"
    location_list_1 = []
    location_list_2 = []
    len = 0
    final_result = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            len += 1
            result = line.split()
            location_list_1.append(result[0])
            location_list_2.append(result[1])

    location_list_1.sort()
    location_list_2.sort()
    for i in range(0, len):
        result = int(location_list_1[i]) - int(location_list_2[i])
        if result < 0:
            result = result * -1
        final_result += result
    print(final_result)


if __name__ == "__main__":
    main()
