from character_match import is_character_match, anagrams_for

# Part 1
print(is_character_match('charm', 'march') == True)
print(is_character_match('zach', 'attack') == False)
print(is_character_match('CharM', 'mARcH') == True)
print(is_character_match('abcde2', 'c2abed') == True)

print("This test is for the challenge quesiton")
print(is_character_match('Anna Madrigal', 'A man and a girl') == True)

# Part 2

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
list_of_words2 = ["threads", "tra   she  d", "har.d,e/st", "hat8red+s"]
print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
print(anagrams_for("threads", list_of_words2) == ["threads", "trashed"])
print(anagrams_for("apple", list_of_words) == [])
