if __name__ == '__main__':
    bin_num = str(input())
    one_split = len(max(bin_num.split("1")))
    zero_split = len(max(bin_num.split("0")))

    if (one_split or zero_split) >= 6:
        print('Sorry, sorry!')
    else:
        print('Good luck!')
