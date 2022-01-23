Projet d'intéraction distribuée, 3A SRI

Concept : un Arduino uno muni d'un capteur de température, ainsi qu'un capteur virtuel de température (générant un flottant aléaoire entre 0 et 30) communiquent avec un agrégat. L'agrégat est écrit à l'aide du framework Flask, les deux capteurs font une requête POST toutes les 10 secondes des températures mesurées et autres métadonnées. Ces valeurs sont stockées par l'agrégat sous la forme d'une liste, qui les communique à un slot développé en Flask lorsque celui-ci les lui demande. Le tout est orchestré par docker-compose.

Pour lancer le projet, il suffit de disposer de docker-compose, et d'un arduino avec capteur de température. L'arduino est connecté en USB et le service qui l'utilise appelle la bibliothèque `pyserial` pour aller lire le fichier où sont écrites les données par l'Arduino.

Lancement du projet :

1- Téléverser le sketch dans l'arduino (sketch fourni, voir suite) et connecter la donnée issue du capteur sur le port A0.

2- Ouvrir le fichier `docker-compose.yaml` et aller modifier les lignes suivantes au niveau du service `capteur_reel` : `environment: - PORT_ARDUINO=/dev/ttyACM0` et `devices: - "/dev/ttyACM0"` (remplacer `/dev/ttyACM0` par le bon fichier correspondant à votre configuration) afin que le service ait accès au port Série de l'Arduino.

3- Lancement de l'orchestration : `docker-compose build` puis `docker-compose up`.

Utilisation :

Le port 5000 de la machine hôte est mappé par docker-compose au port 5000 du service slot, on peut donc s'en servir pour intéragir avec les capteurs : il suffit de taper dans un navigateur : `http://localhost:5000` pour afficher le dashboard, ou bien faire une requête GET vers `/get_data` sans aucun argument (par exemple avec le navigateur web en tapant `http://localhost:5000/get_data`) pour obtenir l'ensemble des données au format JSON.

Notes :

Au lancement de l'orchestration, il n'y a aucune donnée enregistrée. Il faut donc patienter quelques secondes afin de disposer de données. Evolution possible : ajouter un service de base de donnée pour stocker les mesures afin qu'elles soient persistantes.

Le sketch utilisé dans l'Arduino est fourni afin d'être compilé et versé vers le microcontroleur (donc à faire une seule fois) et n'est pas utilisé par docker-compose.

Capteur de température utilisé pendant le développement : TMP 36GZ.
