import unittest
from time import time
import pandas as pd


def get_data(name="input.txt"):
    ''''''
    filename = "2024/Day 5: Print Queue/" + name
    ordering_rules = []
    updates = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if '|' in line:
                ordering_rules.append([int(l)
                                      for l in line.strip().split('|')])
            elif ',' in line:
                updates.append([int(l) for l in line.strip().split(',')])

    return ordering_rules, updates


def check_update_is_in_correct_order(update, ordering_rules):
    for rule in ordering_rules:
        for i, num in enumerate(update):
            if num == rule[0] and rule[1] in update[:i]:
                # print('update: ', update, 'rule: ', rule, 'index: ', i, update[:i])
                return False
    return True


def main():
    ordering_rules, updates = get_data()
    correct_updates = list(filter(
        lambda update: check_update_is_in_correct_order(
            update, ordering_rules),
        updates
    ))
    middle_number_sum = 0
    for update in correct_updates:
        middle_number_sum += update[len(update) // 2]
    print(middle_number_sum)


class TestCountWordInDataframe(unittest.TestCase):
    def test_get_data_returns_correct_data(self):
        ordering_rules, updates = get_data("input_1.txt")
        self.assertEqual(len(ordering_rules), 21)
        self.assertEqual(ordering_rules[7], [29, 13])
        self.assertEqual(len(updates), 6)
        self.assertEqual(updates[2], [75, 29, 13])

    def test_check_update_is_in_correct_order_correct_data(self):
        ordering_rules, updates = get_data("input_1.txt")
        self.assertTrue(check_update_is_in_correct_order(
            updates[0], ordering_rules))
        self.assertTrue(check_update_is_in_correct_order(
            updates[1], ordering_rules))
        self.assertTrue(check_update_is_in_correct_order(
            updates[2], ordering_rules))
        self.assertFalse(check_update_is_in_correct_order(
            updates[3], ordering_rules))
        self.assertFalse(check_update_is_in_correct_order(
            updates[4], ordering_rules))
        self.assertFalse(check_update_is_in_correct_order(
            updates[5], ordering_rules))
        correct_updates = list(filter(
            lambda update: check_update_is_in_correct_order(
                update, ordering_rules),
            updates
        ))
        self.assertEqual(len(correct_updates), 3)
        middle_number_sum = 0
        for update in correct_updates:
            middle_number_sum += update[len(update) // 2]
        self.assertEqual(middle_number_sum, 143)


# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    main()
