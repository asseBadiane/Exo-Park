# Récupération du Backend et du Frontend

## Backend

### Clonage du référentiel (Git)

1. Ouvrez votre terminal.

2. Utilisez la commande suivante pour cloner le référentiel du backend :
 ```
git clone git@github.com:asseBadiane/Exo-Park.git
```

3. Accédez au répertoire nouvellement cloné :
 ```
cd Exo-Park
```
4. Créer un environnement virtuelle et l'activer (sous lunix)
```
  python3 -m venv env
  source env/bin/activate
```
5. Installez les dépendances du projet (le cas échéant) en exécutant
 ```
 pip install -r requirements.txt
```
6. Tu dois créer un fichier .env et le configurer avec les donnés suivant:
   ```
   DB_NAME="database_name"
   DB_USER="user_name"
   DB_PASSWORD="password"
   DB_HOST="localhost"
   DB_PORT="5432"
   ```
6. Tu peux lancer le backend avec:
   ```
   python manage.py runserver
   ```

 Vous êtes prêt à travailler sur le backend.
   

## Frontend

### Clonage du référentiel (Git)

1. Accédez dans le répertoire frontend :
 ```
   cd frontend
 ```
2. Installez les dépendances du projet (le cas échéant) en exécutant :
```
npm install
```
4. Vous êtes maintenant prêt à travailler sur le frontend.
