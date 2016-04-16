# status: testado com exemplos da prova

if __name__ == '__main__':
    char = input()
    all_words = input().split(' ')

    words = [word for word in all_words if char in word]

    print("{0:.1f}".format(len(words)/len(all_words) * 100))
