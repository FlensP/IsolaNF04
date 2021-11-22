import random

nc = 0
nl = 0
plateau = []


def find_player(joueur):
    for x in range(nl):
        for y in range(nc):
            if plateau[x][y] == str(joueur):
                return x, y


def check_possible(joueur):
    x, y = find_player(joueur)
    if y + 1 < nc:
        if plateau[x][y + 1] == '0':
            return True
    if y - 1 >= 0:
        if plateau[x][y - 1] == '0':
            return True
    if x + 1 < nl:
        if plateau[x + 1][y] == '0':
            return True
    if x - 1 >= 0:
        if plateau[x - 1][y] == '0':
            return True
    if x + 1 < nl and y + 1 < nc:
        if plateau[x + 1][y + 1] == '0':
            return True
    if x + 1 < nl and y - 1 >= 0:
        if plateau[x + 1][y - 1] == '0':
            return True
    if x - 1 >= 0 and y - 1 >= 0:
        if plateau[x - 1][y - 1] == '0':
            return True
    if x - 1 >= 0 and y + 1 < nc:
        if plateau[x - 1][y + 1] == '0':
            return True

    return False


def affichage():
    print("\n")
    for i in range(2 * nl + 1):
        if (i % 2) == 0:
            for j in range(nc):
                print("__", end='')
        else:
            for j in range(2 * nc + 1):
                if (j % 2) == 0:
                    print("|", end='')
                else:
                    print(plateau[int((i - 1) / 2)][int((j - 1) / 2)], end='')
        print("\n", end='')


def jeu():
    # Phase d'initialisation

    global nl, nc, plateau

    while nl <= 1:  # le nombre de lignes doit être supérieur à 1
        nl = int(input("Rentrez le nombre de lignes du plateau"))
    while nc < nl or nc <= 1:  # le nombre de colonnes doit être supérieur à 1 et supérieur ou égal au nombre de ligne
        nc = int(input("Rentrez le nombre de colonnes du plateau"))
    # le joueur doit choisir avec quel mode il veut jouer
    isComp = input("Si vous souhaitez jouer contre un ordinateur, envoyez 'y', sinon, envoyez n'importe quoi d'autre")
    computer = (isComp == 'y')
    plateau = [['0' for _ in range(nc)] for _ in range(nl)]  # creation du plateau en fonction des paramètres

    # positionnement initial des pions
    if nl % 2 == 0:
        plateau[int(nl / 2)][0] = '1'
        plateau[int(nl / 2 - 1)][nc - 1] = '2'
    else:
        plateau[int((nl - 1) / 2)][0] = '1'
        plateau[int((nl - 1) / 2)][nc - 1] = '2'

    affichage()
    # phase de jeu
    joueur = 1
    while check_possible(joueur):
        if (joueur == 2) and computer:
            print("C'est au tour de l'ordinateur")
        else:
            print("C'est au tour du joueur ", joueur)

        # déplacement
        deplacement_fait = False
        if (joueur == 1) or not computer:
            while not deplacement_fait:
                posx = int(input("Où voulez-vous placer votre pion en ligne ?"))
                posy = int(input("Où voulez-vous plcer votre pion en colonne ?"))
                x, y = find_player(joueur)
                if abs(posy - y) <= 1 and abs(posx - x) <= 1:
                    if 0 <= posx < nl and 0 <= posy < nc:
                        if plateau[posx][posy] == '0':
                            plateau[x][y] = '0'
                            plateau[posx][posy] = str(joueur)
                            deplacement_fait = True
        else:
            while not deplacement_fait:
                posx = int(random.choice(range(nl)))
                posy = int(random.choice(range(nc)))
                x, y = find_player(joueur)
                if abs(posy - y) <= 1 and abs(posx - x) <= 1:
                    if 0 <= posx < nl and 0 <= posy < nc:
                        if plateau[posx][posy] == '0':
                            plateau[x][y] = '0'
                            plateau[posx][posy] = str(joueur)
                            deplacement_fait = True

        # destruction
        destruction_faite = False
        if (joueur == 1) or not computer:
            while not destruction_faite:
                posx = int(input("Quelle case voulez-vous détruire en ligne ?"))
                posy = int(input("Quelle case voulez-vous détruire en colonne"))
                if 0 <= posx < nl and 0 <= posy < nc:
                    if plateau[posx][posy] == '0':
                        plateau[posx][posy] = 'X'
                        destruction_faite = True
        else:
            while not destruction_faite:
                posx = int(random.choice(range(nl)))
                posy = int(random.choice(range(nc)))
                if 0 <= posx < nl and 0 <= posy < nc:
                    if plateau[posx][posy] == '0':
                        plateau[posx][posy] = 'X'
                        destruction_faite = True

        affichage()

        joueur = int(2 / joueur)  # permet de passer au joueur suivant sans utiliser un if
    print("Le gagnant est le joueur :", int(2 / joueur))


if __name__ == '__main__':
    jeu()
