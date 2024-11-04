from main import calculate_matches


def test_calculate_case_with_matches():
    lst = ["cat", "tac", "act", "dog", "god"]
    assert calculate_matches(lst) == "Words found: 5 (cat, tac, act, dog, god)"


def test_calculate_case_without_matches():
    lst = ["hello", "world", "python"]
    assert calculate_matches(lst) == "Words found: 0 ()"


def test_calculate_empty_list():
    lst = []
    assert calculate_matches(lst) == "Words found: 0 ()"


def test_calculate_single_word():
    lst = ["solo"]
    assert calculate_matches(lst) == "Words found: 0 ()"


def test_calculate_repeating_characters():
    lst = ["a", "aa", "aaa"]
    assert calculate_matches(lst) == "Words found: 2 (a, aa)"


def test_calculate_duplicates():
    lst = ["abc", "bca", "abc"]
    assert calculate_matches(lst) == "Words found: 3 (abc, bca, abc)"


def test_calculate_anagram_groups():
    lst = ["bat", "tab", "rat", "tar"]
    assert calculate_matches(lst) == "Words found: 4 (bat, tab, rat, tar)"


def test_calculate_partial_overlap():
    lst = ["bat", "tab", "table"]
    assert calculate_matches(lst) == "Words found: 2 (bat, tab)"

