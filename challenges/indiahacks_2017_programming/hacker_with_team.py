N, Q = map(int, input().split(' '))
S = [int(s) for s in input().split(' ')]

for _ in range(Q):
    inp = [int(q) for q in input().split(' ')]
    O = inp[0]
    if O == 1:
        l, r, K = inp[1], inp[2], inp[3]
    if O == 2:
        i, X = inp[1], inp[2]
