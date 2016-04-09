# status: testado com exemplos da prova

if __name__ == '__main__':
    students = int(input().strip())
    scores = [int(s) for s in input().strip().split(' ')]

    score_frequencies = {}

    for score in scores:
        if not score in score_frequencies.keys():
            score_frequencies[score] = 1
            pass
        score_frequencies[score] += 1

    print(sorted([x for x in score_frequencies.keys() if score_frequencies[x] == max(score_frequencies.values())])[-1])
