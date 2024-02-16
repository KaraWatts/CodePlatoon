def count_up(num):
    if num == 0:
        return 0
    count = count_up(num-1) + 1
    print(count)
    return count


def count_down(num):
    if num == 0:
        print(0)
        return
    print(num)
    count_down(num-1)


count_up(5)
count_down(5)