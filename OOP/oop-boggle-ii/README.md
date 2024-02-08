# Boggle Challenge Part 2: Word Checker

## Summary
While real Boggle includes all words 3 letters or greater in a variety of combinations (i.e., you can zig zag through the board), we're just starting to learn Object Orientation. In this challenge, we are going to build off our last Boggle challenge by using our `BoggleBoard` generator to check the existence of a 4-letter word against our generated boggle board. Essentially, we need to get all 4-letter combinations of letters on the board (vertical, horizontal, diagonal - all forwards and backwards) and see if our 4-letter word that we pass in is on that board.

### Step 1: Pseudocode

Stop! I know what you're about to do. I've done it many times before. You're about to jump in to writing code.

![Admiral Ackbar from star wars saying its a trap](http://i.imgur.com/LaJ9Kmo.gif)

Instead, get out some paper and draw out a 4x4 Boggle Board. Fill it with letters (perhaps utilizing your brand-spanking new generator). Pick a gibberish word (makes it easier to check letter by letter) and check if it's on the board.

Reflect on your mental process. How did you do decide if the word was on the board or not?

Write your pseudocode for the algorithm.

### Step 2: Implement "BoggleBoard#include_word"
```python
board.include_word("pear") # => True or False
```

It's time to translate your pseudocode to Python.

What, if any, instance methods do you need to define? Would your algorithm be easier to write if your board were stored in a different way?

What are the tradeoffs between storing the board as a 4x4 array of arrays vs. a single 16 element array?

## Resources
* [Boggle on Wikipedia](http://en.wikipedia.org/wiki/Boggle)
* [Play Boggle online](http://www.wordplays.com/boggle)
