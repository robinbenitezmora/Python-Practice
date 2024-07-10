'''
Take two names as input then remove the common characters with their respective common occurrences. For removing purpose we create a user-defined remove_match_char function with two arguments as list1 and list2 which stores list of characters of two players name respectively and return list of concatenated list(list1 + “*” flagst2) and flag value which we store in ret_list variable.After removing all the common characters, count the total no. of remaining characters then create a result list with FLAMES acronym i.e [“Friends”, “Love”, “Affection”, “Marriage”, “Enemy”, “Siblings”]. Now start removing word one by one until list does not contain only one word, using the total count which we got. the word which remains in the last, is the result.
'''

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]

    list3 = list1 + ["*"] + list2
    return [list3, False]

if __name__ == "__main__":
    p1 = input("Enter your name: ").replace(" ", "").lower()
    p2 = input("Enter your crush's name: ").replace(" ", "").lower()

    p1_list = list(p1)
    p2_list = list(p2)

    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]

    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]

    print(result[0])

