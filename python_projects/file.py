import re


def read_write_file():
    """
    write a file and read words in revered order
    """

    my_file = open('testing.txt', 'w')
    my_file.write('Hello this is me 2')
    my_file.close()

    read_my_file = open('testing.txt', 'r')

    text = read_my_file.read()
    text_list = text.split()
    text_list.reverse()
    read_my_file.close()
    print text_list


def read_file_substring_snake():
    """
    write a program which only read lines which have snake as substring

    """
    my_file = open('testing.txt', 'w')
    my_file.write('Hello this is snake 2 blah blah blah snake\n this is me \n this is new line with snake')
    my_file.close()

    read_my_file = open('testing.txt', 'r')

    text = read_my_file.readlines()
    print [i for i in text if 'snake' in i]


def file_exercise_3():
    """
    Write a program that reads a text file and produces an output file
    which is a copy of the file, except the first five
    columns of each line contain a four digit line number,
    followed by a space. Start numbering the first line in the
    output file at 1. Ensure that every line number is formatted to
    the same width in the output file. Use one of your Python programs as test
    data for this exercise:
    your output should be a printed and numbered listing of the Python program.

    """
    # read a text file
    file_handler = open('my_file.txt', 'r')
    number = range(10)
    new_string = []

    while True:
        text_line = file_handler.readline()
        if len(text_line) == 0:
            break

        new_text = text_line

        for i, v in enumerate(new_text):
            if i in number:
                continue
            new_string.append(v)
        new_list = ''.join(map(str, new_string))

        # write out put file
        output = open('output.txt', 'w')
        output.write(new_list)
        output.close()

    with open('output.txt', 'r') as result:
        for i, v in enumerate(result):
            print i+1, v

read_write_file()
read_file_substring_snake()
file_exercise_3()
