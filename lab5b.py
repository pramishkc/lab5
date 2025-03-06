#!/usr/bin/env python3

def append_file_string(file_name, string_of_lines):
    """Appends the given string to the file."""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)  # Append the string to the file

def write_file_list(file_name, list_of_lines):
    """Writes a list of lines to a file, each item as a new line."""
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')  # Write each list item as a new line

def read_file_list(file_name):
    """Reads the contents of a file and returns them as a list of lines."""
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]  # Strip newline characters from each line

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Copies content from one file to another and adds line numbers."""
    with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
        for line_num, line in enumerate(f_read, start=1):
            f_write.write(f"{line_num}:{line}")  # Prefix each line with its line number

def read_file_string(file_name):
    """Reads the contents of a file and returns it as a string."""
    with open(file_name, 'r') as f:
        return f.read()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    # Append string to file1
    append_file_string(file1, string1)
    print(read_file_string(file1))

    # Write list to file2
    write_file_list(file2, list1)
    print(read_file_string(file2))

    # Read file2 as list and print
    file2_lines = read_file_list(file2)
    print(file2_lines)

    # Copy file2 to file3 with line numbers
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

