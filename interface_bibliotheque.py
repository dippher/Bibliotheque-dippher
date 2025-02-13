import tkinter as tk
from tkinter import ttk, messagebox
from bibliotheque import Bibliotheque
from livre import Livre

class InterfaceBibliotheque(tk.Tk):
    """
    Cette classe crée une fenêtre Tkinter avec tous les widgets nécessaires
    pour interagir avec la bibliothèque, y compris l'ajout, la modification,
    la suppression, la recherche, le tri et l'affichage des livres.
    """

    def __init__(self):
        """
        Initialisation de l'interface graphique.
        """
        super().__init__()

        self.bibliotheque = Bibliotheque()
        self.title("Bibliothèque dippher")
        self.geometry("1000x600")

        self.livre_selectionne = None
        self.tri_actuel = ("ID", True) # Par défaut, le tri est par ID en ordre ascendant
        self.creer_widgets()

    def creer_widgets(self):
        """
        Cette méthode configure le menu, le formulaire d'ajout/modification de livres,
        la liste des livres, la barre de recherche, les boutons de tri et les autres boutons.
        """
        # Titre principal
        ttk.Label(self, text="Gestion de livres", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # Section 1: Formulaire d'ajout/modification
        frame_form = ttk.LabelFrame(self, text="Ajouter ou Modifier livre", padding="10")
        frame_form.grid(row=1, column=0, sticky=(tk.N, tk.W, tk.E, tk.S), padx=10, pady=10)

        ttk.Label(frame_form, text="Titre:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        self.titre_entry = ttk.Entry(frame_form)
        self.titre_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(frame_form, text="Auteur:").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        self.auteur_entry = ttk.Entry(frame_form)
        self.auteur_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(frame_form, text="Année:").grid(row=2, column=0, sticky=tk.W, pady=(0, 10))
        self.annee_entry = ttk.Entry(frame_form)
        self.annee_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(frame_form, text="Genre:").grid(row=3, column=0, sticky=tk.W, pady=(0, 10))
        self.genre_entry = ttk.Entry(frame_form)
        self.genre_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Button(frame_form, text="Ajouter/Modifier", command=self.ajouter_ou_modifier_livre).grid(row=4, column=0, columnspan=2, pady=10)

        # Section 2: Liste des livres
        frame_liste = ttk.LabelFrame(self, text="Liste des livres", padding="10")
        frame_liste.grid(row=1, column=1, sticky=(tk.N, tk.W, tk.E, tk.S), padx=10, pady=10)

        # Barre de recherche et options de tri
        frame_recherche_tri = ttk.Frame(frame_liste)
        frame_recherche_tri.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        frame_recherche_tri.columnconfigure(0, weight=3)
        frame_recherche_tri.columnconfigure(1, weight=1)

        self.recherche_entry = ttk.Entry(frame_recherche_tri)
        self.recherche_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(frame_recherche_tri, text="Rechercher", command=self.rechercher_livres).grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame_recherche_tri, text="Trier par:").grid(row=0, column=2, padx=(20, 5))
        ttk.Button(frame_recherche_tri, text="Titre", command=lambda: self.trier_livres('Titre')).grid(row=0, column=3)
        ttk.Button(frame_recherche_tri, text="Auteur", command=lambda: self.trier_livres('Auteur')).grid(row=0, column=4)

        # Liste des livres
        self.tree = ttk.Treeview(frame_liste, columns=('ID', 'Titre', 'Auteur', 'Année', 'Genre'), show='headings')
        self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Tri par ID
        self.tree.heading('ID', text='ID', command=lambda: self.trier_livres('ID'))
        self.tree.heading('Titre', text='Titre', command=lambda: self.trier_livres('Titre'))
        self.tree.heading('Auteur', text='Auteur', command=lambda: self.trier_livres('Auteur'))
        self.tree.heading('Année', text='Année')
        self.tree.heading('Genre', text='Genre')

        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # Bouton de suppression
        ttk.Button(frame_liste, text="Supprimer le livre sélectionné", command=self.supprimer_livre).grid(row=3, column=0, pady=10)

        # Configuration des colonnes
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        frame_liste.columnconfigure(0, weight=1)

        # Menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Quitter", command=self.quitter)

        self.charger_livres()

    def ajouter_ou_modifier_livre(self):
        """
        Cette méthode récupère les informations du formulaire, crée un nouvel objet Livre
        ou modifie un livre existant, et l'ajoute ou la modifie dans la bibliothèque.
        Elle gère également les erreurs de saisie.
        """
        try:
            titre = self.titre_entry.get()
            auteur = self.auteur_entry.get()
            annee = int(self.annee_entry.get())
            genre = self.genre_entry.get()

            if not titre or not auteur or not genre:
                raise ValueError("Tous les champs doivent être remplis.")

            if self.livre_selectionne:
                # Modification d'un livre existant
                livre = Livre(titre, auteur, annee, genre, id=self.livre_selectionne.id)
                self.bibliotheque.modifier_livre(livre)
                messagebox.showinfo("Succès", "Le livre a été modifié avec succès.")
            else:
                # Ajouter un nouveau livre
                livre = Livre(titre, auteur, annee, genre)
                self.bibliotheque.ajouter_livre(livre)
                messagebox.showinfo("Succès", "Le livre a été ajouté avec succès.")

            self.charger_livres()
            self.effacer_champs()
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def supprimer_livre(self):
        """
        Cette méthode récupère le livre sélectionné dans la liste,
        le supprime de la bibliothèque et met à jour l'affichage.
        """
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un livre à supprimer.")
            return

        livre_id = self.tree.item(selection[0])['values'][0]
        self.bibliotheque.supprimer_livre(livre_id)
        self.charger_livres()
        self.effacer_champs()
        messagebox.showinfo("Succès", "Le livre a été supprimé avec succès.")

    def charger_livres(self):
        """
        Charge et affiche tous les livres dans la liste.
        Cette méthode efface la liste actuelle, le remplit avec tous les livres
        présents dans la bibliothèque, puis applique le tri actuel.
        """
        for i in self.tree.get_children():
            self.tree.delete(i)

        livres = self.bibliotheque.obtenir_tous_les_livres()
        
        # Tri par défaut par ID
        livres.sort(key=lambda x: x.id)

        for livre in livres:
            self.tree.insert('', 'end', values=(livre.id, livre.titre, livre.auteur, livre.annee, livre.genre))

    def rechercher_livres(self):
        """
        Recherche et affiche les livres correspondant au critère de recherche.
        """
        critere = self.recherche_entry.get()
        resultats = self.bibliotheque.rechercher(critere)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for livre in resultats:
            self.tree.insert('', 'end', values=(livre.id, livre.titre, livre.auteur, livre.annee, livre.genre))

        self.appliquer_tri()

    def trier_livres(self, colonne):
        """
        Trie les livres selon la colonne spécifiée.
            -paramètre colonne: La colonne selon laquelle trier, de type str
        """
        if self.tri_actuel[0] == colonne:
            # Inverser l'ordre si on clique sur la même colonne
            self.tri_actuel = (colonne, not self.tri_actuel[1])
        else:
            # Nouvelle colonne, tri ascendant par défaut
            self.tri_actuel = (colonne, True)

        self.appliquer_tri()

    def appliquer_tri(self):
        """
        Applique le tri actuel à la liste des livres.
        """
        colonne, ordre = self.tri_actuel
        livres = [(self.tree.set(child, colonne), child) for child in self.tree.get_children('')]
        
        # Utiliser une clé de tri numérique pour l'ID et l'Année
        if colonne in ['ID', 'Année']:
            livres.sort(key=lambda x: int(x[0]), reverse=not ordre)
        else:
            livres.sort(key=lambda x: x[0].lower(), reverse=not ordre)
        
        for index, (val, child) in enumerate(livres):
            self.tree.move(child, '', index)

    def effacer_champs(self):
        """
        Cette méthode est appelée apres l'ajout, la modificatión ou la suppression d'un livre
        pour préparer le formulaire à une nouvelle saisie.
        """
        self.titre_entry.delete(0, tk.END)
        self.auteur_entry.delete(0, tk.END)
        self.annee_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.livre_selectionne = None

    def on_select(self, event):
        """
        Cette méthode remplit le formulaire avec les données du livre sélectionné.
        """
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            livre_id, titre, auteur, annee, genre = item['values']
            self.livre_selectionne = Livre(titre, auteur, annee, genre, id=livre_id)
            self.titre_entry.delete(0, tk.END)
            self.titre_entry.insert(0, titre)
            self.auteur_entry.delete(0, tk.END)
            self.auteur_entry.insert(0, auteur)
            self.annee_entry.delete(0, tk.END)
            self.annee_entry.insert(0, annee)
            self.genre_entry.delete(0, tk.END)
            self.genre_entry.insert(0, genre)

    def quitter(self):
        """
        Fermeture de l'application et la connexion à la base de données.
        """
        self.bibliotheque.fermer()
        self.quit()

if __name__ == "__main__":
    app = InterfaceBibliotheque()
    app.mainloop()

