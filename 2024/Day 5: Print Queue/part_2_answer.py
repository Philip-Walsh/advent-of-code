import unittest
from time import time
import panda as pd


def get_data(name="input.txt"):
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
                return False
    return True


def split_correct_and_incorrect_updates(updates, ordering_rules):
    correct_updates, incorrect_updates = [], []
    for update in updates:
        if check_update_is_in_correct_order(update, ordering_rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    return correct_updates, incorrect_updates


def fix_incorrect_updates(update, ordering_rules):
    update = update[:]
    for rule in ordering_rules:
        for i, num in enumerate(update):
            if num == rule[0] and rule[1] in update[:i]:
                incorrect_val = rule[1]
                update.pop(update.index(incorrect_val))
                update.append(incorrect_val)
    if not check_update_is_in_correct_order(update, ordering_rules):
        update = fix_incorrect_updates(update, ordering_rules)
    return update


def main():
    ordering_rules, updates = get_data()
    # Ensure all updates are isolated copies
    updates = [update[:] for update in updates]
    correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
        updates, ordering_rules)

    middle_number_sum = 0
    for update in correct_updates:
        middle_number_sum += update[len(update) // 2]

    print(middle_number_sum, '== 4135')

    for i, update in enumerate(incorrect_updates):
        fixed_update = fix_incorrect_updates(update, ordering_rules)
        while not check_update_is_in_correct_order(fixed_update, ordering_rules):
            fixed_update = fix_incorrect_updates(fixed_update, ordering_rules)
        middle_number_sum += fixed_update[len(fixed_update) // 2]

    print(middle_number_sum, '< 9420')


if __name__ == "__main__":
    main()


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

    def test_split_correct_and_incorrect_updates_correct_data(self):
        ordering_rules, updates = get_data("input_1.txt")
        correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
            updates, ordering_rules
        )
        self.assertEqual(len(correct_updates), 3)
        self.assertEqual(len(incorrect_updates), 3)

    def test_split_correct_and_incorrect_updates_correct_data_actual(self):
        ordering_rules, updates = get_data("input.txt")
        self.assertEqual(len(updates), 190)

        correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
            updates, ordering_rules
        )
        middle_number_sum = 0
        for update in correct_updates:
            middle_number_sum += update[len(update) // 2]
        self.assertEqual(middle_number_sum, 4135)
        self.assertEqual(len(correct_updates), 87)
        self.assertEqual(len(incorrect_updates), 103)

    def test_fix_incorrect_updates(self):

        ordering_rules, updates = get_data("input_1.txt")
        correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
            updates, ordering_rules
        )
        self.assertEqual(fix_incorrect_updates(
            incorrect_updates[0], ordering_rules), [97, 75, 47, 61, 53])
        self.assertEqual(fix_incorrect_updates(
            incorrect_updates[1], ordering_rules), [61, 29, 13])
        self.assertEqual(fix_incorrect_updates(
            incorrect_updates[2], ordering_rules), [97, 75, 47, 29, 13])


if __name__ == "__main__":
    unittest.main()
    # main()

# if __name__ == "__main__":
