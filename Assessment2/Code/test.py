def eight(input, a):
	space = ""
	input = input[0:a] + (a*space) + input[a+a:]
	return input
print(eight("Chocolate", 1)) #"Choate"
	# eight("Chocolate", 1) → "Choclate"