# Are Datascientists Embracing DevOps Principles for Model Versioning?

## Auteurs

Nous sommes quatre étudiants en dernière année à Polytech Nice-Sophia spécialisés en Architecture Logicielle (AL) :

- _Badr AL ACHKAR_

- _Nadim BEN AISSA_

- _Sourour GAZZEH_

- _Imene YAHIAOUI_

## I. Contexte

L'évolution constante des principes de DevOps vers le domaine de l'apprentissage automatique soulève la question cruciale de l'adoption de ces principes par les data scientists pour le versionnement des modèles. Cette intersection entre ingénierie logicielle et apprentissage automatique constitue une zone d'intérêt particulier, motivée par notre quête de comprendre comment ces deux domaines interconnectés convergent.

Notre motivation derrière cette étude réside dans la volonté de démystifier les pratiques actuelles du versionnement des modèles par les data scientists. Comprendre comment ces professionnels gèrent les différentes versions de leurs modèles revêt une importance capitale dans un contexte où l'apprentissage automatique s'insère de plus en plus dans des pipelines de développement logiciel.

- ### Outils de Versionnement Identifiés :

Dans cette recherche, deux outils majeurs ont capté notre attention : MLflow et Hugging Face. MLflow, au centre de l'écosystème DevOps pour le machine learning, propose une approche intégrée du cycle de vie des modèles. En parallèle, Hugging Face, en tant que plateforme publique, offre une alternative en mettant à disposition des modèles issus de grandes entreprises.


#### 1. Exploration de MLflow : 

MLflow révolutionne la gestion des modèles d'apprentissage automatique
en unifiant le processus du développement à la production. La première
phase de notre enquête se concentre sur la manière dont MLflow gère les
versions des modèles.

- **Comment MLflow stocke les modèles ? Comment sont-ils enregistrés, organisés et récupérés ?**

Pour répondre à ces questions cruciales, nous avons consulté la documentation officielle de MLflow et nous nous sommes appuyés sur les résultats validés par plusieurs articles scientifiques, dont les références sont soigneusement documentées dans notre bibliographie.

MLflow enregistre les modèles sous forme d'artefacts, utilisant divers
formats appelés "flavors", qui correspondent à différents formats
spécifiques de bibliothèques de machine learning, tels que TensorFlow,
PyTorch, Scikit-Learn. Ces modèles sont organisés dans un "registre"
structuré, chacun possédant un nom unique, des versions, des étapes de
transition (telles que développement, production, archivage) et
d'autres métadonnées.

La gestion des versions en Mlflow est automatisée, où chaque modèle
enregistré peut avoir une ou plusieurs versions. Lorsqu'un nouveau
modèle est ajouté au registre des modèles, il est enregistré en tant que
version 1. Chaque nouvel enregistrement sous le même nom incrémente
automatiquement le numéro de version.

Il est possible d'adapter manuellement cette gestion de versions à
travers l'utilisation d'alias, de tags et de descriptions :

- Les alias permettent de pointer vers une version spécifique du
  modèle, facilitant ainsi le référencement via l'URI
  models:/<model-name>@<alias>. Ils offrent une référence
  mutable et nommée à des versions spécifiques, simplifiant leur
  déploiement.

- Les tags permettent de catégoriser les modèles selon leur fonction
  ou statut.

- Les annotations et descriptions en Markdown fournissent des
  informations cruciales telles que des descriptions de version, des
  ensembles de données utilisés, etc.


Cependant, au cours de notre exploration des modèles et du processus de versionnement, nous avons constaté que MLflow est principalement adopté par des entreprises, et aucune d'entre elles ne rend publics leurs modèles, entravant ainsi notre accès à des projets et modèles versionnés pour une analyse approfondie.

#### 2. Exploration de Hugging Face :

