#!/usr/bin/env python3
import pytest

from tasks import string_darts, merge_intervals


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
