import random

from extra import *
from random import choice, randint


def jeu_allumettes():
	nb_almt = 6
	nb_almt_max = 3
	player = choice(["Computer", "Joueur"])
	print("Bienvenue dans le jeu des allumettes")
	while nb_almt > 1:
		player = "Computer" if player == "Joueur" else "Joueur"
		nb_almt_temp = 0
		if nb_almt <= 3:
			nb_almt_max = nb_almt - 1
		print("TOUR : ", player, ", il reste ", nb_almt, "allumettes")
		while nb_almt_temp == 0 or nb_almt_temp > nb_almt_max:
			if player == "Computer":
				nb_almt_temp = randint(1, nb_almt_max)
			else:
				print("Entrer le nombre d'allumettes à retirer ( 1 -", nb_almt_max, ") : ", end="")
				nb_almt_temp = input_s("", int)
			if nb_almt_temp <= 0 or nb_almt_temp > nb_almt_max:
				print("Erreur, nombre d'allumettes incorrect, veuillez réessayer")
			else:
				print("Le", player, "a retiré ", nb_almt_temp, "allumettes")
		nb_almt -= nb_almt_temp
	print("Le joueur", player, "a gagner")


def write_in_file():
	entier_un = input_s("Entrez un entier : ", int)
	entier_de = input_s("Entrez un autre entier : ", int)
	file = open("Exercice/BDD.txt", "w")
	file.write(str(entier_un) + " " + str(entier_de) + "\n")
	file.close()
	file = open("Exercice/BDD.bin", "w")
	file.write(str(entier_un) + " " + str(entier_de) + "\n")
	file.close()
	file = open("Exercice/BDD.txt", "r")
	print(file.read())
	file = open("Exercice/BDD.bin", "r")
	print(file.read())
	file.close()
	

def livre_prin():
	livre_prince = Livre("Le petit prince", "Antoine de Saint-Exupéry", "Gallimard", "9782070413095")
	print(livre_prince)
	livre_prince.change_name("Le grand prince")
	livre_prince.change_author("Jean de Saint-Malo")
	livre_prince.change_edition("Hachette")
	livre_prince.change_code_barre("000000001")
	print(livre_prince)


def roman_prin():
	roman_prince = Roman("Le petit prince", "Antoine de Saint-Exupéry", "Gallimard", "9782070413095", "Roman",
						 "Un petit garçon voyage sur une planète")
	print(roman_prince)
	roman_prince.change_name("Le grand prince")
	roman_prince.change_author("Jean de Saint-Malo")
	roman_prince.change_edition("Hachette")
	roman_prince.change_code_barre("000000001")
	roman_prince.change_genre("Roman++")
	roman_prince.change_resume("Un grand garçon voyage sur une planète")
	print(roman_prince)


class Livre:
	def __init__(self, name, author, edition, code_barre):
		self.name = name
		self.author = author
		self.edition = edition
		self.code_barre = code_barre
	
	def __str__(self):
		return "Nom : " + self.name + "\nAuteur : " + self.author + "\nEdition : " + self.edition + "\nCode barre : " + self.code_barre + "\n"
	
	def change_name(self, name):
		self.name = name
	
	def change_author(self, author):
		self.author = author
	
	def change_edition(self, edition):
		self.edition = edition
	
	def change_code_barre(self, code_barre):
		self.code_barre = code_barre


class Roman(Livre):
	def __init__(self, name, author, edition, code_barre, genre, description):
		super().__init__(name, author, edition, code_barre)
		self.genre = genre
		self.description = description
	
	def __str__(self):
		return super().__str__() + "Genre : " + self.genre + "\nDescription : " + self.description + "\n"
	
	def change_genre(self, genre):
		self.genre = genre
	
	def change_resume(self, description):
		self.description = description
