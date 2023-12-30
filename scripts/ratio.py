import re

models = []

# Open the file in read mode
with open('output.txt', 'r') as file:
    # Read all lines and store them in the 'modules' variable
    # Use strip() to remove any leading/trailing whitespace (including newlines)
    models = [line.strip() for line in file.readlines()]

# # Regular expression pattern to match various version formats (vX, vX.X, vX-X, vX.X.X, etc.)
# pattern = r'[vV]\d+'

# Define the regular expression pattern
pattern = r'\b(small|tiny|large|base)\b'

# Counter for models with versions
models_with_versions = 0

# Iterate over the models and count those with versions
for model in models:
    if re.search(pattern, model):
        models_with_versions += 1


print(f"Total models: {len(models)}")
print(f"Total models with versions: {models_with_versions}")

# Calculate the ratio of models with versions to total models

import matplotlib.pyplot as plt

ratio = models_with_versions / len(models)

labels = ['Models with versions', 'Models without versions']
values = [models_with_versions, len(models) - models_with_versions]

# Plot the pie chart
plt.pie(values, labels=labels, autopct='%.2f%%')
plt.title('Ratio of models with versions to total models')

# export the plot to a file
plt.savefig('ratio.png')

plt.clf()
plt.cla()
plt.close()

# Plot the bar chart
plt.bar(labels, values)
plt.title('Ratio of models with versions to total models')

# export the plot to a file
plt.savefig('ratio_bar.png')


