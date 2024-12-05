import unittest
from time import time
import pandas as pd


def count_xmas_in_dataframe(dataframe):
    rows, cols = dataframe.shape

    xmas_count = 0

    for r in range(rows):
        for c in range(cols):
            if dataframe.iat[r, c] != 'A':
                continue

            if r > 0 and c > 0 and r < rows - 1 and c < cols - 1:
                top_left = dataframe.iat[r - 1, c - 1]
                bottom_right = dataframe.iat[r + 1, c + 1]

                top_right = dataframe.iat[r - 1, c + 1]
                bottom_left = dataframe.iat[r + 1, c - 1]
#                 print(f'''
# {top_left},-,{top_right}
# -,{dataframe.iat[r, c]},-
# {bottom_left},-,{bottom_right}

# top_left in ['X', 'M'] => {top_left in ['X', 'M']}
# bottom_right in ['X', 'M'] => {bottom_right in ['X', 'M']}
# top_left != bottom_right => {top_left != bottom_right}
# top_right in ['X', 'M'] => {top_right in ['X', 'M']}
# bottom_left in ['X', 'M'] => {bottom_left in ['X', 'M']}
# top_right != bottom_left => {top_right != bottom_left}
#                 ''')
                if (
                    top_left in ['S', 'M'] and bottom_right in ['S', 'M'] and top_left != bottom_right and
                    top_right in ['S', 'M'] and bottom_left in [
                        'S', 'M'] and top_right != bottom_left
                ):
                    xmas_count += 1

    return xmas_count


def get_data(name="input.txt"):
    ''''''
    filename = "2024/Day 4: Ceres Search/" + name
    with open(filename, "r") as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]


def main():
    df = pd.DataFrame(get_data())

    count = count_xmas_in_dataframe(df)

    print('count: ', count)


class TestCountXMasInDataframe(unittest.TestCase):
    def test_xmas_word_in_dataframe(self):
        dataframe = pd.DataFrame([
            ['.', 'M', '.', 'S', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', '.', '.', 'M', 'S', 'M', 'S', '.'],
            ['.', 'M', '.', 'S', '.', 'M', 'A', 'A', '.', '.'],
            ['.', '.', 'A', '.', 'A', 'S', 'M', 'S', 'M', '.'],
            ['.', 'M', '.', 'S', '.', 'M', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['S', '.', 'S', '.', 'S', '.', 'S', '.', 'S', '.'],
            ['.', 'A', '.', 'A', '.', 'A', '.', 'A', '.', '.'],
            ['M', '.', 'M', '.', 'M', '.', 'M', '.', 'M', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ])
        expected_count = 9
        actual_count = count_xmas_in_dataframe(dataframe)
        self.assertEqual(actual_count, expected_count)


# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    main()
