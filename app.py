#!/usr/bin/env python3

def greetings():
	print("Hello RESIF people !")

def repeat(x, callback):
	for _ in range(x):
		callback()

if __name__ == "__main__":
	repeat(3, greetings)

# Et plaf, un commentaire
