"""
@bastien.rossiaud
@Orissu
bastien.rossiaud@gmail.com
03/10/2024
objective : program that contains functions to realise a "pendu"
to do : main program
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
    alea = r.random(len(mots))
    return mots[alea]    

def affichage_mot(mot, affiche, lettre): 
    """fonction qui effectue l'affichage du mot
    in : str (un mot); lettre un str
    out : str (le mot en train d'etre cherché)"""
    for i, el in enumerate(mot) : 
         if el == lettre :
              affiche[i] = lettre
    for el in affiche : 
         nouv_mot += el
    return nouv_mot

def first_print(mot):
        affiche = [mot[0],"___" * len(mot) - 1]
        return affiche

def verif_lettre(mot, lettre):
     return lettre in mot

def verif_mot_complet(affiche) : 
     return "___" in affiche

def lettre_proposee(lettre):
     string = str(input("Lettre deja proposée choississez en une autre : "))
     if string != lettre : 
          return string

