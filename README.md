
# Serveurs
- Notre base de données est faite à partir d'une image `MySQL` modifiée pour ajouter nos identifiants et exécuter notre `init.sql` (cf [803_database.dockerfile](https://github.com/Stoupy51/ProjetINFO0803/blob/main/803_database.dockerfile))
- Notre API Web est basée sur `Python` et `Flask`, on copie le code source et on lance l'installation des dépendances puis on expose le port 5000 (cf [803_web_api.dockerfile](https://github.com/Stoupy51/ProjetINFO0803/blob/main/803_web_api.dockerfile))
- Notre facade Web est aussi basée sur `Python` et `Flask`, on copie de la même manière le code source puis on expose le port 80 (cf [803_web_front.dockerfile](https://github.com/Stoupy51/ProjetINFO0803/blob/main/803_web_front.dockerfile))

Voici une illustration de la structure de nos serveurs :<br>
![Structures des serveurs](https://raw.githubusercontent.com/Stoupy51/ProjetINFO0803/main/img/803-Virtu.png)


# Comment le faire fonctionner ?
1. Cloner le projet
2. Se placer dans le dossier du projet
3. Lancer le fichier python `build.py` (ex: `python build.py`)

