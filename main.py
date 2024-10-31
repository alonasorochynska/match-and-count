def calculate(lst):
    result = 0

    list_of_word_dicts = []

    for k in lst:
        new_dict = {}
        for m in k:
            if m not in new_dict:
                new_dict[m] = 1
            else:
                new_dict[m] += 1
        list_of_word_dicts.append(new_dict)

    print("list_of_word_dicts: ", list_of_word_dicts)
    print("")

    for i, w in enumerate(lst):
        word_current = lst.pop(i)
        print("word_current: ", word_current)

        word_dict = {}
        for j in word_current:
            if j not in word_dict:
                word_dict[j] = 1
            else:
                word_dict[j] += 1

        print("word_dict: ", word_dict)

        for n in list_of_word_dicts:
            print("n:         ", n)
            print("word_dict: ", word_dict)  # check if w_d in n
            for p in word_dict:
                if p in n:
                    print("p:        ", p)
                else:
                    print("ERROR")
            print("")

        lst.insert(i, w)
        print("")


# test1 = ["boom", "mobile", "bac", "bcaac", "dghbjalcf", "bac", "cab", "babacab"]
test1 = ["boom", "mobile", "bom"]
print(calculate(test1))
