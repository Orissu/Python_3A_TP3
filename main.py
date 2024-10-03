"""
@bastien.rossiaud
@Orissu
bastien.rossiaud@gmail.com
03/10/2024
objective : main program for the pendu
to do : main program
"""

import functions as fct

#déclaration des variables
def jouer():
    lives = 8
    mot = fct.choice()
    nouv_mot, affiche = fct.first_print(mot)
    memoire_lettres = []

    print(nouv_mot)

    while fct.verif_mot_complet(affiche) : 
        lettre = str(input("Proposez une lettre : "))
    # if lettre in memoire_lettres : 
        #    memoire_lettres.append(f.lettre_proposee(lettre))
        if fct.verif_lettre(mot, lettre):
            nouv_mot, affiche = fct.affichage_mot(mot,affiche,lettre)
            print (nouv_mot)
        else : 
            print(nouv_mot)
            if fct.verif_nbre_vies(lives) == True :
                print(f"vous avez perdu, le mot était {mot}")
                raise IndexError
            else :
                lives -= 1

    print("vous avez gagné !")


jouer()
if str(input("rejouer ? ")) == "oui" :
    jouer()