from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os

def main_cycle():
    algorithm_branch = input('===============================================\n' +
                             'create new project structure              :: 1\n' +
                             'create test files and directories         :: 2\n' +
                             'quit                                      :: 0\n' +
                             '===============================================\n')
    if algorithm_branch == '1':
        create_project_structure()
    elif algorithm_branch == '2':
        create_test_files()
    elif algorithm_branch == '0':
        quit()
    else:
        print('You have to use only presented options')
        main_cycle()



def create_project_structure():
    dirname = askdirectory()
    print(dirname)



def create_test_files():
    filename = askopenfilename()
    file = open(filename)
    pa = os.path.split(filename)
    js_directory = pa[0]
    tests_directory = create_test_directory(pa[0])

    function_names = []
    function_texts = ['']
    counter = 0

    for line in file:
        index = str(line).find('function')
        if index > -1:
            counter = counter + 1
            function_texts.append('')

            func_start = index + 9
            func_end = str(line).find('(') - 1
            func_name = str(line)[func_start:func_end]

            function_names.append(func_name)

            function_texts[counter] = function_texts[counter] + str(line)
        else:
            if str(line).find('//') < 0:
                function_texts[counter] = function_texts[counter] + str(line)

    func_text_counter = 0

    for item in function_names:
        for inner_item in function_texts:
            if str(inner_item).find(item) > 0:
                print(js_directory + '/' + item + '.js', 'w+')
                print(tests_directory + '/' + item + '.test.js', 'w+')

                new_js = open(js_directory + '/' + item + '.js', 'w+')
                new_test = open(tests_directory + '/' + item + '.test.js', 'w+')

                new_js.write(inner_item + "\nmodule.exports = " + item)
                new_js.close()

                new_test.write("const " + item + " = require('../" + item + ".js'); \n"
                               + 'describe("Tests for ' + item + ' function", function () {\n})')
                new_test.close()
                print(item, inner_item)
                break
            else:
                continue

    #file.close()
    #os.remove(filename)

    #print('success')
    #print('===================================================================================')
    #another_one = input('make test directory for another HW? Y/N: ')
    #another_one.upper()

    #if another_one == 'Y':
    #    create_test_files()


def create_test_directory(path):
    os.mkdir(path + '/__tests__')
    return path + '/__tests__'


#create_test_files()
main_cycle()
