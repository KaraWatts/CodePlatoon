# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):

	character_list1 = sorted(string1.lower().replace(' ', ''))
	character_list2 = sorted(string2.lower().replace(' ', ''))

	return character_list1 == character_list2



# Part 2
def anagrams_for(word, list_of_words):
	
	anagram_list = [test_word for test_word in list_of_words if is_character_match(word, test_word)]
	print(anagram_list)
	return anagram_list

