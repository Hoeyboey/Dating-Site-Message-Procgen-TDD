def init(source_messages):
	word_dictionary = {}
	
	for x in source_messages:
		x = x.lower()
		words_in_current_message = x.split(" ")
		for y in words_in_current_message:
			if y not in word_dictionary:
				word_dictionary[y] = 1
			else:
				word_dictionary[y] = word_dictionary[y] + 1
	return word_dictionary     