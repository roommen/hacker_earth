l, r, k = map(int, input().strip().split(' '))

i, count = l, 0
while i <= r:
    if i % k == 0:
        count += 1
    i += 1

print(count)
