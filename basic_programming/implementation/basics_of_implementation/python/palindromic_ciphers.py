if __name__ == '__main__':
    T = int(input())
    alphabet_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12,
                     'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23,
                     'x':24, 'y':25, 'z':26}
    for _ in range(T):
        s = str(input())
        len_ = len(s)
        mid = len_ // 2
        palindrome = 0
        if len_ % 2 == 0:
            if s[:mid] + s[mid-1::-1] == s:
                palindrome = 1
        else:
            if s[:mid] + s[mid] + s[mid-1::-1] == s:
                palindrome = 1

        if palindrome == 1:
            print("Palindrome")
        else:
            prod = 1
            for letter in s:
                prod *= alphabet_dict[letter]
            print(prod)
