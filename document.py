from abc import ABC, abstractmethod

class Document(ABC):
    """
    Classe abstraite représentant un document.
    Cette classe sert de base pour tous les documents
    qui seront stockés dans la bibliothèque.
    """

    @abstractmethod
    def afficher_details(self):
        """
        Méthode abstraite pour afficher les détails du document.
        Cette méthode doit être implémentée par la class livre.
        Elle retourne une chaîne de caractères contenant
        les informations pertinentes sur le document.
        """
        pass

