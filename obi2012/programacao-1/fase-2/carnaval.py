# status: testado com exemplos da prova

if __name__ == '__main__':
    notes = sorted([float(x) for x in input().split()])

    del notes[-1]
    del notes[0]

    print('%.1f' % sum(notes))
