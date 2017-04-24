L = int(input())
N = int(input())

for _ in range(N):
    W, H = map(int, input().strip().split(' '))
    if W < L or H < L:
        print('UPLOAD ANOTHER')
    if W >= L and H >= L:
        if W == H:
            print("ACCEPTED")
        else:
            print("CROP IT")
