# Intro to Complexity Analysis

This is a good time to explain the basics of complexity analysis. Imagine for a moment we didn't have this property of contiguous + same sized slots. If that were the case we would need to walk from the beginning of the list and count the # of elements one at a time until we got to the fourth. This would be an example of a _linear time_ operation, or in Big-O terms: `O(N)`. This means that, if the array had length N (for any N), the _worst case scenario_ to find a specific index is N operations. So if our array was of size 1000 and we wanted to see the last element, we would need to look at 1000 elements before we got to the one we want to see.

Luckily this isn't the case though, because of those two properties, it's a simple math formula to reach the correct index in one operation. So for an array of size 1000, to get the 1000th element all we need to do is compute: `startAddress + index * sizeof(int)` and we can immediately jump to that element. This is called _constant time_, or `O(1)`. This is the best guarantee possible - it means no matter how big the size of the data, the time it takes to do the operation remains the same.

So in this case we would say the Array has a lookup complexity of `O(1)`. Note that different operations on a data structure can have different complexity guarantees. So consider the cases of adding or removing something from an array. Assuming you already had the room for it (no need to 'grow' the array):

- adding to the end - `O(1)`. Why? Jump to the last index, add one, put it there.
- adding to the beginning/middle - `O(N)`. Why? Will first need to copy every other element to the index next to it. Middle is just as bad as beginning because we are concerned with 'worst case' behavior.

> An important note: in traditional Arrays, the full size of the Array must be known when defining it. That isn't the case with JS or Python arrays, which you can add to indefinitely. How this actually works under the hood is that, when you try to add an element to an already full array in JS, behind the scenes it will double it's size in memory, copy over all the existing elements, and then add the next one. This is significant because in reality adding an element to an array, even to the end, is not necessarily `O(1)`.
