Gestionnaire de Bibliothèque

Etudiant: L2022GLSI0102

Description
Ce projet est une application de gestion de bibliothèque personnelle développée en Python avec une interface graphique utilisant Tkinter. L'application permet aux utilisateurs de gérer une collection de livres en offrant des fonctionnalités d'ajout, de modification, de suppression, de recherche et de tri.

Fonctionnalités

1. **Ajouter un livre** : Permet d'ajouter un nouveau livre à la bibliothèque en spécifiant le titre, l'auteur, l'année de publication et le genre.

2. Modifier un livre : Permet de modifier les informations d'un livre existant.

3. Supprimer un livre : Permet de retirer un livre de la bibliothèque.

4. Rechercher des livres : Permet de rechercher des livres selon un critère (titre ou auteur).

5. Trier les livres : Permet de trier la liste des livres par ID(option par default), titre ou auteur.

6. Affichage de la liste des livres : Affiche tous les livres de la bibliothèque dans un tableau.

Structure du projet

Le projet est composé de plusieurs fichiers Python :

- interface_bibliotheque.py : Contient la classe principale 'InterfaceBibliotheque' qui gère l'interface graphique.
- bibliotheque.py : Contient la classe 'Bibliotheque' qui gère la logique de la collection de livres.
- livre.py : Définit la classe 'Livre' représentant un livre individuel.
- document.py : Contient la classe abstraite 'Document' dont hérite la classe 'Livre'.
- recherchable.py : Définit l'interface 'Recherchable' implémentée par la classe 'Bibliotheque'.
- database.py : Gère les opérations de base de données pour stocker et récupérer les informations des livres.

Comment utiliser l'application

1. Lancer l'application : Exécutez le fichier 'interface_bibliotheque.py'.

2. Ajouter un livre :
   - Remplissez les champs Titre, Auteur, Année et Genre dans le formulaire à gauche.
   - Cliquez sur le bouton "Ajouter/Modifier".

3. Modifier un livre :
   - Sélectionnez un livre dans la liste.
   - Les informations du livre s'afficheront dans le formulaire.
   - Modifiez les champs souhaités.
   - Cliquez sur le bouton "Ajouter/Modifier".

4. Supprimer un livre :
   - Sélectionnez un livre dans la liste.
   - Cliquez sur le bouton "Supprimer le livre sélectionné".

5. Rechercher des livres :
   - Entrez un terme de recherche dans la barre de recherche.
   - Cliquez sur le bouton "Rechercher".

6. Trier les livres :
   - Cliquez sur les en-têtes de colonne dans la liste des livres pour trier par ID, Titre ou Auteur.
   - Utilisez les boutons "Trier par" pour trier par Titre ou Auteur.

Détails techniques

- L'application utilise SQLite pour stocker les données des livres.
- La base de données est automatiquement crée et gérée par l'application.
- L'interface graphique est créée avec Tkinter, une bibliothèque standard de Python pour les interfaces graphiques.

Prérequis

- Python 3.x
- Tkinter (généralement inclus dans l'installation standard de Python)
- SQLite3 (inclus dans la bibliothèque standard de Python)
