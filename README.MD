# SoftDesk API



---


**SoftDesk API** 

**SoftDesk API** 

---


- **Python** : version 3.8 ou supérieure / Python 3.8 or higher
- **Git** : pour cloner le projet / to clone the project
- **Pip** : pour installer les dépendances / to install dependencies
- **Virtualenv** : recommandé pour isoler l'environnement / recommended for environment isolation

---

# Installation

#### **1. Clonez le dépôt / Clone the repository**

```
git clone https://github.com/PlantBasedStudio/SoftDesk.git
cd softdesk_api
```

#### **2. Créez et activez un environnement virtuel / Create and activate a virtual environment**

1. Lancer l'environnement / create a virtual environment

```
pip install pipenv
pipenv install
pipenv shell

```

ou/or 

```
pip install poetry
poetry install
poetry shell

```


2. Installez les dépendances / Install dependencies

```
pip install -r requirements.txt
```

Configurez la base de données / Configure the database


```
python manage.py migrate
```

1. Lancez le serveur de développement / Run the development server
```
python manage.py runserver
```

Accédez à l'application sur http://127.0.0.1:8000.


#### Comment tester / How to try
