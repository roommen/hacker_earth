def factorial(N_):
    if N_ == 0:
        return 1
    return N_ * factorial(N_ - 1)


if __name__ == '__main__':
    N = int(input())
    print(factorial(N))
