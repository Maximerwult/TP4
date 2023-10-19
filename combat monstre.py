# par Maxime
# TP3




# on importe l'élément d'aléatoire
import random


# on définit les variables de lancer de dé et d'un combat

def lancer_de_de():
    return random.randint(1, 6)

def combat(niveau_vie):
    adversaire = random.randint(1, 5)
    score_de = lancer_de_de()


    if score_de > adversaire:
        niveau_vie += adversaire
        return "victoire", niveau_vie
    else:
        niveau_vie -= adversaire
        return "défaite", niveau_vie

# niveau de vie de départ, victoires de départ, numéro du combat
def main():
    niveau_vie = 20
    nombre_victoires = 0
    combat_num = 1



# que faire?
    while True:
        adversaire = random.randint(1, 5)
        print("Vous tombez face à face avec un adversaire de difficulté:", adversaire)
        print("Que voulez-vous faire?")
        print("1- Combattre cet adversaire")
        print("2- Contourner cet adversaire et aller ouvrir une autre porte")
        print("3- Afficher les règles du jeu")
        print("4- Quitter la partie")

        choix = input()
        # choix 1 a 5
        if choix == "1":
            resultat_combat, niveau_vie = combat(niveau_vie)
            if resultat_combat == "victoire":
                nombre_victoires += 1
            else:
                if niveau_vie <= 0:
                    print("La partie est terminée, vous avez vaincu", nombre_victoires, "monstre(s).")
                    break

            if nombre_victoires >= 3:
                adversaire = "Difficile"
            else:
                adversaire = "Facile"

            print("Adversaire:", adversaire)
            print("Force de l'adversaire:", adversaire)
            print("Niveau de vie de l'usager:", niveau_vie)
            print("Combat", combat_num, ":", nombre_victoires, "vs", (combat_num - nombre_victoires))
            combat_num += 1

        elif choix == "2":
            niveau_vie -= 1
            print("Niveau de vie:", niveau_vie)

        elif choix == "3":
            print("Pour réussir un combat, il faut que la valeur obtenue par le lancer de dé dépasse la puissance du monstre adverse. Si la valeur du dé est supérieur au niveau de l'ennemi, le joueur gagne de point de vie, en revanche, si la valeur du dé est égale ou inferieure a la puissance du monstre, alors le joueur perds des points de vie")
            # Afficher les règles du jeu

        elif choix == "4":
            print("Merci et au revoir")
            break

        elif choix == "69" or "420":
            print("Funny number")
    

if __name__ == "__main__":
    main()
