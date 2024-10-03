"""
@bastien.rossiaud
@Orissu
bastien.rossiaud@gmail.com
03/10/2024
objective : main program for the pendu
to do : main program
"""

import functions as f

#déclaration des variables

lives = 8
mot = f.choice()
affiche = f.first_print(mot)
memoire_lettres = []

print(affiche)

while f.verif_mot_complet == True : 
    lettre = str(input("Proposez une lettre : "))
    if lettre in memoire_lettres : 
        string = f.lettre_proposee(lettre)
    if f.verif_lettre(mot, lettre):
            pass