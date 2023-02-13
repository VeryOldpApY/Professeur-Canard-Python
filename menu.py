from Exercice.TP_1 import *
from Exercice.TP_2 import *
from extra import *


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
		case 2:
			exercice = input_s("Entrez le numéro d'exercice : (2-5)\n", int)
			match exercice:
				case 2:
					launch(jeu_allumettes)
				case 3:
					launch(write_in_file)
				case 4:
					launch(livre_prin)
				case 5:
					launch(roman_prin)
				case _:
					print("Exercice inconnu")
		case _:
			print("TP inconnu")
