if __name__ == '__main__':
    K = int(input())
    disliked_word = list()
    for _ in range(K):
        disliked_word.append(str(input()))

    S = int(input())
    sentence = [s for s in input().strip().split(' ') if s not in disliked_word]

    acronym = ""
    for s in sentence:
        acronym += str(s[0]).upper() + "."

    print(acronym[:-1])
