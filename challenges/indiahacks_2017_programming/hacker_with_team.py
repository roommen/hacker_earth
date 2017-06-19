N, Q = map(int, input().split(' '))
S = [int(s) for s in input().split(' ')]

for _ in range(Q):
    inp = [int(q) for q in input().split(' ')]
    O = inp[0]
    if O == 1:
        # print("S is", S)
        l, r, K = inp[1], inp[2], inp[3]
        skills = 0
        for members in range(l-1, r):
            # print("range", S[(members-K):(members+1)])
            sum_ = sum(s for s in S[(members-K):(members+1)])
            skills += sum_
        print(skills)
    if O == 2:
        i, X = inp[1], inp[2]
        S[i-1] = X
        # print(S)


