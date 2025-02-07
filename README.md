# Documentation des Commandes

Avant toute chose il faut avoir python, pytest, coverage, docker dans son environnement.
Cette documentation explique les différentes commandes utilisées pour gérer la couverture de code, exécuter des tests, et utiliser Docker.

## 1. `coverage report -m`
### Description
Cette commande permet d'afficher un rapport de couverture de code dans la console. La couverture de code est une mesure de combien de lignes du code sont couvertes par des tests.

```bash
coverage report -m
```

## 2. `coverage run -m pytest`
### Description
Cette commande exécute les tests avec pytest tout en collectant des données de couverture de code grâce à coverage. Le -m indique à Python d'exécuter le module pytest.

```bash
coverage run -m pytest
```

## 3. `coverage html`
### Description
Cette commande génère un rapport de couverture sous forme de fichiers HTML. Elle crée un répertoire htmlcov contenant des fichiers HTML permettant de visualiser la couverture de code dans un navigateur.

```bash
coverage html
```

## 4. `docker build -t fizzbuzz .`
### Description
Cette commande construit une image Docker à partir d'un Dockerfile situé dans le répertoire actuel. Le -t permet de spécifier un nom pour l'image.

```bash
docker build -t fizzbuzz .
```

## 5. `docker run fizzbuzz`
### Description
Cette commande permet d'exécuter un conteneur à partir de l'image Docker (ici, l'image fizzbuzz).

```bash
docker run fizzbuzz
```

## 6. `pytest test_fizzbuzz.py`
### Description
Cette commande exécute les tests dans le fichier test_fizzbuzz.py en utilisant pytest.

```bash
pytest test_fizzbuzz.py
```

## 7. `python fizzbuzz.py`
### Description
Cette commande exécute le fichier Python fizzbuzz.py.

```bash
python fizzbuzz.py
```
