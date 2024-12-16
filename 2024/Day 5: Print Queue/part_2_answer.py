import unittest
from time import time
import pandas as pd




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

def apply_rules_to_update(update, ordering_rules):
    # Create a copy of the update to avoid modifying the original list
    unsorted_update = update[:]
    print("Initial update:", unsorted_update)
    
    max_iterations = 100  # Safeguard to prevent infinite loops
    iterations = 0
    
    # Keep iterating until all rules are satisfied
    while not check_update_is_in_correct_order(unsorted_update, ordering_rules):
        iterations += 1
        if iterations > max_iterations:
            print("Exceeded max iterations. Exiting.")
            break
        
        print(f"Iteration {iterations}: Current update:", unsorted_update)
        for rule in ordering_rules:
            if rule[0] in unsorted_update and rule[1] in unsorted_update:
                index_a = unsorted_update.index(rule[0])
                index_b = unsorted_update.index(rule[1])
                
                # If rule is violated, move the element at index_b before index_a
                if index_b > index_a:
                    print(f"Rule {rule} broken. Moving {rule[1]} before {rule[0]}.")
                    unsorted_update.pop(index_b)
                    unsorted_update.insert(index_a, rule[1])
                    print("After applying rule:", unsorted_update)
    
    print("Final sorted update:", unsorted_update)
    return unsorted_update

# def apply_rules_to_update(update, ordering_rules):
#     # Create a copy of the update to avoid modifying the original list
#     unsorted_update = update[:]
    
#     # Keep iterating until all rules are satisfied
#     while not check_update_is_in_correct_order(unsorted_update, ordering_rules):
#         for rule in ordering_rules:
#             if rule[0] in unsorted_update and rule[1] in unsorted_update:
#                 index_a = unsorted_update.index(rule[0])
#                 index_b = unsorted_update.index(rule[1])
                
#                 # If rule is violated, move the element at index_b before index_a
#                 if index_b > index_a:
#                     unsorted_update.pop(index_b)
#                     # unsorted_update.insert(index_a, rule[1])
#                     unsorted_update.append(rule[1])
#     return unsorted_update

#     while not check_update_is_in_correct_order(unsorted_update, ordering_rules):
#             unsorted_update = apply_rules_to_update(unsorted_update, ordering_rules)
#     return unsorted_update


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
        update = apply_rules_to_update(update, ordering_rules)
            # input('ready')
    
        middle_number_sum += update[len(update) // 2]

    # print(middle_number_sum, '< 9420' I keep getting this answer but is incorrec)


# if __name__ == "__main__":
#     main()


class TestCountWordInDataframe(unittest.TestCase):
    
    def test_apply_rules_to_update_correctly_fixes_order(self):

        ordering_rules = [[20, 2], [10, 5], [7, 3]]
        updates = [
            [2, 20, 5, 10, 3, 7],  # Completely incorrect
            [20, 5, 2, 10, 7, 3],  # Partially incorrect
            [20, 10, 7, 3, 5, 2]   # Already correct
        ]
        fixed_updates = [
            apply_rules_to_update(update, ordering_rules)
            for update in updates
        ]
        self.assertEqual(fixed_updates[0], [20, 2, 10, 5, 7, 3])
        self.assertEqual(fixed_updates[1], [20, 10, 5, 7, 3, 2])
        self.assertEqual(fixed_updates[2], [20, 10, 7, 3, 5, 2])

    def test_apply_rules_to_update_handles_complex_scenarios(self):
        ordering_rules = [[20, 2], [10, 5], [7, 3], [15, 10], [25, 20]]
        
        updates = [
            [25, 2, 15, 10, 7, 3, 20, 5],  # Complex case
            [2, 20, 5, 15, 25, 7, 10, 3],  # Mixed order
        ]
        fixed_updates = [
            apply_rules_to_update(update, ordering_rules)
            for update in updates
        ]
        self.assertEqual(fixed_updates[0], [25, 20, 15, 10, 7, 5, 3, 2])
        self.assertEqual(fixed_updates[1], [25, 20, 15, 10, 7, 5, 3, 2])
    # def test_get_data_returns_correct_data(self):
    #     ordering_rules, updates = get_data("input_1.txt")
    #     self.assertEqual(len(ordering_rules), 21)
    #     self.assertEqual(ordering_rules[7], [29, 13])
    #     self.assertEqual(len(updates), 6)
        # self.assertEqual(updates[2], [75, 29, 13])

    # def test_check_update_is_in_correct_order_correct_data(self):
    #     ordering_rules, updates = get_data("input_1.txt")
    #     self.assertTrue(check_update_is_in_correct_order(
    #         updates[0], ordering_rules))
    #     self.assertTrue(check_update_is_in_correct_order(
    #         updates[1], ordering_rules))
    #     self.assertTrue(check_update_is_in_correct_order(
    #         updates[2], ordering_rules))
    #     self.assertFalse(check_update_is_in_correct_order(
    #         updates[3], ordering_rules))
    #     self.assertFalse(check_update_is_in_correct_order(
    #         updates[4], ordering_rules))
    #     self.assertFalse(check_update_is_in_correct_order(
    #         updates[5], ordering_rules))
    #     correct_updates = list(filter(
    #         lambda update: check_update_is_in_correct_order(
    #             update, ordering_rules),
    #         updates
    #     ))
    #     self.assertEqual(len(correct_updates), 3)
    #     middle_number_sum = 0
    #     for update in correct_updates:
    #         middle_number_sum += update[len(update) // 2]
    #     self.assertEqual(middle_number_sum, 143)

    # def test_split_correct_and_incorrect_updates_correct_data(self):
    #     ordering_rules, updates = get_data("input_1.txt")
    #     correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
    #         updates, ordering_rules
    #     )
    #     self.assertEqual(len(correct_updates), 3)
    #     self.assertEqual(len(incorrect_updates), 3)

    # def test_split_correct_and_incorrect_updates_correct_data_actual(self):
    #     ordering_rules, updates = get_data("input.txt")
    #     self.assertEqual(len(updates), 190)

    #     correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
    #         updates, ordering_rules
    #     )
    #     middle_number_sum = 0
    #     for update in correct_updates:
    #         middle_number_sum += update[len(update) // 2]
    #     self.assertEqual(middle_number_sum, 4135)
    #     self.assertEqual(len(correct_updates), 87)
    #     self.assertEqual(len(incorrect_updates), 103)

    def test_apply_rules_to_update(self):

        ordering_rules, updates = get_data("input_1.txt")
        correct_updates, incorrect_updates = split_correct_and_incorrect_updates(
            updates, ordering_rules
        )
        self.assertEqual(apply_rules_to_update(
            incorrect_updates[0], ordering_rules), [97, 75, 47, 61, 53])
        self.assertEqual(apply_rules_to_update(
            incorrect_updates[1], ordering_rules), [61, 29, 13])
        self.assertEqual(apply_rules_to_update(
            incorrect_updates[2], ordering_rules), [97, 75, 47, 29, 13])
# 🎈


if __name__ == "__main__":
    unittest.main()
    # main()