import math


def print_primes(N_):
    i = 2
    if N_ > i:
        print("2", end=" ")
    while i <= N_:
        j, prime = 2, 1
        while j <= math.sqrt(i)+1:
            if i % j == 0:
                prime = 0
                break
            j += 1
        if prime == 1:
            print(i, end=" ")
        i += 1


if __name__ == '__main__':
    N = int(input())
    print_primes(N)
