if __name__ == '__main__':
    alphabet_dict = {0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                     13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                     24: 'x', 25: 'y', 26: 'z'}

    N = int(input().strip())

    for _ in range(N):
        str_ = str(input().strip())
        len_ = len(str_)
        i = 0
        add_str = ""
        while i < len_:
            # print(add_str)
            add_str += alphabet_dict[((ord(str_[i]) - 96) + (ord(str_[-(i+1)]) - 96)) % 26]
            i += 1

        print(add_str)
