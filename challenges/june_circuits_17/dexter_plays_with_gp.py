T = int(input())

for _ in range(T):
    r, S, p = map(int, input().split(' '))
    N, sum_of_a, a = 1, 0, 0
    while N < p:
        if N == 1:
            a = 1
            sum_of_a += a
        else:
            multi = a * r
            mod_ = multi % p
            a = mod_
            # print("N, a", N, a)
            sum_of_a += a
            # print("sum of a", sum_of_a)

        # print("evaluating expre")
        if (sum_of_a % p) == S:
            print(N)
            break

        N += 1

        if N == p:
            print(-1)

