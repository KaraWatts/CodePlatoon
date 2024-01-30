
## Interview Cheatsheet & Review

### Bits, Bytes, and Binary
At the end of the day, all the code you write, whether it be Python, Java, Javascript, Cobol, etc., is translated into 0's and 1's (i.e., binary) because computers are electronics. Electronics have currents running through them and the currents are either on (1) or off (0). Information is stored on your computer using bits and bytes:
- Bits are 1's or 0's
- Bytes are made up of 8 bits (e.g., 10010101)

Binary looks like gibberish to the average person but is the way computers process information. Think about how we represent numbers. We actually only ever use the numbers 1-9 in any number. Once you get larger than 10, we combine the numbers 0-9 to create a new number and our brain calculates its true value. We're so used to this that it becomes commonplace for us.
- When we get past 9, we move to 10. We don't have a new symbol for 10, but just keep track of how many times we've gone past 9 and add that to the left of the 9 and move the 9 to a 0, giving us 10
- We do this over and over. This is called positional notation. We operate in a base 10 world because there are 10 digits we commonly deal with.

With that same line of logic, computers operate in a base 2 world because there are only 2 digits they deal with: 0 and 1. Every time we get to the end of our possible numbers, we have to add 1 to the left row and keep calculating. But because we are in Base 2 world, we compute the math a different way.
- For example: the number 1234 is ONE thousand, TWO hundreds, THREE tens, and FOUR ones. When you add those together: 1000 + 100 + 100 + 10 + 10 + 10 + 1 + 1 + 1 + 1 = One thousand two hundred and thirty four. 1234 is the numeric representation of that in Base 10 world.
- In Base 2 world, instead of starting with 1 and multiplying by ten (powers of 10) for each place in the number, we start at 1 and go in powers of 2. Rather than the column to the left of a number being worth 10 times the amount of that column you are on, the column to the left of a number is worth 2 times the amount of the column that you are on

Thus, the number 1234 is represented as 10011010010. 2^10 (1024) + 2^7 (128) + 2^6 (64) + 2^4 (16) + 2^1 (2)

If we were to add 0101 + 1000, what would you get? 13 because 0101 is 5 and 1000 is 8. Instead of calculating each number as base10, we can add straight down. Let's try 0110 and 0111:
```
  0110 (6)
+ 0111 (7)
-------
```
Starting from the right, 0+1 = 1 so we drop that down: XXX1

Next, 1+1 in the 2's place means that we have 2 2's, or 4. That is represented as 100. Add it to the beginning one and it's X101.

Continuing on, we have 1+1 in the 8's place or 2 4's or 8. That is represented as 1000. Adding it to the previous numbers, we have 1101 or 13 total.

### Memory, Memory Assignment, and Storage
Now that we know **how** information is stored on our machines, we have to ask **where** it is stored. There's two types of storage on your machine: persistent and temporary:

**Temporary Storage**
- Think of memory as a giant bookshelf that holds billions of books vertically
  - Each shelf is numbered (i.e., each bit of memory has a memory address)
  - Each shelf holds 1 byte or 8 bits (0's and 1's)
- Also known as RAM （Random Access Memory). Each computer has a limited amount of this. In today's modern computers, it's typically 4GB, 8GB, 16GB, and 32GB
  - Much less storage than true storage
- Data stored in memory is temporary as compared to data stored in persistent storage which is permanent
- Fast to retrieve data
- When you load an application, it takes a certain amount of space to run and is loaded into your RAM/memory
  - The more applications that are open, the less RAM/memory is available, and ultimately, that slows your computer
- Memory is attached to a memory controller, which is connected to a memory processor
- The controllers are able to read/write to RAM through a direct connection
- Processors also have caches where they store copies of the stuff you recently read into memory so it's more readily available
  - Generally when you ask for something in memory, it grabs the thing you want from the memory address it's sent from and also a bunch of _nearby_ memory addresses (generally because once you ask for one thing in memory, you typically want the things around it). This is all stored in the cache
- Your operating system will assign memory addresses and linearly increase the memory address based on what you are using
  - Example: a number is 32 bits or 4 bytes (32 / 8 = 4). Those 4 bytes are assigned 4 consecutive memory addressses via your operating system
