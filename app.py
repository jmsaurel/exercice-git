#!/usr/bin/env python3
"""
Programme d'affichage d'un triple salut inutile
"""

# Fonction affichage
def greetings():
	"""Salute RESIF people"""
	print("Hello RESIF people !")

# Fonction begaiement
def repeat(x, callback):
	"""Call xtimes callback."""
	for _ in range(x):
		callback()

if __name__ == "__main__":
	repeat(3, greetings)

# Et plaf, un commentaire

# Encore un commentaire
