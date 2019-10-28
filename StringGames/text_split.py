txt = "ala ma kota ala ma ala iterator kota"


def split_and_count(txt):
    dict = {}

    for word in txt.split(" "):
        dict[word] = dict.get(word, 0) + 1

    sorted_data = dict.values()

    print(sorted_data)
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted(( key, value) for (value, key) in dict.items()))


print(split_and_count(txt))