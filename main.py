# import

nc = 0
nl = 0
plateau = []


def find_player(joueur):
    for x in range(nl):
        for y in range(nc):
            if plateau[x][y] == joueur:
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


def jeu():
    # Phase d'initialisation

    global nl, nc

    while nl <= 1:  # le nombre de lignes doit être supérieur à 1
        nl = int(input("Rentrez le nombre de lignes du plateau"))
    while nc < nl or nc <= 1:  # le nombre de colonnes doit être supérieur à 1 et supérieur ou égal au nombre de ligne
        nc = int(input("Rentrez le nombre de colonnes du plateau"))
    # le joueur doit choisir avec quel mode il veut jouer
    isComp = input("Si vous souhaitez jouer contre un ordinateur, envoyez 'y', sinon, envoyez n'importe quoi d'autre")
    computer = (isComp == 'y')
    plateau = [[0 for _ in range(nl)] for _ in range(nc)]  # creation du plateau en fonction des paramètres

    # positionnement initial des pions
    if nl % 2 == 0:
        plateau[nl / 2][0] = '1'
        plateau[nl / 2 - 1][nc - 1] = '2'
    else:
        plateau[(nl - 1) / 2][0] = '1'
        plateau[(nl - 1) / 2][nc - 1] = '2'

    # phase de jeu
    joueur = 1
    while check_possible(joueur):
        i = 0

        # déplacement
        deplacement_fait = False
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

        # destruction
        destruction_faite = False
        while not destruction_faite:
            posx = int(input("Quelle case voulez-vous détruire en ligne ?"))
            posy = int(input("Quelle case voulez-vous détruire en colonne"))
            if 0 <= posx < nl and 0 <= posy < nc:
                if plateau[posx][posy] == '0':
                    plateau[posx][posy] = 'X'

                    destruction_faite = True

        # TODO : affichage

        joueur = 2 / joueur  # permet de passer au joueur suivant sans utiliser un if
    print("Le gagnant est le joueur :", 2 / joueur)


if __name__ == '__main__':
    jeu()
