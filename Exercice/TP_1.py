from extra import input_s
from math import *


def types_predefinis():
	lettre = input_s("Entrez une lettre : ", str)
	entier = input_s("Entrez un entier : ", int)
	
	print(lettre, " vaut ", ord(lettre))
	print(entier, " vaut ", chr(entier))


def calcul_surface():
	a = input_s("Entrez la longueur du côté A : ", int)
	b = input_s("Entrez la longueur du côté B : ", int)
	c = input_s("Entrez la longueur du côté C : ", int)
	
	print("La surface du trapèze est de ", (a + b * c * 0.5))


def somme_factoriel():
	n = input_s("Entrez un nombre : ", int)
	somme = 0
	for i in range(1, n):
		print(i, "+ ", end='')
		somme += i
	print(n, "=", somme + int(n))
	print(somme + int(n), "=", end=' ')
	for i in range(int(n), 1, -1):
		print(i, "+ ", end='')
	print(1)
	
	print()
	
	somme = 1
	for i in range(1, n):
		print(i, "* ", end='')
		somme *= i
	print(n, "=", somme * int(n))
	print(somme + int(n), "=", end=' ')
	for i in range(int(n), 1, -1):
		print(i, "* ", end='')
	print(1)


def arbre_noel():
	height = input_s("Entrez la hauteur de l'arbre : ", int)
	for i in range(0, height):
		print("=" * (height + 2 - i), end='')
		print("*" * (i * 2 + 1), end='')
		print("=" * (height + 2 - i))
		
	print("=" * (height + 2), end='')
	print("*" * 1, end='')
	print("=" * (height + 2))
	
	print("=" * (height + 2 - 1), end='')
	print("*" * 3, end='')
	print("=" * (height + 2 - 1))


def math():
	nb = input_s("Entrez un entier : ", int)
	print("Le logarithme népérien de", nb, "est", log(nb))
	print("Le sinus de", nb, "est", sin(nb))
	print("Le cosinus de", nb, "est", cos(nb))
