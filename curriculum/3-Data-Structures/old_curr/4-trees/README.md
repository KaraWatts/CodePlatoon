# Trees

## Instructor Notes & Prerequesites

Prequesites are Big O, recursion, and other data structures like stacks, queues, possibly linked lists, so that implementing a tree can build on those skills already practiced for the others.

## What are we trying to accomplish?

There is a decent chance that if you get a data structures question in a tech interview, it might involve a tree.

Trees are one of the classic introductory data structures, in addition stacks and queues and linked lists, and are used all the time. A filesystem is a tree. [The DOM is a tree as you can see in this excellent visualizer here](https://bioub.github.io/dom-visualizer/).

Trees also can tie together many of the concepts - recursion, big-o, and building data structures - quite nicely.

You will learn what a tree is and why it is so useful. You will specifically learn about a binary tree. You will learn a few real-world use cases of a tree data structure that you're familiar with.

You will learn about the very powerful concept of a binary search.

## Lectures & Assignments

- Lecture: [Binary Trees & Recursion](./binary-trees-and-recursion.md)

  - Assignment: [Use this visualization tool and spend 10-15 playing with adding nodes to a Binary Search Tree](https://cmps-people.ok.ubc.ca/ylucet/DS/Algorithms.html)

  - Assignment: [Binary Search - Search Insert Position](https://leetcode.com/problems/search-insert-position/) (you may have done this already, but can now solve it with the `O(log n))` solution)

  - Assignment: [Binary Tree - Maximum Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/). The main idea here is that you can 'descend' the tree to the bottom using recursion and 'bubble up' the answer using return statements.

  - Assignment: Read [How Data Structures are actually used in the industry](https://blog.pragmaticengineer.com/data-structures-and-algorithms-i-actually-used-day-to-day/amp/). There is a focus on trees. **Do not skip this.**

## TLO's (Testable Learning Objectives)

- Able to implement a binary tree.
  - Able to add a node to the tree in sorted order.

## ELO's (Elective Learning Objectives)

- Able to explain the difference between a Tree and a Binary Tree.
- Able to give at least one real-world use case of a Tree.
- Able to explain the difference between breadth-first search (BFS) and depth-first-search (DFS)
