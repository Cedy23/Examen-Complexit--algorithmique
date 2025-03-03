# Dimensions du parking
longueur_parking = 120  # en m
largeur_parking = 50    # en m

# Dimensions d'une place de stationnement
longueur_place = 5      # en m
largeur_place = 2.5     # en m

# Distance entre les rangées de voitures
distance_rangee = 1     # en m

# Calcul du nombre de places de stationnement par rangée
places_par_rangee = largeur_parking // largeur_place

# Calcul du nombre de rangées de voitures
nombre_rangees = longueur_parking // (longueur_place + distance_rangee)

# Calcul du nombre total de places de stationnement
nombre_places = int(places_par_rangee * nombre_rangees)

# Tarif journalier par voiture
tarif_journalier = 3000  # en MGA

# Revenu maximum du parking sur une journée
revenu_maximum = nombre_places * tarif_journalier

# Affichage des résultats
print(f"Nombre maximum de voitures pouvant être garées : {nombre_places}")
print(f"Revenu maximum du parking sur une journée : {revenu_maximum} MGA")

# Calcul pour la zone réservée aux bus (15% de l'espace total)
espace_total = longueur_parking * largeur_parking
espace_bus = 0.15 * espace_total
espace_restant = espace_total - espace_bus

# Recalcul du nombre de places de stationnement avec la zone réservée aux bus
nombre_places_restant = (espace_restant // (longueur_place * largeur_place))

# Revenu maximum du parking sur une journée avec la zone réservée aux bus
revenu_maximum_restant = int(nombre_places_restant * tarif_journalier)

# Affichage des résultats avec la zone réservée aux bus
print(f"Nombre de places disponibles avec une zone réservée aux bus : {nombre_places_restant}")
print(f"Revenu maximum du parking sur une journée avec la zone réservée aux bus : {revenu_maximum_restant} MGA")