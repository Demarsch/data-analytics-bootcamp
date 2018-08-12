from os import path
import sys

def get_input_file_locations(file_name: str) -> list:
    '''
    Return possible locations where specific file will be looked for.
    :param str file_name: name of input file
    :return: list of possible locations
    :rtype: list
    '''
    return [
        file_name,
        path.join('..', file_name),
        path.join('Input', file_name),
        path.join('..', 'Input', file_name)
    ]

def get_input_file_path(file_name: str) -> str:
    '''
    Return the path to the specified file name (if one exists).
    :param str file_name: name of the file to look for
    :return: path to the file or empty string if file not found
    :rtype: str
    '''
    for file_path in get_input_file_locations(file_name):
        if path.exists(file_path):
            return file_path
    return ''

def print_separator(file=sys.stdout):
    '''
    Print a horizontal line having a standard console window width (80 symbols).
    :param file: file to print separator to. Defaults to sys.stdout
    '''
    print(''.rjust(80, '-'), file=file)