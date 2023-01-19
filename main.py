from Exercice.TP_1 import *
from extra import *


def main():
	launch(menu)
	print("Au revoir !")


def menu():
	tp = input_s("Entrez le numéro du TP : (1-2)\n", int)
	match tp:
		case 1:
			exercice = input_s("Entrez le numéro d'exercice : (1-8)\n", int)
			match exercice:
				case 1:
					launch(types_predefinis)
				case 2:
					launch(calcul_surface)
				case 3:
					launch(somme_factoriel)
				case 4:
					launch(arbre_noel)
				case 5:
					launch(math)
				case _:
					print("Exercice inconnu")
		case _:
			print("TP inconnu")
