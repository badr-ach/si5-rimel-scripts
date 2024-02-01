### Introduction :
Ce répertoire facilite la reproduction des expériences que nous avons menées et présentées dans notre livre.

### Contenu :
Ce repertoire contient les dossiers suivant :
1. **data** : Les données des modèles extraites de Hugging Face à l'aide du web scraping.
3. **outputs** : Les données générées par les scripts d'analyse des données initiales pour obtenir les résultats des expériences.
2. **image-results** : Les résultats obtenus lors de l'exécution des scripts d'expériences, sous forme d'images.

### Utilisation :

**1. Installation du Python :**

Assurez-vous que Python est installé sur votre système. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis [le site officiel de Python](https://www.python.org/). La version recommandée est la 3.8.

**2. Installation des libraries :**

Exécutez le script install-requirements.sh situé dans le répertoire principal pour installer les bibliothèques nécessaires.
```
./install-requirements.sh
```
Ce script vérifie l'état d'installation des bibliothèques  `bs4` , `requests`, `matplotlib`, `numpy`,  `WordCloud` , `Circlify`, `seaborn`, `networkx` en utilisant  `pip`, les installant s'ils ne sont pas déjà présents.

**3. Execution du code :**

Pour le code nous avons choisit un format Jupyter Notebook utilisant le fichier `notebook.ipynb`  pour bénéficier d'une documentation claire du code.
