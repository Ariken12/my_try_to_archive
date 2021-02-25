import random as r
from math import log2, ceil
from sys import stdout

BYTE = 256


def create_random_file(amount_bytes, filename='file.bin'):
    '''
    This function create file
    :param amount_bytes: amount of random bytes
    :param filename: file will rewrite if it already exist
    :return: nothing
    '''
    file = open(filename, 'wb')
    for i in range(amount_bytes):
        file.write(bytearray([r.randint(0, 255)]))
    file.close()


def number_into_bytes(number, size):
    output = bytearray()
    while number > 0:
        output += bytearray([number % 256])
        number //= 256
    return bytearray(size - len(output)) + output


def archive_file_by_destroy_repeating(input_filename, output_filename='output.bin', log=None):
    input_file = open(input_filename, 'rb')
    output_file = open(output_filename, 'wb')
    bytes_from_file = bytearray(input_file.read())
    index_len = ceil(log2(len(bytes_from_file)) / 8)
    indexes_of_repeatings = bytearray()
    for byte in bytes_from_file:
        pass
    #todo: make this shit


def archive_file_by_indexing(input_filename, output_filename='output.bin', log=None):
    input_file = open(input_filename, 'rb')
    output_file = open(output_filename, 'wb')
    bytes_from_file = bytearray(input_file.read())
    index_len = ceil(log2(len(bytes_from_file)) / 8)
    print('amount bytes by 1 byte:', index_len, file=log)
    for value in range(BYTE):
        print('byte:', value, 'begin', file=log)
        output_file.write(bytearray([BYTE - 1]))
        for index_of_byte in range(len(bytes_from_file)):
            if bytes_from_file[index_of_byte] == value:
                print('position:', index_of_byte, 'writed', file=log)
                output_file.write(number_into_bytes(index_of_byte, index_len))
    input_file.close()
    output_file.close()


def file_reader(filename, mode, information='npc'):
    file = open(filename, 'r' + mode)
    text = file.read()
    print('_________________________')
    if 'n' in information:
        print(filename)
    if 'p' in information:
        print(text)
    if 'c' in information:
        print(len(text))
    print('_________________________')
    file.close()


if __name__ == '__main__':
    log = open('log.txt', 'w')
    create_random_file(100000)
    archive_file_by_indexing('file.bin', log=log)
    file_reader('file.bin', 'b', 'nc')
    file_reader('output.bin', 'b', 'nc')
    # print(number_into_bytes(255))
