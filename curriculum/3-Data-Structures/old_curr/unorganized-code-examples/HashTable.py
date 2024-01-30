class HashTable:
    def __init__(self):

        self.table = [[] for i in range(64)]   # creates a list of 64 lists

    # given a key, this function should return a numerical index, which we can use to access the table above

    def _hash(self, key):
        hash = 0
        for char in key:
            # returns an integer representing a unicode character
            hash += ord(char)

        return hash % len(self.table)

    def set(self, key, value):
        index = self._hash(key)
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)

        for data in self.table[index]:
            if data[0] == key:
                return data[1]


myHash = HashTable()

myHash.set('name', 'alice')
myHash.set('age', 34)
# this key will cause a hash collision with 'name', because they are anagrams
myHash.set('mane', 'luxurious')

print(myHash.table)
print(myHash.get('name'))
print(myHash.get('age'))
print(myHash.get('mane'))
print(myHash.get('mean'))


# Comparison of List to Dict in terms of compelxity

reference = ["name", "age"]

lst = [("name", "alice"), ("mane", "luxurious"), ("age", 34)]

dict = {
    "name": "alice",
    "mane": "luxurious",
    "age": 34
}


def find_in_list(reference, lst):
    vals = []

    for ref in reference:
        for key, val in lst:
            if ref == key:
                vals.append(val)

    return vals


def find_in_dict(reference, dict):
    vals = []

    for ref in reference:
        if ref in dict:
            vals.append(dict[ref])

    return vals


print(find_in_list(reference, lst))
print(find_in_dict(reference, dict))
