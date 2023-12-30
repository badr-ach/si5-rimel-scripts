import re

import requests
from bs4 import BeautifulSoup

models = set()

for i in range(1,14900) :
  print("Iteration: ", i)

  url = f"hhttps://huggingface.co/models?pipeline_tag={feature_tag}&p={i}&sort=trending"

  response = requests.get(url)

  soup = BeautifulSoup(response.content.decode('utf8'))

  for model in soup.find_all('article'): 

    model_name = model.find('a').attrs['href'][1:]

    models.add(model_name)
  
  with open("./data/__bulk__.txt", "w") as file:
    for element in models:
      file.write(element + "\n")
  

print(models)