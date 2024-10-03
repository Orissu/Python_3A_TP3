"""
@bastien.rossiaud
@Orissu
bastien.rossiaud@gmail.com
03/10/2024
objective : faire un jeu du pendu avec tkinter
to do : finir le main code avec la fonction jouer et GUI
"""


from tkinter import Tk, Label, Button
import functions as fct

def jouer():
    lives = 8
    mot = fct.choice()
    memoire_lettres = []
    nouv_mot, affiche = fct.first_print(mot)
    pass

mw = Tk()
mw.title('jeu du pendu')
mw.geometry('800x400+100+100')
bouton_jouer = Button(mw, text ='Jouer', command=jouer)
bouton_jouer.pack(expand=True) #a programmer
bouton_quitter = Button(mw, text ='Quitter', command = mw.destroy)
bouton_quitter.pack(side = "bottom") #a programmer

mw.mainloop()