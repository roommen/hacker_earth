S = str(input())

len_ = len(S)
mid = len_ // 2
S_mid = S[:mid]
rev_mid = S_mid[::-1]

if len_ % 2 == 0:
    print('YES' if S_mid + rev_mid == S else 'NO')
else:
    print('YES' if S_mid + S[mid] + rev_mid == S else 'NO')