Hugging Face est une plateforme spécialisée dans le partage et la découverte de modèles d'apprentissage automatique. Elle offre une vitrine publique où des data scientists du monde entier et des grandes entreprises importantes telles que Meta et Google. peuvent partager leurs modèles avec la communauté. Cela crée un écosystème ouvert où des modèles développés par des entreprises notables comme Facebook et Google sont accessibles à tous.

Dans le contexte de notre recherche, nous avons approfondi notre exploration pour comprendre comment les versions des modèles sont nommés et gérés sur Hugging Face. D'après la documentation officielle sur hugging face, les data scientists qui contribuent à la plateforme bénéficient d'une flexibilité significative dans le processus de nommage de leurs modèles et leurs versions, offrant ainsi une identification claire et facile de chaque modèle et sa version partagée.

Enfin, la particularité de Hugging Face réside dans sa transparence et son accessibilité. Les modèles sont généralement rendus publics, permettant à chacun de les explorer, les utiliser et les évaluer. Ainsi, après considération, nous avons opté pour Hugging Face comme plateforme principale pour notre recherche.


## II. Question général
L'objectif fondamental de notre projet de recherche est d'explorer l'adoption des principes DevOps par les data scientists pour le versionnement des modèles.

Ces réflexions nous conduiront à explorer les questions sous-jacentes suivantes :

1.  **_Est ce que les modèles publiés sur Hugging Face adoptent un
    schéma de versionnement traditionnel ou part plutôt sur le
    versionnement libre ?_**

2.  **_Le type de tâches (image-to-text, reinforcement, etc.)
    influence-t-il le schéma de versionnement ?_**

3.  **_Existe-t-il des tendances de versionnement spécifiques dans les grandes entreprises utilisant Hugging Face?_**

## III. Collecte de Données : Méthodes et Outils

Pour répondre de manière approfondie aux interrogations formulées, nous avons entrepris une exploration minutieuse du dépôt open source de Hugging Face, une riche source regroupant plus de 500 000 modèles partagés par une multitude d'utilisateurs et de grandes entreprises. Nous avons amorcé notre démarche par une analyse manuelle des modèles présents dans ce référentiel, initiant ainsi une approche qualitative essentielle pour appréhender la diversité des tâches et des méthodologies de versionnement.

Dans une volonté d'élargir notre échantillon de manière significative et de systématiser notre processus, nous avons opté pour le web scraping. Cette technique a permis la collecte efficace d'un nombre substantiel de modèles, alimentant ainsi nos différentes expériences. L'utilisation de Python, avec une focalisation sur la bibliothèque BeautifulSoup pour l'analyse HTML et requests pour les requêtes HTTP, a facilité l'extraction systématique des données nécessaires.
Cette transition stratégique de l'analyse manuelle vers l'automatisation au moyen du web scraping a grandement renforcé notre capacité à examiner un éventail plus large de modèles, établissant ainsi une base plus robuste pour nos diverses expérimentations. 

Pendant la phase de web scraping, nous avons décidé de cibler spécifiquement les modèles avec des tags associés à des catégories, représentant ainsi l'objectif du modèle avec sa catégorie. Cette approche sélective a permis d'obtenir des informations pertinentes, compte tenu du volume considérable de modèles sur Hugging Face.

Parallèlement, nous avons veillé à écarter toute redondance dans les modèles téléchargés, assurant ainsi l'intégrité de notre échantillon. En fin de compte, notre effort a abouti à la constitution d'une base de données solide, comprenant environ 230 000 modèles, qui servira de fondement pour répondre de manière approfondie aux diverses questions formulées dans le cadre de notre recherche.

## IV. Hypothèses, Expériences & Analyse des résultats

1. **_Adoption du Versionnement Traditionnel vs Versionnement Libre des
    Modèles_**

**1.1. _Hypothèse : Le versionnement des modèles ne suit pas une
approche traditionnel - (major,minor,patch)_**

