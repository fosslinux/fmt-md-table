#!/usr/bin/env python3
import fileinput
import sys

def parse_input():
    try:
        sys.argv[1]
        table = open(sys.argv[1], 'r').readlines()
    except IndexError:
        try:
            table = sys.stdin.readlines()
        except:
            print("some stdin error occured!")
            sys.exit(1)
    except:
        print("some parsing error occured!")
        sys.exit(1)
    return table

def format_input(table):
    for index in range(len(table)):
        table[index] = table[index].rstrip()
        if not table[index]:
            del table[index]
        line = table[index]
        table[index] = []
        for column in line.split('|'):
            table[index].append(column)
        del table[index][0]
        del table[index][-1]
    return table

def get_column_length(table):
    columns_num = len(table[0])
    column_length = [0 for __ in range(columns_num)]
    for line in table:
        if len(line) != columns_num:
            print("invalid syntax!")
            print(line)
            sys.exit(1)
        for index, column in enumerate(line):
            if len(column) > column_length[index]:
                column_length[index] = len(column)
    return column_length

def pad_table(table, column_length):
    for table_index, line in enumerate(table):
        for column_index, column in enumerate(line):
            if column_length[column_index] > len(column):
                padding = column_length[column_index] - len(column)
                for __ in range(padding):
                    table[table_index][column_index] += ' '
    return table

def print_table(table):
    for table_index in range(len(table)):
        print("|", end='')
        for column_index in range(len(table[table_index])):
            print(f"{table[table_index][column_index]}|", end='')
        print()

def main():
    table = parse_input()
    table = format_input(table)
    column_length = get_column_length(table)
    table = pad_table(table, column_length)
    print_table(table)

if __name__ == "__main__":
    main()
