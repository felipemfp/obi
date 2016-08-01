import hashlib
import pickle
import os
import sys
import subprocess
import time


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


cache = {}
hashes = []

def get_cache():
    try:
        with open('tests/results.dat', 'rb') as afile:
            if afile:
                global cache
                cache = pickle.load(afile)
    except FileNotFoundError:
        os.makedirs('tests')

def save_cache():
    ks = [k for k in cache.keys() if not k in hashes]
    for k in ks:
        del cache[k]
    afile = open('tests/results.dat', 'wb')
    pickle.dump(cache, afile)


def get_tests_results(question):
    global cache

    main_folder = question
    script = '{0}.py'.format(question)
    hasher = hashlib.md5()
    with open(script, 'rb') as f:
        hasher.update(f.read())
    hsh = hasher.digest()
    hashes.append(hsh)
    if hsh in cache:
        return cache[hsh]

    tests = os.listdir(main_folder)
    right_answers = 0
    total_answers = 0

    for test_folder in tests:
        test_folder_name = '{0}/{1}'.format(main_folder, test_folder)
        tests_cases = [case for case in os.listdir(test_folder_name)]
        for index in range(int(len(tests_cases) / 2)):
            case_input_name = '{0}/{1}{2}'.format(
                test_folder_name, 'in', index + 1)
            case_output_name = '{0}/{1}{2}'.format(
                test_folder_name, 'out', index + 1)
            input_file = open(case_input_name)
            proc = subprocess.Popen(
                ['python', script], stdin=input_file,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = proc.communicate()[0].decode('utf-8').strip()
            output_file = open(case_output_name).read().strip()

            if result == output_file:
                right_answers += 1
                sys.stdout.write('.')
            else:
                sys.stdout.write('F')
            total_answers += 1
            sys.stdout.flush()

    cache[hsh] = (right_answers, total_answers)
    return cache[hsh]

if __name__ == '__main__':
    is_successful = True
    obis = [f for f in os.listdir('.') if os.path.isdir(f) and ('obi' in f)]
    obis.sort()
    get_cache()
    for obi in obis:
        print(obi.upper())
        levels = os.listdir(obi)
        for level in levels:
            print(' {0}'.format(level))
            level = '{0}/{1}'.format(obi, level)
            stages = os.listdir(level)
            for stage in stages:
                print('  {0}'.format(stage))
                stage = '{0}/{1}'.format(level, stage)
                questions = [f for f in os.listdir(stage) if f.endswith('.py')]
                for question in questions:
                    s = time.time()
                    name = question
                    print('   {0} '.format(name), end='')
                    question = '{0}/{1}'.format(stage, question)
                    folder = '{0}/{1}'.format(stage, os.path.splitext(name)[0])
                    if os.path.isdir(folder):
                        right_answers, total_answers = get_tests_results(folder)
                        if right_answers < total_answers:
                            is_successful = False
                        color = Colors.GREEN if right_answers == total_answers else Colors.FAIL
                        print('   {1}/{2}'.format(name,right_answers, total_answers), end='')

                    print(' [{:.2f}s]'.format(time.time() - s))
    save_cache()
    if not is_successful:
        exit(1)
    exit(0)
