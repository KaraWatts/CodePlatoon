# O(1)
def lookup_by_index(lst, index):
    return lst[index]


# find_by_index takes a list and a target value
# and returns the first index matching that value
# if it exists. Otherwise it returns -1.
# O(N)
def find_by_index(lst, target):
    counter = 0
    for index in range(len(lst)):
        counter += 1
        if lst[index] == target:
            print(counter)
            return index
    else:
        print(counter)
        return -1


def find_by_index_naive(lst, target):
    counter = 0
    answer = -1
    for index in range(len(lst)):
        counter += 1
        if lst[index] == target:
            answer = index

    print(counter)
    return answer


# test it out
lst = list(range(1000))
find_by_index(lst, 999)
find_by_index_naive(lst, 999)
# print(find_by_index(lst, 142))
# print(find_by_index(lst, 999))
