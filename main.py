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
        if plateau[x][y + 1] == 'O':
            return True
    if y - 1 >= 0:
        if plateau[x][y - 1] == 'O':
            return True
    if x + 1 < nl:
        if plateau[x + 1][y] == 'O':
            return True
    if x - 1 >= 0:
        if plateau[x - 1][y] == 'O':
            return True
    if x + 1 < nl and y + 1 < nc:
        if plateau[x + 1][y + 1] == 'O':
            return True
    if x + 1 < nl and y - 1 >= 0:
        if plateau[x + 1][y - 1] == 'O':
            return True
    if x - 1 >= 0 and y - 1 >= 0:
        if plateau[x - 1][y - 1] == 'O':
            return True
    if x - 1 >= 0 and y + 1 < nc:
        if plateau[x - 1][y + 1] == 'O':
            return True
    return False


def jeu():
    # Phase d'initialisation

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

        # TODO : déplacement

        # TODO : destruction

        # TODO : affichage

        joueur = 2 / joueur  # permet de passer au joueur suivant sans utiliser un if


if __name__ == '__main__':
    jeu()
