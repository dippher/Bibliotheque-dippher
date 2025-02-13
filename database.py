import sqlite3

class Database:
    """
    Cette classe encapsule toutes les opérations liées à la base de données SQLite,
    y compris la connexion, la création de tables, et les opérations CRUD
    (Create, Read, Update, Delete) pour les livres.
    """

    def __init__(self, db_name='bibliotheque.db'):
        """
        Initialise la connexion à la base de données.

        :param db_name: Le nom du fichier de la base de données SQLite
        :type db_name: str
        """
        self.connexion = sqlite3.connect(db_name)
        self.curseur = self.connexion.cursor()
        self.creer_table()

    def creer_table(self):
        """
        Crée la table des livres si elle n'existe pas déjà.

        Cette méthode est appelée lors de l'initialisation de la base de données
        pour s'assurer que la structure nécessaire est en place.
        """
        self.curseur.execute('''CREATE TABLE IF NOT EXISTS livres
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                titre TEXT, auteur TEXT, annee INTEGER, genre TEXT)''')
        self.connexion.commit()

    def ajouter_livre(self, livre):
        """
        Ajoute un nouveau livre à la base de données.

        :param livre: Le livre à ajouter
        :type livre: Livre
        :return: L'ID du livre nouvellement ajouté
        :rtype: int
        """
        self.curseur.execute("INSERT INTO livres (titre, auteur, annee, genre) VALUES (?, ?, ?, ?)",
                            (livre.titre, livre.auteur, livre.annee, livre.genre))
        self.connexion.commit()
        return self.curseur.lastrowid

    def modifier_livre(self, livre):
        """
        Modifie un livre existant dans la base de données.
        """
        self.curseur.execute("UPDATE livres SET titre = ?, auteur = ?, annee = ?, genre = ? WHERE id = ?",
                            (livre.titre, livre.auteur, livre.annee, livre.genre, livre.id))
        self.connexion.commit()

    def supprimer_livre(self, id_livre):
        """
        Supprime un livre de la base de données.
            -paramètre id_livre: L'ID du livre à supprimer, de type int
        """
        self.curseur.execute("DELETE FROM livres WHERE id = ?", (id_livre,))
        self.connexion.commit()

    def obtenir_tous_les_livres(self):
        """
        Récupère tous les livres de la base de données.
            -return: Une liste de tuples contenant les données de chaque livre
        """
        self.curseur.execute("SELECT * FROM livres")
        return self.curseur.fetchall()

    def fermer_connexion(self):
        """
        Fermeture de la connexion à la base de données.
        """
        self.connexion.close()

