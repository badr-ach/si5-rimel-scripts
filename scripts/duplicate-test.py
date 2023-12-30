import os

directory = 'data'
exclude_file = '__bulk__.txt'
modules_names_entries = set()
files_count = 0

for filename in os.listdir(directory):
    if filename != exclude_file:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            files_count += 1
            print(f'Checking {filename}...')
            for line in file:
                if line in modules_names_entries:
                    # Do something with the repeated line
                    # For example, you can add it to a list or print it
                    print(f'Repeated line in {filename}: {line}')
                else:
                    modules_names_entries.add(line)

print(f'Number of files checked: {files_count}')
print(f'Number of lines checked: {len(modules_names_entries)}')