- Once you declare a variable X, X is assigned to a memory address and the memory address assigned after that might belong to another variable Y, etc. If you try to add K to X, you actually need to copy X and then add the K to it, assigning the new value to an entirely new memory address because data is typically stored in consecutive memory addresses.
- When we store **integers** we use 4 or 8 bytes. 4 bytes is 32 bits, 8 bytes is 64 bits
- Arrays are stored as consecutive bytes, as are strings. When you add to an array, you generally need to take all of its contents, find free consecutive memory spaces, put the contents in those consecutive memory spaces, and add what you want.

**Persistent Storage**
- Found in many forms: Solid-State Drives (SSDs), Hard-Disk Drive (HDDs), etc.
- Data stored in storage is permanent as compared to data stored in memory is temporary
- Storage numbers are much larger than memory numbers because it's cheaper to produce storage than memory
- Slow to retrieve data, like going to get data from a filing cabinet
- HDDs are slower than SSDs because the disk literally spins for HDDs so there's no direct connection between bytes on disks to memory controllers. They literally need to move along the surface of a spinning disc
  - Imagine a record player vs. an MP3 player

# Data Structures
Data structures are ways of storing data on your computer. There are many popular data structures to be tested on in a coding interview. We'll go over a few, including:
  1. Linked Lists
  2. Arrays
  3. Stacks
  4. Queues
  5. Trees


### Linked Lists and Arrays
- Both of these data structures keep track of elements and keep things in order. The implementation of keeping that order is different.
- Linked Lists **do not** keep track of index. Arrays **do** keep track of index.
- Linked Lists are lists of objects (nodes) that are attached to each other. Each node has a value and a pointer to the next node
- Accessing an element in an array is O(1) / constant time because arrays keep track of indexes. Accessing an element in a linked list is O(n) / linear time because there is no index so you would need to traverse the list to get what you want

**Linked Lists**
- Used to store a collection of items. These items are generally called Nodes.
- Each item in a linked list has 2 attributes
  1. **data** - the content it's holding
  2. **next** - a pointer to the next item
- In general, linked lists go in one direction but not in the other
  - Doubly linked lists go in both directions. In that case, they have 3 attributes:
    1. **data** - the content it's holding
    2. **next** - a pointer to the next item
    3. **previous** - a pointer to the previous item
- Insertion/Removal from Linked Lists can be O(1) in it's best case scenario (i.e., adding to the front), O(n) in it's worst case scenario (i.e., adding to the back in a regular linked list)

**Arrays**
- We're already familiar with arrays. It's a data structure that holds elements (data) and it keeps track of order using indexes
- When you create an array, your computer looks for sequential memory addresses that have nothing in them. It'll reserve those sequential memory addresses so that you can put things in them. The reason behind lookups being O(1) is because your computer knows where the array starts. If you give it the index of the element you're looking for, it'll just add that number to the start of the array's memory address and get the element. Mathematical operators are O(1).
- Arrays are not efficient with insertion/deletion because once you delete an element or add an element somewhere (other than the end), you have to move/copy all other elements back or forward, meaning that it takes O(n) time in the worst-case scenario


### Stacks And Queues
Both of these abstract data types (i.e., you don't really ever use the Stack or Queue class in programming) are linear data structures (one thing comes after another) which are flexible with sizing.

**Stacks**
- Last in, first out (LIFO)
- Think of a stack of plates in your cupboard or a stack of pancakes
  - The last plate you stack is the first one you take out
  - The last pancake you stack is the first one you take off to eat

**Queues**
- First in, first out (FIFO)
- Think of a line of people waiting in line. The first person who showed up is the first person served
- Queues are made of many nodes. Nodes are a data structure with a value (the thing it contains) and a pointer to the next node.
- In a queue, you add things to the tail (end) of the list and remove things from the head (front) of the list
  - `Enqueue` is the term when you add to the end and `Dequeue` is the term when you remove from the beginning
- There's a concept of a **Deque**
  - Double ended queue
  - A queue that goes both ways. You can enqueue or dequeue from either end

### Trees
- Data structure with a **root** (top) node that breaks out into other nodes, called **child** nodes. If a child node has no children, then it's called a **leaf** node as it stops at the leaf.
- Most of the time when we talk about trees, we talk about binary trees
  - A binary tree is a tree where each node has no more than 2 child nodes, a left node and a right node, one of which could be null
