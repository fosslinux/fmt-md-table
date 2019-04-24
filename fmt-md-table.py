#!/usr/bin/env python3
import fileinput
import sys

def parse_input():
    try:
        table = sys.stdin.readlines()
    except:
        print("some stdin error occured!")
        sys.exit(1)
    return table

def format_input(table):
    for index, row in enumerate(table):
        row = row.rstrip()
        if not row:
            # deletes the actual table index
            del table[index]
            continue
        new_row = []
        # slice to remove first and last indexes
        for column in row.split('|')[1:-1]:
            new_row.append(column)
        # assign our new row to the table
        table[index] = new_row
    return table

def get_column_length(table):
    columns_num = len(table[0])
    column_length = [0 for __ in range(columns_num)]
    for row in table:
        if len(row) != columns_num:
            print("rows have different number of columns!", file=sys.stderr)
            print(line)
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
                    table[table_index][column_index] += pad_char
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
    column_length = get_column_length(table)
    table = pad_table(table, column_length)
    print_table(table)

if __name__ == "__main__":
    main()
