import unittest
from time import time
import pandas as pd


def count_word_in_dataframe(dataframe, word):
    rows, cols = dataframe.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (1, 1), (-1, 1), (1, -1)]
    word_length = len(word)

    def is_valid_path(r, c, dr, dc):
        path = []
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols and dataframe.iat[nr, nc] == word[i]):
                return None
            path.append((nr, nc))
        return path

    all_paths = set()

    for r in range(rows):
        for c in range(cols):
            # Start searching only if the first letter matches
            if dataframe.iat[r, c] == word[0]:
                for dr, dc in directions:
                    path = is_valid_path(r, c, dr, dc)
                    if path:
                        all_paths.add(tuple(path))

    return len(all_paths), list(all_paths)


def get_data(name="input.txt"):
    ''''''
    filename = "2024/Day 4: Ceres Search/"+ name
    with open(filename, "r") as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]


def main():
    df = pd.DataFrame(get_data())
    search_word = "XMAS"

    count, paths = count_word_in_dataframe(df, search_word)
    print(df)
    print(df.shape)

    print(count)


class TestCountWordInDataframe(unittest.TestCase):
    def test_count_word_in_dataframe(self):
        dataframe = pd.DataFrame([
            ['.', '.', 'X', '.', '.', '.'],
            ['.', 'S', 'A', 'M', 'X', '.'],
            ['.', 'A', '.', '.', 'A', '.'],
            ['X', 'M', 'A', 'S', '.', 'S'],
            ['.', 'X', '.', '.', '.', '.']
        ])
        search_word = 'X'
        expected_count = 4
        actual_count, _ = count_word_in_dataframe(dataframe, search_word)
        self.assertEqual(actual_count, expected_count)

    def test_count_word_in_dataframe_from_file(self):
        dataframe = pd.DataFrame(get_data("input_1.txt"))
        search_word = 'X'
        expected_count = 4
        actual_count, _ = count_word_in_dataframe(dataframe, search_word)
        self.assertEqual(actual_count, expected_count)

    def test_count_word_not_found(self):
        dataframe = pd.DataFrame([
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'x', 'h']
        ])
        search_word = 'XX'
        expected_count = 0
        actual_count, _ = count_word_in_dataframe(dataframe, search_word)
        self.assertEqual(actual_count, expected_count)

    def test_count_full_word(self):
        dataframe = pd.DataFrame([
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I']
        ])
        search_word = 'BE'
        expected_count = 1
        actual_count, _ = count_word_in_dataframe(dataframe, search_word)
        self.assertEqual(actual_count, expected_count)

    def test_basic_horizontal_word(self):
        dataframe = pd.DataFrame([
            ['X', 'M', 'A', 'S']
        ])
        search_word = 'XMAS'
        expected_count = 1
        actual_count, _ = count_word_in_dataframe(dataframe, search_word)
        self.assertEqual(actual_count, expected_count)

    def test_count_full_word_in_complex_speed(self):
        dataframe = pd.DataFrame([
            ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
            ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
            ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
            ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
            ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
            ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
            ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
            ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
            ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
            ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
        ])
        search_word = 'XMAS'
        expected_count = 18
        start_time = time()
        actual_count, matches = count_word_in_dataframe(dataframe, search_word)
        # c = [set(list(m)) for m in matches]
        # [print(m) for m in c]
        print(len(matches))
        duration = time() - start_time
        self.assertEqual(len(matches), expected_count)
        # self.assertEqual(len(c), expected_count)
        self.assertEqual(actual_count, expected_count)
        self.assertLess(duration, 0.1)


# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    main()
