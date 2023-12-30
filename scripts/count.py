import os

def count_lines_in_directory(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                total_lines += len(lines)
    return total_lines

directory = './data'
total_lines = count_lines_in_directory(directory)
print(f'Total lines: {total_lines}')
