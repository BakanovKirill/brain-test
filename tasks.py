#!/usr/bin/env python3
import re


def merge_intervals(intervals):
    # make sure they are sorted by first element removing need to compare.
    # intervals[i][0] <= intervals[i+1][0] after sort
    intervals.sort(key=lambda interval: interval[0])
    result = [intervals[0]]
    for current in intervals:
        previous = result[-1]  # last element from list
        # Merge if intervals look like this:
        # prev_0---curr_0---prev_1---curr_1
        # prev_0---curr_0---curr_1---prev_1
        if current[0] <= previous[1]:
            # as seen from the visual comment above, we need only to choose curr_1 or prev_1
            # as the end of merged interval
            previous[1] = max(previous[1], current[1])
        else:
            result.append(current)
    return result


def string_darts(target, words_lst):
    """
    Returns True if a target string can be represented with any subset of words_list or whole_words_list

    :param target: any string, ex. "Hello there!"
    :param words_lst: list of lower cased characters or words, ex. ['a', 'bc', 'hello', '.']
    :return: True/False
    """
    # Check the easiest case if we compare 2 similar strings
    if len(words_lst) == 1 and words_lst[0] == target:
        return True
    # Remove all whitespaces, lowercase the input string
    target = target.replace(" ", "").lower()
    # Create a comparator index list aka darts board,
    # where words replace 0 with 1 in a range of indices of the target if hit.
    target_darts_board = [0] * len(target)
    for word in words_lst:
        dart = [1] * len(word)
        for m in re.finditer(word, target):
            # Fill range in board when we found a word
            target_darts_board[m.start() : m.end()] = dart
            # If all 0 are replaced with 1, then we filled the whole target!
            if sum(target_darts_board) == len(target_darts_board):
                return True
    return False


if __name__ == "__main__":
    print("Running: merge_intervals")

    input_intervals = [[-1, 15], [-10, 3], [13, 28], [40, 50], [50, 100]]
    print(f"Input: {input_intervals}")

    merged_intervals = merge_intervals(input_intervals)
    print(f"Output: {merged_intervals}")

    print("\n================\n")

    print("Running: string_darts")
    text = "I am eating a frog"
    words = ["i", "eat", "ing", "am", "a", "frog"]
    print(f"Test string: '{text}'")
    print(f"Words array: {words}")
    can_represent = string_darts(target=text, words_lst=words)
    print(f"Result: {can_represent}")
