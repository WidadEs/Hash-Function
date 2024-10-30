# Custom Hash Function
## Description
### Ce code implémente une fonction de hachage personnalisée en Python. Cette fonction, custom_hash_function, calcule une valeur de hachage pour une chaîne de caractères donnée. Elle utilise un nombre premier (31) pour créer une distribution plus uniforme des valeurs de hachage. Chaque caractère est pris en compte en fonction de son code ASCII et de sa position dans la chaîne, ce qui rend la fonction sensible à la casse et à l'ordre des caractères.

### Ce code inclut des détails sur chaque étape de calcul et ajoute des pauses pour ralentir l'exécution, permettant d’observer le processus étape par étape.

## Fonctionnement de la fonction de hachage
### La fonction custom_hash_function prend une chaîne en entrée et utilise un algorithme de hachage basé sur les étapes suivantes :

### 1-Initialisation d'une variable hash_value à 0.
### 2-Boucle sur chaque caractère de la chaîne en prenant en compte :
### 3-La valeur ASCII du caractère (ord(char)).
### 4-Un nombre premier multiplicatif (31).
### 5-L'index du caractère pour pondérer sa contribution.
### 6-Les étapes de calcul pour chaque caractère sont affichées pour permettre de suivre l'évolution de la valeur de hachage.
### 7-Une pause (time.sleep(0.5)) ralentit volontairement l'exécution pour une meilleure visibilité du processus.
### 8-Retourne la valeur de hachage finale pour la chaîne donnée.
