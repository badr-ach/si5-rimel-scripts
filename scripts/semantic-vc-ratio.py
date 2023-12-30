import os
import re
import matplotlib.pyplot as plt

# Define the semantic versioning regex pattern
version_regex = r"[vV]\d[.-]?\d?[.-]?\d?"

# Initialize counters
file_count = 0
version_count = 0

# Initialize a dictionary to store the version counts by file name
version_counts_by_file = {}
models_countn_by_file = {}

# Iterate through the files in the directory
for filename in os.listdir('./data'):
    if filename != "__bulk__.txt" and filename.endswith(".txt"):
        file_count += 1
        version_counts_by_file[filename] = 0
        models_countn_by_file[filename] = 0

        # Open the file and iterate through each line
        with open(os.path.join('./data', filename), 'r') as file:
            for line in file:
                # Check if the line contains a semantic versioning string
                models_countn_by_file[filename] += 1
                if re.search(version_regex, line):
                    version_count += 1
                    version_counts_by_file[filename] += 1

# Global version adoption ratio
number_of_models = sum([models_countn_by_file[key] for key in models_countn_by_file.keys()])
number_of_models_with_versions = sum([version_counts_by_file[key] for key in version_counts_by_file.keys()])

plt.pie([number_of_models_with_versions, number_of_models - number_of_models_with_versions], labels=['Models with versions', 'Models without versions'], autopct='%.2f%%')
plt.title('Ratio of models with versions to total models')
plt.savefig('global-ratio.png')

plt.clf()
plt.cla()
plt.close()

# Reorder the dictionary by value count (descending)
models_countn_by_file = dict(sorted(models_countn_by_file.items(), key=lambda item: item[1], reverse=True))
# Reorder by order of keys in the models_countn_by_file dictionary
version_counts_by_file = {key: version_counts_by_file[key] for key in models_countn_by_file.keys()}

# Calculate the number of subplots needed (one for each file)
num_files = len(version_counts_by_file)

# Calculate the number of rows needed
num_rows = num_files // 6
if num_files % 6:
    num_rows += 1

print(f'Number of rows: {num_rows}')
print(f"Number of files: {num_files}, {file_count}")

# Create a figure
fig = plt.figure(figsize=(15, num_rows*2.5))

# Iterate over the dictionary and create a pie chart for each file
for i, (filename, version_count) in enumerate(version_counts_by_file.items()):
    # Calculate the row and column indices
    row = i // 6
    col = i % 6

    # Create a subplot
    ax = plt.subplot2grid((num_rows, 6), (row, col))

    # Calculate the number of models in the file
    num_models = models_countn_by_file[filename]
    
    # Calculate the number of models without versions
    num_models_without_versions = num_models - version_count

    # Create a pie chart
    ax.pie([version_count, num_models_without_versions], labels=['Semantically\n Versioned', 'Not Semantically\n Versioned'], autopct='%.2f%%', textprops={'fontsize': 6}, labeldistance=1.2)
    ax.set_title(filename.replace('.txt', ''), fontsize=8)


# Set the font size for labels and title
plt.rcParams.update({'font.size': 6})

# Display the figure
plt.tight_layout()
plt.savefig('version_ratios_by_file_pie.png')

plt.clf()
plt.cla()
plt.close()




import numpy as np

# Create a colormap and select 42 distinct colors from it
colors = plt.cm.nipy_spectral(np.linspace(0, 1, 42))

# Create a new figure with a smaller size
plt.figure(figsize=(10, 5))

# Iterate over the dictionary and plot each point with a different color
for i, (filename, version_count) in enumerate(version_counts_by_file.items()):
    # Calculate the number of models in the file
    num_models = models_countn_by_file[filename]
    
    # Calculate the percentage of semantic versioning adoption
    versioning_adoption = version_count / num_models * 100

    # Plot the point with a different color
    plt.scatter(num_models, versioning_adoption, color=colors[i], label=filename)

# Set the labels for the x and y axes
plt.xlabel('Number of models in the file')
plt.ylabel('Percentage of semantic versioning adoption')

# Display a legend under the plot area
legend = plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', fontsize='small', ncol=3)

# Set the title of the legend
legend.set_title("Models Category Name in (In Descending Count)")

# Save the figure with a smaller size
plt.savefig('version_ratios_by_file_scatter.png', bbox_inches='tight')

