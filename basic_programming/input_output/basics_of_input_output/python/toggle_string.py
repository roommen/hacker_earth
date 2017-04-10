S = list(input())

toggle = ""
for s in S:
    if 65 <= ord(s) <= 90:
        toggle += chr(ord(s) + 32)
    if 97 <= ord(s) <= 122:
        toggle += chr(ord(s) - 32)

print(toggle)
