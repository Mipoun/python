def Morpion():

    #Permet d'initialiser le jeu
    def __init__(self):

    #Contient le code qui assure le bon déroulement du jeu en lui même
    def jeu(self):
       
    #Affiche le plateau de jeu
    def afficher_plateau(self):


    #Test si il y a un vainqueur où si il n'y a plus de mouvement possible
    def test_fin_jeu(self,joueur):
   
    #Permet à un joueur de jouer son tour      
    def jouer(self, joueur):
    
    #Permet d'initialiser le jeu
def __init__(self):
        #Création et initialisation du plateau de jeu
        self.plateau=[['-','-','-'],['-','-','-'],['-','-','-']]
        #Déclaration du premier Joueur
        self.J1='X'
        #Déclaration du second Joueur
        self.J2='O'
    
    #Permet à un joueur de jouer son tour      
def jouer(self, joueur):
        #Demande les coordonnées où le joueur souhaite jouer
        x = input("Entrez l'abscisse compris entre 1 et 3 : ")
        y = input("Entrez l'ordonnée compris entre 1 et 3 : ")
        #Affectation de la marque du joueur à la position x et y du plateau 
        self.plateau[int(x)][int(y)]=joueur
    
    #Affiche le plateau de jeu
 def afficher_plateau(self):
        for i in range (0, 3):
            for j in range (0, 3):
                print ("|", end="")
                print (self.plateau[i][j], end="")
            print ("|")
        print ("-----------------------------------------")
    
    #Test si il y a un vainqueur où si il y a plus de mouvement possible
def test_fin_jeu(self,joueur):
        #vérifie le joueur courant n'a pas aligné son signe sur une ligne
        for i in range (0,3):
            compteur=0
            for j in range (0,3):
                if self.plateau[i][j]==joueur:
                    compteur+=1
            #Si il a aligné son signe 3 fois en horizontal
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur

        #vérifie le joueur courant n'a pas aligné son signe sur une colonne
        for i in range (0,3):
            compteur=0
            for j in range (0,3):
                if self.plateau[j][i]==joueur:
                    compteur+=1
            #Si il a aligné son signe 3 fois en vertical
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur
        # Test de diagonales 1
        compteur=0
        for i in range (0,3):
            if self.plateau[i][i]==joueur:
                    compteur+=1
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur
        compteur=0
        # Test de diagonales 2
        for i in range (0,3):
            if self.plateau[2-i][i]==joueur:
                    compteur+=1
            if compteur==3:
                #le joueur est déclaré vainqueur  et donc retourné par la fonction
                return joueur
                
        #vérifie qu'il reste de la place sur le plateau en comptant les signes de tout les joueurs
        compteur=0
        for i in range (0,3):
            for j in range (0,3):
                if( self.plateau[i][j]!='-'):
                    compteur+=1
        #Si il n'y a plus de place sur le plateau
        if compteur==8: 
            # On retourne vrai pour dire que le jeu est fini
            return True
        #Le jeu n'est pas encore fini on retourne false
        return False
      
    #Contient le code qui assure le bon déroulement du jeu en lui même
def jeu(self):
        morpion.afficher_plateau()
        bool_fin_jeu=False
        #Tant que le jeu n'est pas fini
        while bool_fin_jeu==False:
            #Le joueur 1 joue
            morpion.jouer(self.J1)
            morpion.afficher_plateau()
            #Test de victoire de J1
            resultat_test_fin_jeu=self.test_fin_jeu(self.J1)
            #Si J1 à gagné
            if( resultat_test_fin_jeu==self.J1):
                #Affiche Joueur 1 à gagné
                print ("Joueur " + self.J1 +" a gagné" );
                return self.J1
            elif ( resultat_test_fin_jeu==True):
                #Affiche Égalité entre les joueurs
                print ("Égalité entre les joueurs" );
                return "égalité"
            #Le joueur 2 joue
            morpion.jouer(self.J2)
            morpion.afficher_plateau()
            resultat_test_fin_jeu=self.test_fin_jeu(self.J2)
            #Test de victoire de J2
            if( resultat_test_fin_jeu!=False):
                print ("Joueur " + self.J2 +" a gagné" );
                return self.J2
            elif ( resultat_test_fin_jeu==True):
                print ("Égalité entre les joueurs" );
                return "égalité"

