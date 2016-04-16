# status: testado com exemplos da prova

if __name__ == '__main__':
    pontuations = sorted([int(x) for x in input().strip().split(' ')], reverse=True)
    print(pontuations[1])
