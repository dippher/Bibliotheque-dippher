from recherchable import Recherchable
from livre import Livre
from database import Database

class Bibliotheque(Recherchable):
    """
    Cette classe implémente l'interface Recherchable et utilise la classe Database
    pour stocker et récupérer les informations sur les livres. Elle gère l'ensemble
    des opérations liées à la collection de livres.
    """

    def __init__(self):
        """
        Initialise une nouvelle bibliothèque.

        Crée une instance de la classe Database pour gérer les opérations de base de données.
        """
        self.db = Database()

    def ajouter_livre(self, livre):
        """
        Ajoute un livre à la bibliothèque.
            -paramètre livre: Le livre à ajouter
            -return: L'ID du livre nouvellement ajouté
        """
        return self.db.ajouter_livre(livre)

    def modifier_livre(self, livre):
        """
        Modifie un livre existant dans la bibliothèque.
            -paramètre livre: Le livre à modifier
        """
        self.db.modifier_livre(livre)

    def supprimer_livre(self, id_livre):
        """
        Supprime un livre de la bibliothèque.
        -paramètre id_livre: L'ID du livre à supprimer, de type int
        """
        self.db.supprimer_livre(id_livre)

    def obtenir_tous_les_livres(self):
        """
        Récupère tous les livres de la bibliothèque.
            -return: Liste de tous les livres
        """
        livres_data = self.db.obtenir_tous_les_livres()
        return [Livre(titre=data[1], auteur=data[2], annee=data[3], genre=data[4], id=data[0]) for data in livres_data]

    def rechercher(self, critere):
        """
        Recherche des livres selon un critère.
        Cette méthode implémente l'interface Recherchable.
            -paramètre critere: Le critère de recherche, de type str
            -return: Liste des livres correspondants
        """
        tous_les_livres = self.obtenir_tous_les_livres()
        return [livre for livre in tous_les_livres if critere.lower() in livre.titre.lower() or
                critere.lower() in livre.auteur.lower()]

    def fermer(self):
        """
        Ferme la connexion à la base de données.
        """
        self.db.fermer_connexion()