L'observation des modèles sur Hugging Face suggère que la numérotation des versions des modèles ne suit pas un motif prévisible, contrairement à la structure classique de versionnement. Il semble y avoir une variation dans la manière dont les versions sont étiquetées. Cette variation dans l'étiquetage des versions suscite la question suivante : Est-ce que les modèles publiés sur Hugging Face adoptent un schéma de versionnement traditionnel ou part plutôt sur le versionnement libre ?

**1.2. _Expérience : Calcule de l'adoption du versionnement traditionnel_**

Nous avons exploité la base des modèles téléchargés grâce au web scraping, en nous focalisant exclusivement sur l'analyse du nom de l'artefact, qui renferme des informations cruciales telles que la version du modèle. Afin de discerner le versionnement sémantique au sein de ces noms, nous avons opté pour un format spécifique basé sur des motifs fréquemment rencontrés : (vX, vX.X, vX-X, vX.X.X, etc.).

Cette approche a impliqué l'utilisation d'une expression régulière (regex) bien définie, à savoir "[vV]\d[.-]?\d?[.-]?\d?", pour détecter les différents formats de versionnement. Notre objectif était de calculer le pourcentage de modèles adoptant une approche de versionnement sémantique parmi l'échantillon analysé. 

Les résultats ont été graphiquement représentés sous la forme d'un diagramme circulaire, offrant une perspective visuelle sur la prévalence des modèles avec versionnement par rapport à ceux sans versionnement apparent.


**1.3. _Résultat :_**

Le graphique ci-dessous présente les résultats de l'expérience, illustrant le pourcentage d'adoption du versionnement sémantique :

![ratio global](./images/global-ratio.png)

Cette première expérience nous a permis de confirmer notre hypothèse, avec un ratio de 79% des modèles qui ne suivent pas le versionnement traditionnel.

Cependant, il est essentiel de souligner qu'au sein de ces modèles, environ 21% (soit environ 41 000 modèles) semblent explorer des tentatives de versionnement sémantique. Ce nombre important souligne l'intérêt marqué de certains datascientists à établir une structure plus claire et compréhensible pour leurs modèles. Cette observation met en lumière la diversité des pratiques de versionnement au sein de la communauté des datascientists, reflétant peut-être des besoins spécifiques liés à la nature expérimentale de certains projets ou à des préférences individuelles.

Cette variabilité dans les schémas de versionnement souligne l'importance de la flexibilité sur les plateformes de partage de modèles, comme Hugging Face, qui permettent aux datascientists de définir leurs propres conventions. Cette flexibilité revêt une importance particulière dans le domaine de l'apprentissage automatique, caractérisé par des évolutions rapides, des expérimentations fréquentes et des besoins spécifiques liés aux différentes tâches.

2.  **_Influence de la tâche du modèle sur son versionnement_**

  **2.1. _Hypothèse :  La nature de la tâche du modèle influence la  façon avec laquelle on le versionne_**

Nous émettons l'hypothèse selon laquelle la nature de la catégorie d'un modèle influence de manière significative sa méthodologie de versionnement. Cette hypothèse suggère que des caractéristiques propres à chaque catégorie de modèle peuvent exercer une influence sur les choix de versionnement adoptés.

  **2.2. _Expériences realisées_ :**

Dans le cadre de notre étude sur l'influence de la tâche des modèles sur leur versionnement, nous avons réalisé deux étapes distinctes. Dans la première étape, nous avons cherché à identifier les types de tâches pour lesquels les modèles adoptent un versionnement sémantique. Dans la deuxième étape, nous avons exploré l'existence de patterns de versionnement libre, le cas échéant.

a. **_Etape 1 : Analyse du Versionnement des Modèles par Catégorie de Tâche_**

