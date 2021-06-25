def longest_word_in_file():
	"""
	A program that takes in a filename and displays the longest 
	word(s) in the file we'll be making use of text files only.
	: return: None
	"""
	# get the filename
	filename = input('\nEnter the filename only, the file extension would be added: ')
	# add the file extension to the filename
	filename = filename.strip() + '.txt'
	# make a dictionary that tracks 
	# each word and their length
	words_and_their_length = {}
	try:
		with open(filename, 'r') as f_obj:
			# loop through each sentence / line and 
			# split each sentence into several words
			for i in f_obj:
				split_sentence = i.split()
				# loop through each splitted word and 
				# store the name and length of each word
				for j in split_sentence:
					words_and_their_length[j] = len(j)
	except FileNotFoundError:
		print(f'The file \'{filename}\' couldn\'t be found')
	else:
		# get the length of each word in file
		length_of_each_word = [i for i in words_and_their_length.values()]
		# get the length of the longest word
		longest_word_length = max(length_of_each_word)
		if length_of_each_word.count(longest_word_length) == 1:
			for i,j in words_and_their_length.items():
				if j == longest_word_length:
					print(f'The Longest word in the file is {i}')
		else:
			# if more than a word have the same length,
			# store all the words in a list
			tie_words = [i for i,j in words_and_their_length.items() if j == longest_word_length]
			print('The Longest words in the file are {}'.format(', '.join(tie_words)))

longest_word_in_file()