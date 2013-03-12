from sys import argv
script, filename = argv

def ratings_out(filename):
	in_file = open(filename)
	read_file = in_file.readlines()
	in_file.close()
	strip_lines = [i.split('\n', 1)[0] for i in read_file]
	
	dictionary = {}
	for element in strip_lines:
		separate_lines = element.split(":")
		restaurant_name = separate_lines[0]
		rating = separate_lines[1]
		dictionary[restaurant_name] = rating

		# key = separate_lines[0]
		# for key in separate_lines:
		# 	if key in dictionary:
		# 		dictionary[key] = separate_lines[1]
		print dictionary

ratings_out(filename)


#     dictionary = {}          
#     for word in word_list:
#         if word in dictionary:
#             dictionary[word] += 1
#         else:
#             dictionary[word] = 1
#     print dictionary

# count_words(filename)
	
