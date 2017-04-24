if __name__ == '__main__':
    N = int(input().strip())
    prod = 1
    for x in input().strip().split(' '):
        prod *= int(x)

    print(prod % 1000000007)
