def input_s(text: str, type: object):
	result = input(text)
	try:
		if type == int and result.isdigit():
			return int(result)
		elif type == float and result.replace(".", "").isdigit():
			return float(result)
		elif type == str and result.isalpha():
			return str(result)
		elif type == bool and result == True or result == False:
			return bool(result)
		else:
			print("Type non reconnu")
	except TypeError and ValueError:
		print("Erreur de saisie")
	else:
		return input_s(text, type)


def launch(prog):
	play = True
	while play:
		prog()
		
		if input_s("Voulez-vous continuer ? (Y/N) : ", str) in ("Y", "y", "Yes", "yes"):
			play = True
		else:
			play = False
