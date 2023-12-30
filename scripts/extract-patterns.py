import re
import collections

# Read the file and tokenize the model names
with open('./data/text-generation.txt', 'r') as file:
    models = [line.split('/')[1].strip() for line in file if '/' in line]

# models with versions
models = [model for model in models if '-' or '.' in model]

# model names
models_names = [model.split('-')[0].split('.')[0] for model in models]

# models names with multiple versions
multi_versions_models_names = [name_part for name_part, count in collections.Counter(models_names).items() if count > 1]

# models with multiple versions
multi_versions_models = [model for model in models if model.split('-')[0].split('.')[0] in multi_versions_models_names]

multi_versions_models_dict = {}

for model in multi_versions_models:
    model_name = model.split('-')[0].split('.')[0]
    version = "-".join(model.split('-')[1:]) if model.split('-')[0] in multi_versions_models_names else ".".join(model.split('.')[1:]) 
    version = re.sub(r'-?[vV]\d\.?\d?\.?\d?', '', version) 
    version = re.split(r'-', version) 
    version = [re.split(r'\.', version) if re.search(r'\d\.\d',version) is None else [version] for version in version]
    version = [[version for version in versions if version != ''] for versions in version]
    version = [token for version in version for token in version]
    version = [token for token in version if not token.isdigit()]
    version = [token for token in version if len(token) > 1]
    for token in version:
        if model_name in multi_versions_models_dict:
            existing_tokens = multi_versions_models_dict[model_name]
            if token not in existing_tokens:
                multi_versions_models_dict[model_name].append(token)
        else:
            multi_versions_models_dict[model_name] = [token]

# # versions of models with multiple versions
# multi_versions_models_versions = ["-".join(model.split('-')[1:]) if model.split('-')[0] in multi_versions_models_names 
#                                   else ".".join(model.split('.')[1:]) for model in multi_versions_models]
# # remove semantic versioning
# multi_versions_models_versions = [re.sub(r'-?[vV]\d\.?\d?\.?\d?', '', version) for version in multi_versions_models_versions]

# # Tokenize the version part using "-" and "." as delimiters
# multi_versions_models_versions = [re.split(r'-', version) for version in multi_versions_models_versions]
# multi_versions_models_versions = [re.split(r'\.', version) if re.search(r'\d\.\d',version) is None else [version] for version in multi_versions_models_versions for version in version ]

# # Remove empty strings
# multi_versions_models_versions = [[version for version in versions if version != ''] for versions in multi_versions_models_versions]

# # Extract all the tokens
# tokens = [token for version in multi_versions_models_versions for token in version]

# # Remove tokens that are numbers
# tokens = [token for token in tokens if not token.isdigit()]
            
tokens = [token for model, versions in multi_versions_models_dict.items() for token in versions]

# Count the occurrence of individual tokens 
token_counts = collections.Counter(tokens)

# Find the top tokens 
top_tokens = token_counts.most_common(100)

# Print the top tokens 
print(top_tokens)


# Impossible due to the number of combinations
# # Create a dictionary to store the occurrences of token lists
# token_list_counts = {}

# # Iterate over the values of multi_versions_models_dict
# longest_list = max(multi_versions_models_dict.values(), key=len)

# for versions in multi_versions_models_dict.values():
#     # Generate all possible sublists of the versions list
#     print(len(versions))
#     if len(versions) < 10:
#         for r in range(1, len(versions) + 1):
#             for combination in combinations(versions, r):
#                 # Convert the combination to a tuple to use it as a dictionary key
#                 token_list = list(combination)
#                 token_list_tuple = tuple(token_list)
                
#                 # Increment the count for the token list in the token_list_counts dictionary
#                 if token_list_tuple in token_list_counts:
#                     token_list_counts[token_list_tuple] += 1
#                 else:
#                     token_list_counts[token_list_tuple] = 1

# # Print the token list counts
# print(token_list_counts)
