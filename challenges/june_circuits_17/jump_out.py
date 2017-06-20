N = int(input())

A = [int(n) for n in input().split(' ')]

i, min_jump = 0, list()
while i < N:
    # print("i and A[i]", i, A[i])
    if i + A[i] > N:
        min_jump.append(i+1)
        # print(i+1)
        break
    i += 1

# print(min_jump)
if len(min_jump) == 0:
    print(0)
else:
    print(min(min_jump))
