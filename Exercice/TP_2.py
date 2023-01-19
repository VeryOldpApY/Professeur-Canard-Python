from extra import input_s

def jeu_allumettes():
	nb_almt = 6
	nb_almt_max = 3
	player = "computer"
	while nb_almt > 1:
		if nb_almt <= 3:
			nb_almt_max = nb_almt - 1
		nb_almt_temp = 0
		while 0 > nb_almt > 3:
			nb_almt_temp = input_s(str(("Entrez le nombre d'allumettes à retirer (1-", nb_almt_max, "): ")), int)
		nb_almt -= nb_almt_temp