Dans cette phase, nous avons reproduit la méthodologie de la première expérience pour identifier les modèles adoptant des pratiques de versionnement standard, classés par catégorie. En réutilisant les différents modèles, nous les avons subdivisés en catégories, générant ainsi des graphiques en dispersion illustrant l'adoption du versionnement sémantique par catégorie de modèles. Ces graphiques tiennent compte du nombre de modèles par catégorie et du pourcentage d'adoption du versionnement sémantique, explorant ainsi les tendances et motifs récurrents dans les pratiques de versionnement. Cela met en lumière l'influence potentielle de la tâche des modèles sur ces choix.

- **_Résultat_**

Les résultats graphiques ont clairement démontré que le pourcentage d'adoption du versionnement sémantique varie considérablement d'une catégorie de modèle à une autre :

![ratio global](./images/version_ratios_by_file_scatter.png)

- **_Analyse des résultats_**

Cette observation souligne une corrélation directe entre la nature spécifique de la tâche d'un modèle et les choix de versionnement qui lui sont associés. Les différentes catégories de modèles présentent des tendances distinctes en matière de versionnement, révélant une diversité d'approches au sein de la plateforme. Notre jeu de données est constitué de 42 catégories, et selon le schéma, certaines sont plus volumineuses que d'autres. Quelques catégories massives se distinguent par un taux d'adoption du versionnement sémantique élevé, principalement "Reinforcement Learning" avec un pourcentage de 68.80% et "Automatic Speech Recognition" avec un pourcentage de 46.55%.
Ces catégories spécifiques semblent favoriser l'utilisation d'un modèle de gestion des versions sémantique.
En revanche, le reste des catégories affiche majoritairement un taux d'adoption inférieur à 20%.

En effet, le domaine du "Reinforcement Learning" se caractérise par des modèles d'apprentissage automatique qui interagissent dynamiquement avec leur environnement. Dans ce contexte, les modèles apprennent en prenant des décisions successives afin de maximiser une récompense cumulative. Cette approche d'apprentissage continu est particulièrement adaptée à des environnements complexes et dynamiques, où les modèles doivent s'ajuster constamment pour relever des défis émergents. Les modèles de "Reinforcement Learning" se distinguent par leur capacité à évoluer et à s'adapter à des situations changeantes, nécessitant ainsi des ajustements fréquents pour maintenir des performances optimales. 

D'autre part, dans le domaine de "Automatic Speech Recognition" (ASR), il s'agit d'une technologie dédiée à la reconnaissance automatique de la parole. Les modèles inclus dans cette catégorie sont spécifiquement conçus pour traiter des données audio, cherchant à interpréter et comprendre la parole humaine de manière automatisée. Les modèles ASR sont continuellement soumis à des améliorations afin d'affiner leur capacité à comprendre de manière précise les variations de la parole humaine. Ces améliorations constantes peuvent inclure des ajustements dans la compréhension des accents, la gestion des bruits de fond et l'adaptation à des langues spécifiques. La nature même des données audio implique une nécessité fréquente de mise à jour pour rester à jour avec les évolutions linguistiques et technologiques.

Ainsi, l'utilisation du versionnement sémantique dans ces deux catégories peut offrir une approche structurée pour gérer les modifications et les mises à jour fréquentes nécessaires à l'amélioration continue des modèles. Cela permet de maintenir une traçabilité transparente des évolutions successives dans ces domaines complexes et en constante évolution, facilitant la compréhension des évolutions complexes de ces modèles et offrant ainsi une gestion plus claire des changements itératifs.

b. **_Etape 2 : Exploration des schémas libres pour les catégories de modèles_**

L'objectif de cette deuxième étape est de déterminer si chaque catégorie de modèles adopte des patterns spécifiques qui lui sont propres. Pour ce faire, nous avons exclu les deux catégories "Automatic Speech Recognition" et "Reinforcement Learning", qui présentent un niveau d'adoption du versionnement sémantique important. Nous nous concentrons plutôt sur l'examen des noms de modèles dans les ensembles de données les plus importants, représentant 80% du total, en nous basant sur la loi de Pareto. Les catégories prises en compte sont ainsi : "text classification", "text generation", "text to text generation", "token classification", "text to image", et "fill-mask".

