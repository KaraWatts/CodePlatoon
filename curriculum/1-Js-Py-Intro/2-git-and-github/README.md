# Intro to Version Control with Git and Github

## What are we trying to accomplish?

By the end of this lecture you'll understand how to use the command-line program Git (`git`) to manage changes to a project in a way that allows you to keep track of those changes and roll them back if necessary - a process known as _version control_. Additionally, you'll learn how to integrate Git with the website Github so they changes will be backed up on the internet for the sake of posterity and making it easier to visually explore your project.

*Version control software* is critically important for modern software development. In addition to tracking changes and safely being able to "undo" work, it also lets you safely collaborate on the same codebase with others without causing problems (or "conflicts") for each other, and manage and share different variations of your codebase.

*[Git](https://git-scm.com/)* is one of the most popular version-control tools and some understanding of it is a pre-requisite for every software engineer, regardless of your level of experience. Git was created by Linus Torvaldis, the creator of Linux, to help manage the challenges of a remote, distributed team. It has become widely used, especially in the open-source community. We will focus on git and github in this course. Some other version control tools are [Mercurial](https://www.mercurial-scm.org/) and [SVN](https://www.perforce.com/blog/vcs/what-svn). Learning git will also prepare you to use these other tools if you encounter them in your career.

## Lectures & Assignment

- [Lesson - Git Fundamentals](./1-git-fundamentals.md)
  - [Assignment - Git Practice](https://github.com/Code-Platoon-Assignments/git-practice)
  - [Assignment - Learn Git Branching (Introduction Sequence, 1-3)](http://learngitbranching.js.org/) (this is a good resource to know about if you want to get deeper into `git`)
- [Lesson - Github Fundamentals](./2-github-fundamentals.md)
  - [Github Practice](https://github.com/Code-Platoon-Assignments/github-practice)
  - [Stretch Assignment - Group Project - Experiment with collaborating on a github repo](https://github.com/Code-Platoon-Assignments/Git-Group-Project/tree/main)

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!

## Terminal Learning Objectives

- Clone an existing Github repo to create a local copy
- Link a local git repo to any 'remote' repo (including one we just created on Github) by changing the remote url
- Push local changes to a remote repo
- Pull remote changes to keep the local repo in sync

## Enabling Learning Objectives

- Understand the essential git workflow
  - Checking the 'status' of your git repo
  - Staging untracked files to make git aware of the changes
  - Commiting staged/tracked files into a unique changeset & pushing that commit to a remote repo.
- Understand the concept of 'branches'
  - Understand how to create a new branch
  - Understand how to switch between branches
- Upgrading a regular folder into a Git repository
- Understand how to fork an existing Github repo
