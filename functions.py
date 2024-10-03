"""
@bastien.rossiaud
@Orissu
bastien.rossiaud@gmail.com
03/10/2024
objective : program that contains functions to realise a "pendu"
to do : bonnes pratiques
"""

import random as r

def choice():
    """function that selects a word in a document .txt randomly
    in : None
    out : str (a word)
    """
    file = open("mots.txt",'r')
    contenu = file.read()
    mots = contenu.split()
    alea = r.randint(1, len(mots))
    return mots[alea]    

def affichage_mot(mot, affiche, lettre): 
    """fonction qui effectue l'affichage du mot
    in : str (un mot); lettre un str
    out : str (le mot en train d'etre cherché)"""
    nouv_mot = ""
    for i, el in enumerate(mot) :  
         if el == lettre :
              affiche[i] = lettre
    for el in affiche : 
         nouv_mot += el
    return nouv_mot,affiche

def first_print(mot):
     nouv_mot = ""
     affiche = [mot[0]]
     for i in range(len(mot)-1):
          affiche.append(" ___ ")
     for el in affiche : 
          nouv_mot += el
     return nouv_mot,affiche


def verif_lettre(mot, lettre):
     return lettre in mot

def verif_mot_complet(affiche) : 
     return " ___ " in affiche

def lettre_proposee(lettre):
     string = str(input("Lettre deja proposée choississez en une autre : "))
     if string != lettre : 
          return string

def verif_nbre_vies(lives):
     return lives == 0
