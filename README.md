# Flutter-Login-Python-API

## Description

Ce repository contient une application FLutter basique avec une page de connexion et un écran d'affichage du profil.
La connexion est gérée par une API en Python qui s'occupe de hasher les mots de passe.


## Fonctionnalités

- Authentification des utilisateurs via une API.

- Hash des mots de passe avec SHA-256 côté backend avec un salt.

- Création et récupération de Tokens d'authentification avec la librairie pyjwt et flutter_secure_storage.

- Affichage du profil de l'utilisateur après la connexion.


## Prérequis

- Flutter SDK installé sur votre machine.

- Python installé sur votre machine avec les librairies suivantes: 
    - pyjwt
    - flask
    - flask-swagger-ui

- Avoir une machine pour lancer l'API et pour lancer l'application Flutter.


## Installation


### Étape 1 : Cloner le repository

Clonez le repository contenant l'API et l'application et effectuez les commandes suivantes:
```bash
git clone https://github.com/YannickBOYER/Flutter-Login-Python-API.git
cd api
pip install pyjwt flask flask-swagger-ui
cd ../login_app 
flutter pub get
```

### Étape 2 : Lancer les applications

#### Lancer l'API

Dans le dossier de l'API, exécutez :

```py login.py```

L'API sera accessible sur `http://localhost:5000` ou `http://10.0.2.2:5000` depuis un simulateur Android.

#### Lancer l'application Flutter

Dans le dossier de l'application Flutter, lancez :

```flutter run```

### Étape 3 : Tester l'application

Connectez vous avec le compte suivant sur l'application:

- **Administrateur**
    
    - Email : `admin@example.com`
    - Mot de passe : `adminpass`

### Plus d'informations

- L'application est configurée pour utiliser le debugger Windows.
- Si vous souhaitez utiliser un simulateur Android, utilisez l'adresse `http://10.0.2.2:5000` pour accéder à l'API locale dans le fichier login_app\lib\services\auth_service.dart: ```final String apiUrl = 'http://localhost:5000';```