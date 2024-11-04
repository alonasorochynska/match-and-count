def calculate_matches(lst: list) -> str:
    result_number = 0
    result_words = []

    # list_of_word_dicts - list with all words transformed to dict
    # where keys are letters and values are numbers
    # of letter occurrence in word
    list_of_word_dicts = []

    # count letters in each word in given list in dict format
    # and add result to list_of_word_dicts
    for word in lst:
        new_dict = {}
        for letter in word:
            new_dict[letter] = new_dict.get(letter, 0) + 1
        list_of_word_dicts.append(new_dict)

    # create copy of list with dicts not to destroy future iteration
    temp_list_of_dicts = list_of_word_dicts.copy()

    # extract each word (dict with letters) from list with dicts
    # and check matches of this word with rest of words
    for index, word in enumerate(list_of_word_dicts):
        # word_current - a letter combination to compare through list of words
        word_current = temp_list_of_dicts.pop(index)

        # can_add_word_result - list with comparison result
        can_add_word_result = []

        # check if word_current is in other words
        for w_d_l in temp_list_of_dicts:
            # w_d_l - each word in dict list

            check_match = [
                ltr
                if ltr in w_d_l and w_d_l.get(ltr) >= word_current.get(ltr)
                else 0
                for ltr in word_current
            ]

            check_match = "" if 0 in check_match else "".join(check_match)

            can_add_word_result.append(check_match)

        # add word and 1 occurrence to results if match found
        if any(elem for elem in can_add_word_result):
            result_number += 1
            result_words.append(lst[index])

        # add dict with letters (word) back to list with dicts
        temp_list_of_dicts.insert(index, word)

    return f"Words found: {result_number} ({", ".join(result_words)})"
