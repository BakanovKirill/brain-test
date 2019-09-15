#!/usr/bin/env python3
import re
import pytest


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


@pytest.mark.parametrize(
    "target,words, expected",
    [
        pytest.param(
            "well hello there", ["well hello there"], True, id="single-operation-ok"
        ),
        pytest.param(
            "well hello there", ["there", "hello", "well"], True, id="no-repeat-ok"
        ),
        pytest.param(
            "Well heLlo theRe",
            ["there", "he", "l", "o", "we"],
            True,
            id="with-repeats-ok",
        ),
        pytest.param(
            "Well hello there. General Kenobi!",
            ["there", "he", "l", "o", "e", "w", "!"],
            False,
            id="not-ok",
        ),
    ],
)
def test_string_darts(target, words, expected):
    assert string_darts(target, words) is expected


@pytest.mark.parametrize(
    "input,output",
    [
        pytest.param(
            [[1, 21], [-10, -4], [-20, -1], [20, 30]], [[-20, -1], [1, 30]], id="test-1"
        ),
        pytest.param(
            [[1, 5], [2, 7], [6, 15], [7, 12], [3, 4]], [[1, 15]], id="test-2"
        ),
    ],
)
def test_merge_intervals(input, output):
    assert merge_intervals(input) == output
