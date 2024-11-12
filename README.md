# Nutriscore-Predictions

Nutriscore-Predictions est un projet visant à prédire le Nutri-Score d'un produit alimentaire basé sur ses caractéristiques nutritionnelles. Ce projet expose une API RESTful pour obtenir des prédictions de Nutri-Score via un modèle pré-entraîné. L'application est conteneurisée avec Docker et Docker Compose, permettant une installation et un déploiement simples.

## Table des Matières

- [Présentation](#présentation)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Requête de Prédiction](#requête-de-prédiction)
  - [Exemple de Réponse](#exemple-de-réponse)
- [Structure du Projet](#structure-du-projet)
- [Configuration](#configuration)
- [Dépendances](#dépendances)
- [Volumes et Sauvegarde des Données](#volumes-et-sauvegarde-des-données)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Présentation

Ce projet utilise un modèle de machine learning pré-entraîné pour prédire le Nutri-Score (A, B, C, D ou E) d'un produit alimentaire. L'API reçoit des caractéristiques nutritionnelles d'un produit en entrée et renvoie un Nutri-Score en fonction de celles-ci. 

Les fonctionnalités incluent :

- Une API REST accessible via un point de terminaison `/predict`.
- Persistance des requêtes et des résultats de prédiction dans un volume Docker pour un suivi historique des requêtes.

## Prérequis

Assurez-vous d'avoir installé les éléments suivants :

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

### Étapes d'installation

1. Clonez le dépôt dans votre environnement local :

   ```bash
   git clone https://github.com/DahliaNoir71/Nutriscore-Predictions.git
   cd Nutriscore-Predictions
2. Assurez-vous que le modèle pré-entraîné (model.pkl) est présent dans le dossier principal du projet. Si ce fichier est manquant, entraînez le modèle ou importez un modèle compatible.

3. Construisez et démarrez les conteneurs Docker en utilisant Docker Compose :
    docker-compose up --build
Une fois le processus terminé, l'API sera accessible à l'adresse http://localhost:8080.

Utilisation
Requête de Prédiction

Envoyez une requête POST au point de terminaison /predict avec les caractéristiques nutritionnelles du produit sous format JSON. Le format attendu est le suivant :
{
  "features": [1, 2, 3, 4]
}

Remarque : Les valeurs dans le tableau features doivent correspondre aux caractéristiques nutritionnelles que le modèle a été entraîné à utiliser.
Exemple de Commande cURL :
    curl -X POST -H "Content-Type: application/json" \
    -d '{"features": [1, 2, 3, 4]}' \
    http://localhost:8080/predict

Exemple de Réponse

L'API renvoie un JSON avec le Nutri-Score prédit :
{
  "prediction": "a"
}


