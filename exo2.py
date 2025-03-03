# Demander à un utilisateur de saisir le nombre à deviner
nombre_a_deviner = int(input("Entrez le nombre à deviner (entre 1 et 100) : "))
nombre_essais = 0
trouve = False

print("Devinez le nombre entre 1 et 100")

while not trouve:
    # Demander à l'utilisateur de proposer un nombre
    proposition = int(input("Votre proposition : "))
    nombre_essais += 1
    
    # Vérifier la proposition
    if proposition < nombre_a_deviner:
        print("Trop petit !")
    elif proposition > nombre_a_deviner:
        print("Trop grand !")
    else:
        trouve = True
        print(f"Félicitations ! Vous avez trouvé le nombre en {nombre_essais} essais.")