Dans cette démarche, un script a été développé pour analyser les schémas de versionnement des modèles par catégorie de tâches, en se penchant sur leurs patterns et tokens de versionnement. Ce script repose sur des choix méthodologiques délibérés visant à atteindre notre objectif.

Initialement, le script aborde la complexité inhérente aux noms de modèle, souvent constitués de plusieurs tokens séparés par des tirets ou des points.  En tenant compte du fait que les noms des artefacts comprennent à la fois le nom et la version, nous avons isolé la partie correspondant au token de version. Notre script simplifie les noms en éliminant le premier token. Notre hypothèse, formulée sur la base d'observations, postule que le premier token représente systématiquement le nom par défaut du modèle. Et dans les situations où certains tokens suivants font partie intégrante du nom du modèle, ils sont considérés comme une version. Cette approche ne présente aucune problématique majeure, car elle n'aura pas d'impact significatif sur les tendances générales des tokens de versionnement. 

De plus, un aspect crucial de notre méthodologie réside dans l'exclusion des modèles qui n'apparaissent qu'une seule fois dans l'ensemble de données. L'hypothèse sous-jacente est que les modèles uniques ont moins de chances d'avoir fait l'objet de versionnement, limitant ainsi notre capacité à comprendre l'évolution des noms de versions.

Enfin, notre script exclut spécifiquement les indicateurs numériques. Cette décision repose sur la reconnaissance que les identifiants numériques sont courants dans les pratiques de versionnement sémantique du développement logiciel. Puisque notre intérêt réside dans l'exploration de schémas de versionnement moins conventionnels et plus nuancés, les indicateurs numériques sont considérés comme moins informatifs à cette fin. L'exclusion de ces indicateurs est donc une décision stratégique visant à concentrer notre analyse sur la découverte de schémas de versionnement plus uniques et perspicaces, s'éloignant ainsi du versionnement sémantique.


- **_Résultat :_**

Les résultats montrent que chaque type de modèle a des tokens spécifiques du versionnement :

- **_Analyse des résultats_**

Les résultats suggèrent que chaque type de modèle possède des tokens spécifiques qui lui sont associés. Cependant, il est remarquable que quelques modèles partagent un token commun, tels que "base," "BERT," et "finetuned."

D'après des recherches préliminaires, l'utilisation fréquente du token "base" suggère qu'il pourrait représenter un "base model," indiquant ainsi un modèle fondamental ou de base, souvent utilisé comme point de départ pour des itérations ultérieures. Pour "BERT," acronyme de "Bidirectional Encoder Representations from Transformers," représentant un modèle de langage pré-entraîné utilisant une architecture de transformer bidirectionnelle, le terme "base" pourrait également signaler son rôle de modèle fondamental. Par ailleurs, le terme "finetuned" fait référence au processus de ré-entraînement d'un modèle linguistique pré-entraîné sur un ensemble de données spécifique à une tâche particulière, permettant au modèle de s'ajuster précisément à la spécificité de la tâche visée.

Dans le contexte de la classification de texte, d'autres tokens tels que "classification" et "classifier" sont couramment utilisés, probablement pour indiquer la nature de la tâche que le modèle est destiné à accomplir.

En ce qui concerne la génération de texte, d'autres tokens prédominants incluent "7b" et "13b" qui indiquent respectivement des modèles avec 7 milliards et 13 milliards de paramètres, soulignant la taille croissante et la complexité de ces modèles de génération de texte. "text-generation." Également, nous avons "GPTQ," qui représente une variante particulière du modèle GPT (Generative Pre-trained Transformer).

e. **_Expérience 3 :_**

Dans le cadre de notre démarche continue pour comprendre les schémas de versionnement, la troisième expérience vise à approfondir les résultats de l'expérience précédente en combinant les groupes de tokens constituant une version (2 ou 3 tokens). Cette approche nous permet d'analyser avec plus de détails les combinaisons les plus fréquemment observées, et d'évaluer si des tendances significatives se dégagent.

