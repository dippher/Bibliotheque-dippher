from document import Document

class Livre(Document):
    """
    Classe représentant un livre.

    Cette classe hérite de la classe abstraite Document et implémente
    ses méthodes abstraites. Elle représente un livre avec ses attributs
    spécifiques tels que l'ID, le titre, l'auteur, l'année de publication et le genre.
    """

    def __init__(self, titre, auteur, annee, genre, id=None):
        """
        Initialisation d'un nouveau livre.
            -paramètre titre: Le titre du livre, de type int
            -paramètre auteur: L'auteur du livre, de type int
            -paramètre annee: L'année de publication du livre, de type int
            -paramètre genre: Le genre litéraire du livre, de type str
            -paramètre id: L'identifiant unique du livre, de type int
        """
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre

    def afficher_details(self):
        """
        Afficher les details du livre.
        Cette méthode implémente la méthode abstraite de la classe Document.
        Elle retourne une chaîne formatée contenant toutes les informations du livre.
            -return: Une chaîne de caractères décrivant le livre, son tye est str
        """
        return f"ID: {self.id}, {self.titre} par {self.auteur} ({self.annee}) - {self.genre}"

