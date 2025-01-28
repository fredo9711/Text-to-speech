import tkinter as tk
from tkinter import ttk
from Running_Texttospeech import *

"""

speaking rate
volume
male female
saving

"""
class Gui_mainpage ():
    def __init__(self,fenetre,title,geometry):
        self.fenetre = fenetre
        self.fenetre.geometry(geometry)
        self.fenetre.title(title)
        self.fenetre.resizable(width=True,height=True)
        self.entry =""
        self.Gui_widget()
        self.fenetre.mainloop()
    
    
    
    def Gui_widget(self):
        self.labelTexte = tk.Label(text="Texte qui va etre convertie en parole")
        self.entryTexte = tk.Entry()
        self.labelspeakingrate = tk.Label(text="Reglage pour le speaking rate")
        self.scalespeakingrate = tk.Scale(from_=0,to=100,orient=tk.HORIZONTAL)
        self.labelvolume = tk.Label(text="Reglage pour le volume")
        self.scalevolume = tk.Scale(from_=0,to=100,orient=tk.HORIZONTAL)
        self.listeHF = ["Homme","Femme"]
        self.comboboxHF = ttk.Combobox()
        self.comboboxHF["value"] = self.listeHF
        self.boutonEcoute = tk.Button(text="Ecoute")
        self.BoutonSave = tk.Button(text="sauvegarder")

        
        self.labelTexte.pack()
        self.entryTexte.pack()
        self.labelspeakingrate.pack()
        self.scalespeakingrate.pack()
        self.labelvolume.pack()
        self.scalevolume.pack()
        self.comboboxHF.pack()
        self.boutonEcoute.pack()
        self.BoutonSave.pack()




test = Gui_mainpage(tk.Tk(),"test","600x600")



