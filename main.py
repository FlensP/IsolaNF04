# import


def jeu():
    # Phase d'initialisation
    nl = 0
    nc = 0

    while nl <= 1:  # le nombre de lignes doit être supérieur à 1
        nl = int(input("Rentrez le nombre de lignes du plateau"))
    while nc < nl or nc <= 1:  # le nombre de colonnes doit être supérieur à 1 et supérieur ou égal au nombre de ligne
        nc = int(input("Rentrez le nombre de colonnes du plateau"))
    # le joueur doit choisir avec quel mode il veut jouer
    isComp = input("Si vous souhaitez jouer contre un ordinateur, envoyez 'y', sinon, envoyez n'importe quoi d'autre")
    computer = (isComp == 'y')
    plateau = [[0 for x in range(nl)] for y in range(nc)]  # creation du plateau en fonction des paramètres

    # positionnement initial des pions
    if nl % 2 == 0:
        plateau[nl / 2][0] = '1'
        plateau[nl / 2 - 1][nc - 1] = '2'
    else:
        plateau[(nl - 1) / 2][0] = '1'
        plateau[(nl - 1) / 2][nc - 1] = '2'


if __name__ == '__main__':
    jeu()
