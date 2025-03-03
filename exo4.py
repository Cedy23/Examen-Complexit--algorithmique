#Problème de distance entre ville 

distance_parcourue_livraison = 450 #en km
consommation_par_100km = 14 #en L
litres_carburant_necessaires = (distance_parcourue_livraison * consommation_par_100km) / 100 #en L
print(f"Litres de carburant nécessaires pour la livraison : {litres_carburant_necessaires} L")

prix_litre_carburant = 4800 #en MGA
coût_total_carburant = int(litres_carburant_necessaires * prix_litre_carburant) #en MGA
print(f"Coût total du carburant pour la livraison : {coût_total_carburant} MGA")

# Calcul de la consommation avec le nouveau camion (20% de carburant en moins)
reduction_consommation = 0.20
nouvelle_consommation_par_100km = consommation_par_100km * (1 - reduction_consommation)
litres_carburant_necessaires_reduit = (distance_parcourue_livraison * nouvelle_consommation_par_100km) / 100 
print(f"Litres de carburant nécessaires pour la livraison avec le nouveau camion : {litres_carburant_necessaires:.2f} L")

coût_total_carburant_reduit = litres_carburant_necessaires_reduit * prix_litre_carburant  # en MGA
print(f"Coût total du carburant pour la livraison avec le nouveau camion : {coût_total_carburant_reduit:.2f} MGA")
