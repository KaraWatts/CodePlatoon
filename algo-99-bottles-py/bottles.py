
#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down and pass it around, 98 bottles of beer on the wall.

# Take one down and pass it around, 1 bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.

def bottle_song(n):
	for i in range(n, 0, -1):
		if i == 0:
			verse = """No more bottles of beer on the wall, no more bottles of beer.
		Go to the store and buy some more, 99 bottles of beer on the wall."""
		elif i == 1:
			verse = f"""{i} bottle of beer on the wall, {i} bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall."""
		elif i == 2:
			verse = f"""{i} bottles of beer on the wall, {i} bottles of beer.
Take one down and pass it around, {i-1} bottle of beer on the wall."""
		else:
			verse = f"""{i} bottles of beer on the wall, {i} bottles of beer.
Take one down and pass it around, {i-1} bottles of beer on the wall."""
		print(verse)


print(bottle_song(99))


