# Character Match Challenge

## Part 1

For this challenge you will make a program that takes in two different strings and see if the invidual letter or number characters in a string match in both strings. For example, 'abcde2' can be rearranged to 'c2abed'.

### Example
Your program should return true for all the following examples...
```
is_anagram('charm', 'march')
is_anagram('CharM', 'mARcH')
is_anagram('abcde2', 'c2abed')
```
### Remember
Run your test specs early and often. Also, if you come across a scenario that isn't included in your test suite, then you should absolutely add it!

### Challenge Yourself
* Solve this same exercise without using Python's built-in `sorted` method.

## Part 2

The goal of this exercise is to return a new list of all the anagrams from the provided list.

### Example
```
anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"]) == ["saltier", "realist", "retails"]
```

### Challenge Yourself
* Try to break your method up so that they only have a single job to do.
