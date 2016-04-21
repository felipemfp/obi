# status: testado com exemplos da prova

if __name__ == '__main__':
    notes = sorted([float(x) for x in input().strip().split(' ')])

    del notes[len(notes) - 1]
    del notes[0]

    print('%.1f' % sum(notes))
