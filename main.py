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
    project_name = input('input name for project: ')
    directory = askdirectory()
    os.mkdir(directory + '/' + project_name)

    os.mkdir(directory + '/' + project_name + '/www')
    os.mkdir(directory + '/' + project_name + '/www' + '/src')
    gulp_file = open(directory + '/' + project_name + '/www' + '/src' + '/gulpfile.js', 'w+')
    gulp_file.write('const gulpfile = require(\'gulp\');\n' +
                    'const sass = require(\'gulp-sass\')(require(\'sass\'));\n' +
                    'const del = require(\'del\');\n' +
                    'const gulp = require("gulp");\n' +
                    'const concat = require(\'gulp-concat\');\n' +
                    '\n' +
                    'gulpfile.task(\'clean\', function(cb) {\n' +
                    '    del([\'dist/*\']);\n' +
                    '    cb();\n' +
                    '})\n' +
                    '\n' +
                    'gulpfile.task(\'sass\', function(cb) {\n' +
                    '    gulpfile.src(\'./src/styles/**/*.scss\')\n' +
                    '        .pipe(sass().on(\'error\', sass.logError))\n' +
                    '        .pipe(concat(\'index.css\'))\n' +
                    '        .pipe(gulpfile.dest(\'dist\'));\n' +
                    '    cb();\n' +
                    '})\n' +
                    '\n' +
                    'gulpfile.task(\'copy:html\', function (cb) {\n' +
                    '    gulp.src(\'./src/views/*.html\')\n' +
                    '        .pipe(gulp.dest(\'./dist/views\'))\n' +
                    '    cb()\n' +
                    '})\n' +
                    '\n' +
                    'gulpfile.task(\'copy:js\', function (cb) {\n' +
                    '    gulp.src(\'./src/scripts/*.js\')\n' +
                    '        .pipe(concat(\'index.js\'))\n' +
                    '        .pipe(gulp.dest(\'./dist\'))\n' +
                    '    cb()\n' +
                    '})\n' +
                    '\n' +
                    '//.gif\n' +
                    'gulpfile.task(\'copy:gif\', function (cb) {\n' +
                    '    gulp.src(\'./src/images/*.gif\')\n' +
                    '        .pipe(gulp.dest(\'./dist\'))\n' +
                    '    cb()\n' +
                    '})\n' +
                    '\n' +
                    'gulpfile.task(\'watch\', function () {\n' +
                    '\n' +
                    '    gulpfile.watch([\'./src/**/*.scss\', \'./src/scripts/**/*.js\', \'./src/components/*.html\',' +
                    ' \'./src/images/*.gif\'],\n' +
                    '        gulpfile.series([\'clean\', \'sass\', \'copy:html\', \'copy:js\', \'copy:gif\']));\n' +
                    '\n' +
                    '})\n' +
                    '\n' +
                    'gulpfile.task(\'default\', gulpfile.series([\'clean\', \'sass\', \'copy:html\', \'copy:js\',' +
                    ' \'copy:gif\']))')
    gulp_file.close()

    package_json = open(directory + '/' + project_name + '/www' + '/src' + '/package.json', 'w+')
    package_json.write('{\n' +
                       '  "name": "Project_1",\n' +
                       '  "version": "1.0.0",\n' +
                       '  "main": "index.js",\n' +
                       '  "license": "MIT",\n' +
                       '  "dependencies": {\n' +
                       '    "del": "^6.0.0",\n' +
                       '    "gulp": "^4.0.2",\n' +
                       '    "gulp-concat": "^2.6.1",\n' +
                       '    "gulp-sass": "^5.0.0",\n' +
                       '    "sass": "^1.45.0"\n' +
                       '  },\n' +
                       '  "scripts": {\n' +
                       '    "cmd": "gulp",\n' +
                       '    "build": "yarn cmd default",\n' +
                       '    "watch": "yarn cmd watch",\n' +
                       '    "start": "node server/server"\n' +
                       '  },\n' +
                       '   "devDependencies": {\n' +
                       '        "@types/jest": "^27.0.3",\n' +
                       '        "jest": "^27.4.5"\n' +
                       '   }'
                       '}\n')
    package_json.close()

    os.mkdir(directory + '/' + project_name + '/www' + '/src' + '/scripts')
    js_file = open(directory + '/' + project_name + '/www' + '/src' + '/scripts' + '/script.js', 'w+')
    js_file.close()

    os.mkdir(directory + '/' + project_name + '/www' + '/src' + '/views')
    html_file = open(directory + '/' + project_name + '/www' + '/src' + '/views' + '/index.html', 'w+')
    html_file.write('<!doctype html>\n' +
                    '<html lang="en">\n' +
                    '<head>\n' +
                    '    <meta charset="UTF-8">\n' +
                    '    <meta name="viewport"\n' +
                    '          content="width=device-width, user-scalable=no, initial-scale=1.0,' +
                    ' maximum-scale=1.0, minimum-scale=1.0">\n' +
                    '    <meta http-equiv="X-UA-Compatible" content="ie=edge">\n' +
                    '    <title>Document</title>\n' +
                    '</head>\n' +
                    '<body>\n' +
                    '\n' +
                    '\n <script src="../scripts/main.js"></script>'
                    '</body>\n' +
                    '</html>')
    html_file.close()

    os.mkdir(directory + '/' + project_name + '/www' + '/src' + '/styles')
    css_file = open(directory + '/' + project_name + '/www' + '/src' + '/styles' + '/styles.scss', 'w+')
    css_file.close()

    os.mkdir(directory + '/' + project_name + '/www' + '/src' + '/images')
    os.mkdir(directory + '/' + project_name + '/server')
    package_json_server = open(directory + '/' + project_name + '/server' + '/package.json', 'w+')
    package_json_server.write('{\n' +
                              '  "name": "server",\n' +
                              '  "version": "1.0.0",\n' +
                              '  "scripts": {\n' +
                              '    "dev": "nodemon src/server.js",\n' +
                              '    "start": "node src/server.js"\n' +
                              '  },\n' +
                              '  "dependencies": {\n' +
                              '    "cors": "^2.8.5",\n' +
                              '    "express": "^4.17.2"\n' +
                              '  },\n' +
                              '  "devDependencies": {\n' +
                              '    "nodemon": "^2.0.15"\n' +
                              '  }\n' +
                              '}')
    package_json_server.close()

    os.mkdir(directory + '/' + project_name + '/server' + '/src')
    server_file = open(directory + '/' + project_name + '/server' + '/src' + '/server.js', 'w+')
    server_file.close()

    os.mkdir(directory + '/' + project_name + '/server' + '/src' + '/modules')


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

    sorted_functions = {}

    for item in function_names:
        for inner_item in function_texts:
            if inner_item.startswith('function ' + item):
                sorted_functions[item] = inner_item

    swaps = 1
    delete_array = []

    while swaps > 0:
        for key in sorted_functions:
            for item in function_names:
                if sorted_functions[key].find(item) > -1 and key != item:
                    swaps = swaps + 1
                    sorted_functions[key] = sorted_functions[key] + '\n\n' + sorted_functions[item]
                    delete_array.append(item)
            swaps = 0

    [sorted_functions.pop(key, ' ') for key in delete_array]

    for key in sorted_functions:
        new_js = open(js_directory + '/' + key + '.js', 'w+')
        new_js.write(sorted_functions[key] + "\n\nmodule.exports = " + key)
        new_js.close()

        new_test = open(tests_directory + '/' + key + '.test.js', 'w+')
        new_test.write("const " + key + " = require('../" + key + ".js'); \n\n"
                       + 'describe("Tests for ' + key + ' function", function () {\n\n})')
        new_test.close()

    file.close()
    os.remove(filename)

    print('success')
    print('===================================================================================')
    another_one = input('make test directory for another HW? Y/N: ')
    another_one.upper()

    if another_one == 'Y':
        create_test_files()


def create_test_directory(path):
    os.mkdir(path + '/__tests__')
    return path + '/__tests__'


main_cycle()