f. **_Résultat et analyse de l'expérience 3:_**

- **Les Groupes de Taille Deux :** L'analyse des groupes de deux tokens révèle deux types de regroupements : Catégories Conceptuelles et Séquences Numériques. Ces regroupements sont parfois combinés, suggérant que le versionnement pourrait s'opérer sur plusieurs dimensions ou aspects. Les catégories conceptuelles pourraient représenter différents types de changements ou de mises à jour, tandis que les séquences numériques pourraient indiquer des changements plus quantifiables, tels que des numéros de version ou des mises à jour incrémentielles de la taille de l'entrée, des poids, ou d'autres composants techniques.

- **Les Groupes de Taille Trois et Plus :** Ces regroupements accentuent davantage notre observation précédente, montrant des progressions sémantiques variées dans les tokens de versionnement, souvent combinées. Cette constatation suggère l'existence d'un système de versionnement plus complexe, où plusieurs aspects ou dimensions sont mis à jour simultanément.

Ces résultats, issus d'analyses approfondies, offrent un aperçu plus détaillé des schémas de versionnement. Au-delà de simples indicateurs numériques, les combinaisons de tokens révèlent des informations substantielles sur les types de changements opérés lors du versionnement, contribuant ainsi à une compréhension plus fine des pratiques de gestion des versions dans divers contextes.

**2.3. _Conclusion :_**

En conclusion, il est possible d'affirmer qu'aucun modèle de versionnement n'est unanimement adopté et accepté dans aucune catégorie. De nombreux schémas de versionnement sont détectés, mais leur occurrence est très infime pour être considérée comme une norme.


3.  **_Tendances de Versionnement dans les Grandes Entreprises_**

  3.1. **_Hypothèse : Les grandes entreprises standardise leurs manière > de versionner les modèles ML en interne_**

Nous formulons l'hypothèse que les grandes entreprises ont tendance à standardiser leur approche de versionnement pour les modèles d'apprentissage automatique en interne. Cette hypothèse suggère que, au sein de ces grandes structures, il existe probablement des pratiques et des normes établies vis-à-vis du processus de gestion des versions des modèles d'apprentissage automatique.

  3.2. **_Expérience : Analyse des modèles ceux publié par Google, > OpenAI et Meta, individuellement, et extraction des patterns > adoptée._**

Au cours de cette étude, nous avons spécifiquement sélectionné les entreprises les plus renommées du secteur. Dans cette perspective, notre recherche se concentrera exclusivement sur les artefacts de modèles publiés par Google, Facebook/Meta, et OpenAI, en tenant compte de la variabilité du nombre de modèles. Google a mis à disposition 617 artefacts, Facebook/Meta en a partagé 1879, et OpenAI en compte 32. Notre approche pour cette expérience suivra le même protocole que celui de l'expérience 2, visant à identifier les tokens les plus fréquemment utilisés.

  3.3 **_Résultat :_**

L'analyse des données obtenues a révélé ce qui suit : 

![ratio global](./images/Result3.png)

Nous observons l'identification de tokens spécifiques aux modèles tels que "medium," "large," "base," "small," ou "base." Cependant, aucune tendance claire de versionnement n'a été repérée à l'échelle globale de l'entreprise.


## V. Conclusion

En résumé, notre analyse révèle une grande diversité au sein de la communauté des data scientists en ce qui concerne l'implémentation du versionnement des modèles. Plutôt que de suivre un processus défini, il est fréquent d'observer une approche individualisée, laissant chacun libre de déterminer ses propres méthodes en fonction de ses besoins spécifiques. Cette liberté opérationnelle, bien que reflétant la nature adaptable de la science des données, entraîne souvent une non-conformité marquée aux normes établies par DevOps.
## Références

