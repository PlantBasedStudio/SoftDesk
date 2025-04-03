
## Test de l'API avec Postman

1. **Authentification**

    - Créer un utilisateur (POST):
    ```
    http://localhost:8000/api/register/
    ```
    Body:
    ```json
    {
        "username": "testuser",
        "email": "test@example.com", 
        "password": "password123",
        "first_name": "Test",
        "last_name": "User",
        "age": 25,
        "can_be_contacted": true,
        "can_data_be_shared": false
    }
    ```

    - Obtenir un token (POST):
    ```
    http://localhost:8000/token/
    ```
    Body:
    ```json
    {
        "username": "testuser",
        "password": "password123"
    }
    ```

    - Pour toutes les autres requêtes, ajoutez l'en-tête d'autorisation:
    ```
    Authorization: Bearer <votre_token_jwt>
    ```

2. **Gestion des Projets**

    - Créer un projet (POST):
    ```
    http://localhost:8000/projects/
    ```
    Body:
    ```json
    {
        "title": "Mon premier projet",
        "description": "Description du projet",
        "type": "back-end"
    }
    ```

    - Lister les projets (GET):
    ```
    http://localhost:8000/projects/
    ```

    - Détails d'un projet (GET):
    ```
    http://localhost:8000/projects/1/
    ```

    - Mettre à jour un projet (PUT):
    ```
    http://localhost:8000/projects/1/
    ```
    Body:
    ```json
    {
        "title": "Projet mis à jour",
        "description": "Nouvelle description",
        "type": "back-end"
    }
    ```

    - Supprimer un projet (DELETE):
    ```
    http://localhost:8000/projects/1/
    ```

3. **Gestion des Contributeurs**

    - Ajouter un contributeur (POST):
    ```
    http://localhost:8000/projects/1/contributors/
    ```
    Body:
    ```json
    {
        "user_id": 2,
        "permission": "contributor"
    }
    ```

    - Lister les contributeurs (GET):
    ```
    http://localhost:8000/projects/1/contributors/
    ```

4. **Gestion des Issues**

    - Créer une issue (POST):
    ```
    http://localhost:8000/projects/1/issues/
    ```
    Body:
    ```json
    {
        "title": "Bug à corriger",
        "description": "Description du bug",
        "priority": "high",
        "tag": "bug",
        "status": "to_do",
        "assignee_id": 2
    }
    ```

    - Lister les issues (GET):
    ```
    http://localhost:8000/projects/1/issues/
    ```

5. **Gestion des Commentaires**

    - Ajouter un commentaire (POST):
    ```
    http://localhost:8000/projects/1/issues/1/comments/
    ```
    Body:
    ```json
    {
        "description": "Mon commentaire sur ce bug"
    }
    ```

