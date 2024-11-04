def calculate(lst: list) -> str:
    result_number = 0
    result_words = []

    # list_of_word_dicts - list with all words transformed to dict
    # where keys are letters and values are numbers of letter occurrence in word
    list_of_word_dicts = []

    # count letters in each word in given list in dict format
    # and add result to list_of_word_dicts
    for k in lst:
        new_dict = {}
        for m in k:
            if m not in new_dict:
                new_dict[m] = 1
            else:
                new_dict[m] += 1
        list_of_word_dicts.append(new_dict)

    # create copy of list with dicts not to destroy future iteration
    temp_list_of_dicts = list_of_word_dicts.copy()

    # extract each word (dict with letters) from list with dicts
    # and check matches of this word with rest of words
    for i, w in enumerate(list_of_word_dicts):
        # word_current - a letter combination to compare through list of words
        word_current = temp_list_of_dicts.pop(i)

        # can_add_word_result - list with comparison result
        can_add_word_result = []

        # check if word_current is in other words
        for n in temp_list_of_dicts:
            # n - each word in dict list

            check_match = ""
            for p in word_current:
                if p in n and n.get(p) >= word_current.get(p):
                    # p - each letter in word_current
                    check_match += p
                else:
                    check_match = ""
                    break
            can_add_word_result.append(check_match)

        # add word and 1 occurrence to results if match found
        if any(elem for elem in can_add_word_result):
            result_number += 1
            result_words.append(lst[i])

        # add dict with letters (word) back to list with dicts
        temp_list_of_dicts.insert(i, w)

    return f"Words found: {result_number} ({", ".join(result_words)})"


test1 = ["bac", "bcamac", "bacm", "cab", "bcaac"]
# test1 = ["boom", "mobile", "bac", "bcaac", "dghbjalcf", "bac", "cab", "babacab"]
# test1 = ["boom", "moobile", "omb"]
print(calculate(test1))
