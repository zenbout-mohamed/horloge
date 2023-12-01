# Nous tenons à rappeler que ce programme creer une classe Horloge avec les méthodes nécessaires pour afficher l'heure,
# régler l'heure, régler une alarme et vérifier si l'heure actuelle correspond à l'heure de l'alarme.

# Le module time est utilisé pour introduire des délais dans le programme.
# Il est particulièrement utile ici pour faire une pause d'une seconde entre chaque mise à jour de l'heure.
import time
import threading
# La fonction qui permet de mettre en pause et relancer l'horloge, vous pouvez utiliser la bibliothèque threading de Python pour créer un thread séparé qui gère l'actualisation de l'heure.
# La classe Horloge est définie avec des méthodes pour afficher l'heure, régler l'heure, régler une alarme,
# et de vérifier si l'alarme est déclenchée, et démarrer l'horloge.
class Horloge:
    # La méthode '__init__' est un constructeur qui initialise les attributs de l'objet Horloge avec l'heure passée en paramètre
    #  et initialise l'alarme à None.
    def __init__(self, heures, minutes, secondes):
        # (self) est un paramètre implicite dans les méthodes d'une classe.
        # Il fait référence à l'instance de la classe elle-même.
        # L'utilisation de self permet d'accéder aux attributs et méthodes de l'objet à l'intérieur de ses propres méthodes.
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
        self.alarme = None
        # Par défaut, le mode 24 heures est activé.
        self.mode_12_heures = False  
        self.pause = False
        self.pause_lock = threading.Lock()

        def afficher_heure(self):
            if self.mode_12_heures :
                return self._afficher_heure_12_heures()
            else:
                return self._afficher_heure_24_heures()

    def _afficher_heure_24_heures(self):
        heure_format = "{:02d}:{:02d}:{:02d}".format(self.heures, self.minutes, self.secondes)
        return heure_format

    def _afficher_heure_12_heures(self):
        suffixe_am_pm = "AM" if self.heures < 12 else "PM"
        heures_12_format = self.heures % 12 or 12
        heure_format = "{:02d}:{:02d}:{:02d} {}".format(heures_12_format, self.minutes, self.secondes, suffixe_am_pm)
        return heure_format


    def afficher_heure(self):
        heure_format = "{:02d}:{:02d}:{:02d}".format(self.heures, self.minutes, self.secondes)
        print(heure_format)
    # Cette méthode formate l'heure au format "hh:mm:ss" et l'affiche à la console.
    def regler_heure(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
        self.afficher_heure()

    # Cette méthode permet de régler manuellement l'heure en mettant à jour les attributs et en affichant la nouvelle heure.
    def regler_alarme(self, heures, minutes, secondes):
        self.alarme = (heures, minutes, secondes)
    # Cette méthode permet de régler une alarme en spécifiant une heure à laquelle l'alarme devrait se déclencher.
    def verifier_alarme(self):
        if self.alarme is not None and (self.heures, self.minutes, self.secondes) == self.alarme:
            print("Réveil! Il est maintenant {}.".format(self.afficher_heure()))
    # Cette méthode vérifie si l'alarme est déclenchée en comparant l'heure actuelle avec l'heure réglée pour l'alarme.
    # Si elles correspondent, un message est affiché.
    def demarrer(self):
    # La boucle while True est une boucle infinie en programmation. Elle continuera à s'exécuter indéfiniment tant que la condition spécifiée (True) reste vraie.
    # Dans ce programme, la boucle {while True} est utilisée dans la méthode demarrer de la classe Horloge,
    # pour maintenir le fonctionnement continu de l'horloge. Voici comment elle est utilisée dans ce code.
        while True:
            with self.pause_lock:
                if self.pause:
                    continue
            time.sleep(1) # time.sleep(1) : Cette ligne fait une pause d'une seconde à chaque itération de la boucle, ce qui signifie que le code à l'intérieur de la boucle s'exécute toutes les secondes.
            self.secondes += 1 # self.secondes += 1 : Incrémente le compteur des secondes de l'horloge.
            if self.secondes == 60: # Vérifie si le compteur des secondes atteint 60.Si le compteur des secondes atteint 60, les lignes suivantes sont exécutées :
                self.secondes = 0 # Réinitialise le compteur des secondes à zéro.
                self.minutes += 1 # Incrémente le compteur des minutes.
                if self.minutes == 60: # Vérifie si le compteur des minutes atteint 60. Si le compteur des minutes atteint 60, les lignes suivantes sont exécutées :
                    self.minutes = 0   # Réinitialise le compteur des secondes à zéro.
                    self.heures += 1   # Incrémente le compteur des heures.
                    if self.heures == 24:# Vérifie si le compteur des heures atteint 24. Si le compteur des heures atteint 24, les lignes suivantes sont exécutées :
                        self.heures = 0 #Réinitialise le compteur des heures à zéro.
            self.afficher_heure()   #Nous appellons la méthode afficher_heure() pour afficher l'heure formatée à chaque itération.
            self.verifier_alarme() # Appelle la méthode verifier_alarme() pour vérifier si l'heure actuelle correspond à l'heure de l'alarme et affiche un message si nécessaire.

    def choisir_mode_affichage(self, mode_12_heures=True):
        self.mode_12_heures = mode_12_heures

    def mettre_en_pause(self):
        with self.pause_lock:
            self.pause = True

    def relancer(self):
        with self.pause_lock:
            self.pause = False
            
# Utilisation du programme :
heure = Horloge(16, 30, 0)
heure.regler_alarme(16, 30, 10)  # Nous Réglons l'alarme 10 secondes après l'heure actuelle
heure.choisir_mode_affichage()  # Active le mode 12 heures
heure.demarrer()

# Mettre en pause l'horloge après 5 secondes
time.sleep(5)
horloge.mettre_en_pause()
print("Horloge en pause pendant 5 secondes...")

# Relance l'horloge après 5 secondes
time.sleep(5)
horloge.relancer()
print("Horloge relancée. Actualisation reprise.")
horloge.demarrer()  # La boucle de l'horloge continue



# Cette boucle crée un mécanisme où l'horloge s'incrémente chaque seconde, gérant correctement le passage des secondes,
# des minutes et des heures, et affiche l'heure formatée à chaque itération.
# Elle est conçue pour s'exécuter indéfiniment jusqu'à ce qu'elle soit arrêtée manuellement (par exemple, en interrompant le programme).
