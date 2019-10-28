list = [2, 5, 7, 9, 8, 6, 4,]

def bublesort(list):

    for i in list:

        for j in list:
            if i > j:
                list[j] = i
    return list


print(bublesort(list))