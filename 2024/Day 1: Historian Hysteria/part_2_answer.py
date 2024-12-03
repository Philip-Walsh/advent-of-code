def main():
    filename = "2024/Day 1: Historian Hysteria/input.txt"
    left_location_list = []
    right_location_list = []
    len = 0
    final_result = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            len += 1
            result = line.split()
            left_location_list.append(result[0])
            right_location_list.append(result[1])
    for location_id in left_location_list:
        right_count = right_location_list.count(location_id)
        similarity_score = int(location_id) * right_count
        final_result += similarity_score
    print(final_result)

if __name__ == "__main__":
    main()
