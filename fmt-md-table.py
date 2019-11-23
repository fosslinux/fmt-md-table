#!/usr/bin/env python3
import fileinput
import sys

# TODO: make this cleaner
from not_list_exception import NotListException

def parse_input():
    table = sys.stdin.readlines()
    return table

def check_is_list(var):
    if not type(var) is list:
        raise NotListException

def format_input(table):
    check_is_list(table)
    for index, row in enumerate(table):
        row = row.rstrip()
        if not row:
            continue
            # later empty rows are stripped
        # slice to remove first and last indexes
        # and assign split row to table
        table[index] = row.split('|')[1:-1]
    return table

def strip_empty_rows(table):
    index = 0
    while index < len(table):
        if not table[index]:
            del table[index]
        else:
            index += 1
    return table

def get_column_length(table):
    columns_num = len(table[0])
    column_length = [0 for __ in range(columns_num)]
    for row in table:
        if len(row) != columns_num:
            print("rows have different number of columns!", file=sys.stderr)
            print(row)
            sys.exit(1)
        for index, column in enumerate(row):
            if len(column) > column_length[index]:
                column_length[index] = len(column)
    return column_length

def pad_table(table, column_length):
    for row_index, row in enumerate(table):
        for column_index, column in enumerate(row):
            if column_length[column_index] > len(column):
                padding = column_length[column_index] - len(column)
                # if its the second row in the table, 
                # its meant to have dashes insetad of spaces
                # pad dashes as a result
                if row_index == 1:
                    pad_char = "-"
                else:
                    pad_char = " "
                for __ in range(padding):
                    table[row_index][column_index] += pad_char
    return table

def print_table(table):
    for row in table:
        print("|", end='')
        for col in row:
            print(col + "|", end='')
        # newline for EOL
        print()

def main():
    table = parse_input()
    table = format_input(table)
    table = strip_empty_rows(table)
    column_length = get_column_length(table)
    table = pad_table(table, column_length)
    print_table(table)

if __name__ == "__main__":
    main()
