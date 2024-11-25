
def longest_unique_substring(string): 

	#dernier index
	last_index = {} 
	max_length = 0

	# premier index 
	# taille maximum
	start_index = 0

	for i in range(0, len(string)): 
		
		#trouver le dernier indexstr[i] 
		# Mise à jour de l'index de départ comme maximum de la valeur actuelle de l'index de départ et de la dernière valeur de l'index de départ.  
		# index plus 1 
		if string[i] in last_index: 
			start_index = max(start_index, last_index[string[i]] + 1) 

		# mise à jour du resutats si on a un taille plus grande
		max_length = max(max_length, i-start_index + 1) 

		# mise à jour du dernier index du caractère courant. 
		last_index[string[i]] = i 

	return max_length 



# input = "ABDEFGABEF"
# print(input) 
# output = longest_unique_substring(input) 
# print( str(output)) 
