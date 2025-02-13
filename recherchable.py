from abc import ABC, abstractmethod

class Recherchable(ABC):
    """
    Interface pour la recherche.
    Cette interface est chargée de la recherche,
    """

    @abstractmethod
    def rechercher(self, critere):
        """
        Méthode abstraite pour faire une recherche selon un critère donné.
            -paramètre critere: Le critère de recherche de type str
            -return: Une liste d'objets correspondant au critère de recherche, de type list
        """
        pass

