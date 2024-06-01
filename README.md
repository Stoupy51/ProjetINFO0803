
## Prérequis :
- Python (si vous voulez pas lancer les commandes docker à la main)
- Docker

# Serveurs
- Notre base de données est faite à partir d'une image `MySQL` modifiée pour ajouter nos identifiants et exécuter notre `init.sql` (cf [803_database.dockerfile](https://github.com/Stoupy51/ProjetINFO0803/blob/main/803_database.dockerfile))
- Notre API Web est basée sur `Python` et `Flask`, on copie le code source et on lance l'installation des dépendances puis on expose le port 5000 (cf [803_web_api.dockerfile](https://github.com/Stoupy51/ProjetINFO0803/blob/main/803_web_api.dockerfile))
- Notre facade Web est aussi basée sur `Python` et `Flask`, on copie de la même manière le code source puis on expose le port 80 (cf [803_web_front.dockerfile](https://github.com/Stoupy51/ProjetINFO0803/blob/main/803_web_front.dockerfile))

Voici une illustration de la structure de nos conteneurs :<br>
![Structures des conteneurs](https://raw.githubusercontent.com/Stoupy51/ProjetINFO0803/main/img/803-Virtu.png)

# Docker compose
Notre `docker-compose.yml` permet de lancer les 3 conteneurs dans un ordre d'exécution précis et de les lier entre eux.<br>
La base de données se lance en première, puis l'API Web et enfin la facade Web.<br>
Afin de déterminer si la base de données est prête à recevoir des requêtes, on utilise l'attribut `healthcheck` de Docker.<br>
Puis, dans les dépendances des serveurs, on attend que la condition `service_healthy` soit validée.<br>

# Tester l'application
Pour tester l'application, il suffit de se rendre sur [http://localhost/](http://localhost/)<br>
L'ajout et le filtre se font par les formulaires, et la suppression par la croix à droite de chaque élément.<br>
Pour revenir à la liste de tous les contacts, il suffit juste de filtrer avec toutes les cases de filtrage vides.<br>
Pour ajouter ou filtrer, le champ `attributs` doit être un format JSON valide !<br>

# Comment le faire fonctionner ?
## Avec python
1. Cloner le projet
2. Se placer dans le dossier du projet
3. Lancer le fichier python `build.py` (ex: `python build.py`)

## Sans Python
1. Cloner le projet
2. Se placer dans le dossier du projet
3. Lancer les commandes suivantes :
```bash
docker build -t 803_database -f 803_database.dockerfile .
docker build -t 803_web_api -f 803_web_api.dockerfile .
docker build -t 803_web_front -f 803_web_front.dockerfile .
docker-compose up --force-recreate
```

## Le plus automatique possible (avec python)
1. Télécharger le fichier python [Projet803_COLLIGNON_Alexandre_GARRAT_Axelle.py](https://github.com/Stoupy51/ProjetINFO0803/blob/main/Projet803_COLLIGNON_Alexandre_GARRAT_Axelle.py)
2. Exécuter le fichier python.

