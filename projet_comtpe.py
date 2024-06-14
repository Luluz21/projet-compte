import json
import tkinter as tk

# Création de la fenêtre
fenetre = tk.Tk()

# Création du widget de texte
texte = tk.Text(fenetre)
texte.pack()

# Ajout du code dans le widget de texte

# Charger les comptes depuis un fichier
def charger_comptes():
    try:
        with open('comptes.json', 'r') as fichier:
            comptes = json.load(fichier)
    except FileNotFoundError:
        comptes = {}
    return comptes

# Sauvegarder les comptes dans un fichier
def sauvegarder_comptes(comptes):
    with open('comptes.json', 'w') as fichier:
        json.dump(comptes, fichier)

# Charger les comptes depuis un fichier
def charger_comptes():
    try:
        with open('comptes.json', 'r') as fichier:
            comptes = json.load(fichier)
    except FileNotFoundError:
        comptes = {}
    return comptes

# Sauvegarder les comptes dans un fichier
def sauvegarder_comptes(comptes):
    with open('comptes.json', 'w') as fichier:
        json.dump(comptes, fichier)

# Fonction pour créer un compte
def creer_compte(comptes):
    nom_utilisateur = input("Choisissez un nom d'utilisateur : ")
    mot_de_passe = input("Choisissez un mot de passe : ")

    if nom_utilisateur in comptes:
        print("Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
    else:
        comptes[nom_utilisateur] = mot_de_passe
        sauvegarder_comptes(comptes)
        print("Compte créé avec succès. Vous êtes maintenant connecté.")

# Fonction pour se connecter
def se_connecter(comptes):
    nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    if nom_utilisateur in comptes and comptes[nom_utilisateur] == mot_de_passe:
        print(f"Vous êtes connecté en tant que {nom_utilisateur}.")
        print("Bienvenue dans le monde des cieux.")
    else:
        print("Nom d'utilisateur ou mot de passe incorrects.")

# Chargement initial des comptes
comptes = charger_comptes()

# Menu principal
while True:
    print("1. Créer un compte")
    print("2. Se connecter")
    print("3. Quitter")
    choix = input("Choisissez une option : ")

    if choix == '1':
        creer_compte(comptes)
    elif choix == '2':
        se_connecter(comptes)
    elif choix == '3':
        break
    else:
        print("Option invalide. Veuillez réessayer.")
# Fermeture du programme

texte.insert(tk.END, code)

# Lancement de la boucle principale


