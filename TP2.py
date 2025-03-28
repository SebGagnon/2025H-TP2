"""
TP2 : Gestion d'une base de données d'un hôpital

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

import csv

########################################################################################################## 
# PARTIE 1 : Initialisation des données (2 points)
##########################################################################################################

def load_csv(csv_path):
    """
    Fonction python dont l'objectif est de venir créer un dictionnaire "patients_dict" à partir d'un fichier csv

    Paramètres
    ----------
    csv_path : chaîne de caractères (str)
        Chemin vers le fichier csv (exemple: "/home/data/fichier.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans le fichier csv
        
    """
    patients_dict={}
  
    with open(csv_path, 'r') as file :
        reader=csv.DictReader(file)
        for row in reader :
            id=row['participant_id']
            del row['participant_id']
            patients_dict[id]=row

            
    return patients_dict

########################################################################################################## 
# PARTIE 2 : Fusion des données (3 points)
########################################################################################################## 

def load_multiple_csv(csv_path1, csv_path2):
    """
    Fonction python dont l'objectif est de venir créer un unique dictionnaire "patients" à partir de deux fichier csv

    Paramètres
    ----------
    csv_path1 : chaîne de caractères (str)
        Chemin vers le premier fichier csv (exemple: "/home/data/fichier1.csv")
    
    csv_path2 : chaîne de caractères (str)
        Chemin vers le second fichier csv (exemple: "/home/data/fichier2.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans les deux fichier csv SANS DUPLICATIONS
    """
    

    patients_dict=load_csv(csv_path1)
    dictionnaire2=load_csv(csv_path2)

    for cle in dictionnaire2 :
        if cle not in patients_dict :
            patients_dict[cle]=dictionnaire2[cle]

    return patients_dict

########################################################################################################## 
# PARTIE 3 : Changements de convention (4 points)
########################################################################################################## 

def update_convention(old_convention_dict):
    """
    Fonction python dont l'objectif est de mettre à jour la convention d'un dictionnaire. Pour ce faire, un nouveau dictionnaire
    est généré à partir d'un dictionnaire d'entré.

    Paramètres
    ----------
    old_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant l'ancienne convention
    
    Résultats
    ---------
    new_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant la nouvelle convention
    """
    new_convention_dict = {}

    for cle in old_convention_dict :
        (old_convention_dict[cle]['date_of_scan'])=(old_convention_dict[cle]['date_of_scan']).replace('-','/')
        if (old_convention_dict[cle]['date_of_scan'])== 'n/a' :
            (old_convention_dict[cle]['date_of_scan'])= None       

    new_convention_dict = old_convention_dict

    return new_convention_dict

########################################################################################################## 
# PARTIE 4 : Recherche de candidats pour une étude (5 points)
########################################################################################################## 

def fetch_candidates(patients_dict):
    """
    Fonction python dont l'objectif est de venir sélectionner des candidats à partir d'un dictionnaire patients et 3 critères:
    - sexe = femme
    - 25 <= âge <= 32
    - taille > 170

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    candidates_list : liste python (list)
        Liste composée des `participant_id` de l'ensemble des candidats suivant les critères
    """
    candidates_list = []

    for cle in patients_dict:
        if patients_dict[cle]['sex']=='F':
            if 25<=int(patients_dict[cle]['age'])<=32 :
                if int(patients_dict[cle]['height']) > 170 :
                       candidates_list.append(cle)


    return candidates_list

########################################################################################################## 
# PARTIE 5 : Statistiques (6 points)
########################################################################################################## 

def fetch_statistics(patients_dict):
    """
    Fonction python dont l'objectif est de venir calculer et ranger dans un nouveau dictionnaire "metrics" la moyenne et 
    l'écart type de l'âge, de la taille et de la masse pour chacun des sexes présents dans le dictionnaire "patients_dict".

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux contenant:
            - au premier niveau: le sexe --> metrics.keys() == ['M', 'F']
            - au deuxième niveau: les métriques --> metrics['M'].keys() == ['age', 'height', 'weight'] et metrics['F'].keys() == ['age', 'height', 'weight']
            - au troisième niveau: la moyenne et l'écart type --> metrics['M']['age'].keys() == ['mean', 'std'] ...
    
    """
    metrics = {'M':{}, 'F':{}}

    # TODO : Écrire votre code ici\

    # Moyenne et ecart type age filles

    nombre_filles=0
    age_filles=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='F':
            if patients_dict[cle]['age']!='n/a':
                nombre_filles+=1
                age_filles+=int(patients_dict[cle]['age'])
      
    moyenne_age_filles=age_filles/nombre_filles
   
    ecart=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='F':
            if patients_dict[cle]['age']!='n/a':
                ecart=ecart + (int(patients_dict[cle]['age'])-moyenne_age_filles)**2

    ecart_type_age_filles=(ecart/moyenne_age_filles)**(0.5)
    
    # Moyenne et ecart type taille filles

    nombre_filles=0
    taille_filles=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='F':
            if patients_dict[cle]['height']!='n/a':
                nombre_filles+=1
                taille_filles+=int(patients_dict[cle]['height'])
      
    moyenne_taille_filles=taille_filles/nombre_filles
   
    ecart=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='F':
            if patients_dict[cle]['height']!='n/a':
                ecart=ecart + (int(patients_dict[cle]['height'])-moyenne_taille_filles)**2
                
    ecart_type_taille_filles=(ecart/moyenne_taille_filles)**(0.5)
    
    # Moyenne et ecart type poids

    nombre_filles=0
    poids_filles=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='F':
            if patients_dict[cle]['weight']!='n/a':
                nombre_filles+=1
                poids_filles+=int(patients_dict[cle]['weight'])
      
    moyenne_poids_filles=poids_filles/nombre_filles
   
    ecart=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='F':
            if patients_dict[cle]['weight']!='n/a':
                ecart=ecart + (int(patients_dict[cle]['weight'])-moyenne_poids_filles)**2
                
    ecart_type_poids_filles=(ecart/moyenne_poids_filles)**(0.5)
    
    
     # Moyenne et ecart type age gars

    nombre_gars=0
    age_gars=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='M':
            if patients_dict[cle]['age']!='n/a':
                nombre_gars+=1
                age_gars+=int(patients_dict[cle]['age'])
      
    moyenne_age_gars=age_gars/nombre_gars
   
    ecart=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='M':
            if patients_dict[cle]['age']!='n/a':
                ecart=ecart + (int(patients_dict[cle]['age'])-moyenne_age_gars)**2

    ecart_type_age_gars=(ecart/moyenne_age_gars)**(0.5)
    
    # Moyenne et ecart type taille gars

    nombre_gars=0
    taille_gars=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='M':
            if patients_dict[cle]['height']!='n/a':
                nombre_gars+=1
                taille_gars+=int(patients_dict[cle]['height'])
      
    moyenne_taille_gars=taille_gars/nombre_gars
   
    ecart=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='M':
            if patients_dict[cle]['height']!='n/a':
                ecart=ecart + (int(patients_dict[cle]['height'])-moyenne_taille_gars)**2
                
    ecart_type_taille_gars=(ecart/moyenne_taille_gars)**(0.5)
    
    # Moyenne et ecart type poids

    nombre_gars=0
    poids_gars=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='M':
            if patients_dict[cle]['weight']!='n/a':
                nombre_gars+=1
                poids_gars+=float(patients_dict[cle]['weight'])
      
    moyenne_poids_gars=poids_gars/nombre_gars
   
    ecart=0

    for cle in patients_dict :
        if patients_dict[cle]['sex']=='M':
            if patients_dict[cle]['weight']!='n/a':
                ecart=ecart + (float(patients_dict[cle]['weight'])-moyenne_poids_gars)**2
                
    ecart_type_poids_gars=(ecart/moyenne_poids_gars)**(0.5)
    
    
    
    metrics = {'M':{'age':{'mean':moyenne_age_gars,'std':ecart_type_age_gars},'height':{'mean':moyenne_taille_gars,'std': ecart_type_taille_gars},'weight':{'mean':moyenne_poids_gars,'std':ecart_type_poids_gars}}, 'F':{'age':{"mean":moyenne_age_filles,'std':ecart_type_age_filles},'height':{'mean':moyenne_taille_filles,'std':ecart_type_taille_filles},'weight':{'mean':moyenne_poids_filles,'std': ecart_type_poids_filles }}}
      
      
    # Fin du code

    return metrics

########################################################################################################## 
# PARTIE 6 : Bonus (+2 points)
########################################################################################################## 

def create_csv(metrics):
    """
    Fonction python dont l'objectif est d'enregister le dictionnaire "metrics" au sein de deux fichier csv appelés
    "F_metrics.csv" et "M_metrics.csv" respectivement pour les deux sexes.

    Paramètres
    ----------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux généré lors de la partie 5
    
    Résultats
    ---------
    paths_list : liste python (list)
        Liste contenant les chemins des deux fichiers "F_metrics.csv" et "M_metrics.csv"
    """
    paths_list = []

    # TODO : Écrire votre code ici
    
    fieldnames = ['stats', 'age', 'height', 'weight']
    with open('F_metrics.csv','w',newline='') as file :
        writer=csv.writer(file,delimiter=',')
        writer.writerow([i for i in fieldnames])
        writer.writerow(['mean',str(metrics['F']['age']['mean']),str(metrics['F']['height']['mean']),str(metrics['F']['weight']['mean'])])
        writer.writerow(['std',str(metrics['F']['age']['std']),str(metrics['F']['height']['std']),str(metrics['F']['weight']['std'])])
    with open('M_metrics.csv','w',newline='') as file :
        writer=csv.writer(file,delimiter=',')
        writer.writerow([i for i in fieldnames])
        writer.writerow(['mean',str(metrics['M']['age']['mean']),str(metrics['M']['height']['mean']),str(metrics['M']['weight']['mean'])])
        writer.writerow(['std',str(metrics['M']['age']['std']),str(metrics['M']['height']['std']),str(metrics['M']['weight']['std'])])

    paths_list = ['F_metrics.csv','M_metrics.csv']
    # Fin du code
   
    return paths_list

########################################################################################################## 
# TESTS : Le code qui suit permet de tester les différentes parties 
########################################################################################################## 

if __name__ == '__main__':
    ######################
    # Tester la partie 1 #
    ######################

    # Initialisation de l'argument
    csv_path = "subjects.csv"

    # Utilisation de la fonction
    patients_dict = load_csv(csv_path)

    # Affichage du résultat
    print("Partie 1: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 2 #
    ######################

    # Initialisation des arguments
    csv_path1 = "subjects.csv"
    csv_path2 = "extra_subjects.csv"

    # Utilisation de la fonction
    patients_dict_multi = load_multiple_csv(csv_path1=csv_path1, csv_path2=csv_path2)

    # Affichage du résultat
    print("Partie 2: \n\n", patients_dict_multi, "\n")

    ######################
    # Tester la partie 3 #
    ######################

    # Utilisation de la fonction
    new_patients_dict = update_convention(patients_dict)

    # Affichage du résultat
    print("Partie 3: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 4 #
    ######################

    # Utilisation de la fonction
    patients_list = fetch_candidates(patients_dict)

    # Affichage du résultat
    print("Partie 4: \n\n", patients_list, "\n")

    ######################
    # Tester la partie 5 #
    ######################

    # Utilisation de la fonction
    metrics = fetch_statistics(patients_dict)

    # Affichage du résultat
    print("Partie 5: \n\n", metrics, "\n")
    

    ######################
    # Tester la partie 6 #
    ######################

    # Initialisation des arguments
    dummy_metrics = {'M':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}, 
                     'F':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}}
    
    # Utilisation de la fonction
    paths_list = create_csv(metrics)

    # Affichage du résultat
    print("Partie 6: \n\n", paths_list, "\n")

