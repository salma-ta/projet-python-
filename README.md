##              L’entreprise MeetingPro : application de gestion de la réservation des salles


## réalisé par : 
Narjis Nejjar           narjis.nejjar@uha.fr 
Salma Taouil            salma.taouil@uha.fr


## contexte du projet :
Meetinpro est une application développée en Python qui sert à la gestion des réservations des salles de coworking avec un interphace graphique .

L'application permet de :
-Gérer les clients (ajout, consultation)
-Gérer différents types de salles (Standard, Conférence, Informatique)
-Effectuer des réservations avec gestion des conflits
-Consulter les disponibilités et réservations
-Sauvegarder les données en JSON


les types des salles à gérer:
1-des salles standards : une salle de réunion classique avec une capacité d'accueil variable (1 personne
à 4 personnes).
2-des salles de conférence : une salle de réunion avec un estrade de présentation, un vidéo projecteur et
une capacité d'accueil entre 4 et 10 personnes.  
3-des salles informatiques :une salle de réunion avec un ordinateur par place. Capacité d'accueil de 1
personne à 4 personne. 


les principales fonctionnalités :
1. Ajouter un nouveau client
2. Ajouter une nouvelle salle
3. Afficher les salles réservables
4. Afficher les réservations pour un client
5. Identifier si une salle est disponible sur un créneau
6. Afficher les salles disponibles pour un créneau
7. Réserver une salle 


## structure de projet :
PROJET PYTHON/
│
├── README.md            ##description du projet
│
├──src/
│    │──models
│    │── interphace graphique     
│    │──database
│──tests/                ##tests unitaires
│   │──test              
