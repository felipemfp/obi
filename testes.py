from os import listdir, path
import sys, subprocess


def get_tests_results(question):
    main_folder = question
    script = "{0}.py".format(question)

    tests = [test for test in listdir(main_folder)]

    for test_folder in tests:

        test_folder_name = "{0}/{1}".format(main_folder, test_folder)
        tests_cases = [case for case in listdir(test_folder_name)]
        tests_results = []

        for index in range(int(len(tests_cases) / 2)):
            case_input_name = "{0}/{1}{2}".format(test_folder_name, "in",index + 1)
            case_output_name = "{0}/{1}{2}".format(test_folder_name, "out",index + 1)
            input_file = open(case_input_name)
            proc = subprocess.Popen(['python', script], stdin=input_file, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = proc.communicate()[0].decode('utf-8').strip()
            output_file = open(case_output_name).read().strip()
            tests_results.append('.' if result == output_file else 'F')
            print('.' if result == output_file else 'F', end='')
            print(end='')


        # print('Teste', "%2s" % test_folder, ''.join(tests_results))

if __name__ == "__main__":
    obis = [f for f in listdir('.') if path.isdir(f) and ("obi" in f)]

    for obi in obis:
        levels = [f for f in listdir(obi)]
        print(levels)
        for level in levels:
            level = "{0}/{1}".format(obi, level)
            stages = [f for f in listdir(level)]
            for stage in stages:
                stage = "{0}/{1}".format(level, stage)
                questions = [f for f in listdir(stage) if f.endswith("py")]
                for question in questions:
                    name = question
                    question = "{0}/{1}".format(stage, question)
                    folder = "{0}/{1}".format(stage, path.splitext(name)[0])

                    if path.isdir(folder):
                        # print("Testando questão", name, end='\n')
                        get_tests_results(folder)

                print(questions)
            print(stages)

    print('\n'.join(obis))

    # get_tests_results("obi2012/programacao-1/fase-1/vice")
