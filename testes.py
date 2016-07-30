from os import listdir, path
import sys
import subprocess


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_tests_results(question):
    main_folder = question
    script = '{0}.py'.format(question)

    tests = listdir(main_folder)
    right_answers = 0
    total_answers = 0

    for test_folder in tests:
        test_folder_name = '{0}/{1}'.format(main_folder, test_folder)
        tests_cases = [case for case in listdir(test_folder_name)]
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

    return right_answers, total_answers

if __name__ == '__main__':
    is_successful = True
    obis = [f for f in listdir('.') if path.isdir(f) and ('obi' in f)]
    obis.sort()
    for obi in obis:
        print(obi.upper())
        levels = listdir(obi)
        for level in levels:
            print(' {0}'.format(level))
            level = '{0}/{1}'.format(obi, level)
            stages = listdir(level)
            for stage in stages:
                print('  {0}'.format(stage))
                stage = '{0}/{1}'.format(level, stage)
                questions = [f for f in listdir(stage) if f.endswith('.py')]
                for question in questions:
                    name = question
                    print('   {0} '.format(name), end='')
                    question = '{0}/{1}'.format(stage, question)
                    folder = '{0}/{1}'.format(stage, path.splitext(name)[0])
                    if path.isdir(folder):
                        right_answers, total_answers = get_tests_results(folder)
                        if right_answers < total_answers:
                            is_successful = False
                        color = Colors.GREEN if right_answers == total_answers else Colors.FAIL
                        print('   {1}/{2}'.format(name,right_answers, total_answers), end='')

                    print('')
    if not is_successful:
        exit(1)
    exit(0)
