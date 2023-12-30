import re

import requests
from bs4 import BeautifulSoup

print("Scrapping model tags...");

pipeline_tags = [];
url = f"https://huggingface.co/models"
response = requests.get(url)
soup = BeautifulSoup(response.content.decode('utf8'))

for model in soup.find_all('a', class_='tag tag-white'):
  tag = model.attrs['href'][1:].split('=')[1]
  pipeline_tags.append(tag)

print("Model tags scrapped successfully, Total tags: ", len(pipeline_tags))

for model_tag in pipeline_tags:
  print("Scrapping models for tag: ", model_tag)

  url = f"https://huggingface.co/models?pipeline_tag={model_tag}&sort=trending"
  response = requests.get(url)
  soup = BeautifulSoup(response.content.decode('utf8'))
  models_count = soup.find('div', class_='ml-3 w-16 font-normal text-gray-400').text
  models_counted = 0;

  with open(model_tag+".txt", "w") as file:
    for model in soup.find_all('article'): 
      model_name = model.find('a').attrs['href'][1:]
      file.write(model_name + "\n")
      models_counted += 1

  index = 1

  while models_counted < int(models_count.replace(',', '').replace(' ', '').replace('.', ' ')):
    url = f"https://huggingface.co/models?pipeline_tag={model_tag}&p={index}&sort=trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode('utf8'))

    with open(model_tag+".txt", "a") as file:
      for model in soup.find_all('article'): 
        model_name = model.find('a').attrs['href'][1:]
        file.write(model_name + "\n")
        models_counted += 1

    index += 1