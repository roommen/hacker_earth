N = int(input())

A = [int(a) for a in input().split(' ')]

i = 0
count_list = list()
# count_list.
count = 0
try:
    while i < N:
        if A[i] == 1:
            count += 1
            if i == (N-1):
                # print("appening this")
                count_list.append(count)
        else:
            if i != 0 and A[i-1] != 0:
                count_list.append(count)
            count = 0
        i += 1
    # print("count_list 1", count_list)
    # print("length", len(count_list), count_list)
    if len(count_list) > 1:
        max_ = max(count_list)
        print(max_ + 1)
    elif len(count_list) == 0:
        print(0)
    else:
        print(max(count_list))
except IndexError:
    # print("count_list 2", count_list)
    max_ = max(count_list)
    if len(count_list) > 1:
        max_ = max(count_list)
        print(max_ + 1)
    elif len(count_list) == 0:
        print(0)
    else:
        print(max(count_list))
