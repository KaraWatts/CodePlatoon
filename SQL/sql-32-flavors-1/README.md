# SQL: 32 Flavors Ice Cream Shoppe

The ancient and vaguely magical Ye Olde 32 Flavors Ice Cream Shoppe has had a meltdown. All of their records, which they kept in thick vellum books that looked suspiciously like something a wizard might write their spells in, are ruined.

Luckily the owner of the Shoppe, Daldus Bumbledore, had already decided that the store was overdue for a new kind of magic, and that all of their records should be moved over to computers.

You have been hired to develop the software 32 Flavors will use to manage sales, inventory, and employees. They currently only have one location, which is mysteriously hard to find, but they have plans to open franchises nationwide in the near future.

## Diagrams

Use either [QuickDatabaseDiagrams](https://www.quickdatabasediagrams.com/) or [DrawSQL](https://drawsql.app) to help design your data schema.

It is fine to use a different tool if you prefer, but these are ones we like.

## 32 Flavors: Modeling an ice cream store

Your first task is to create a data model. Mr. Bumbledore has indicated that he cares about the following:

### Inventory

He likes to keep it simple. Inventory only consists of:

- Buckets of Ice Cream
- Boxes of Ice Cream Cones (Boxes of Cones)

### Sales

Sales are also simple. 32 Flavors sells one product:

- Ice cream cone

They have many different flavors and even offer *dairy-free* ice cream! Your ice cream comes in a waffle cone, a sugar cone, or, just for kids, [a cake cone](https://www.webstaurantstore.com/guide/678/types-of-ice-cream-cones.html). They've even got *gluten-free* varieties of all their cones!

### Employees & Hours

There is currently only one store and all the employees work there. Mr. Bumbledore is mainly interested in tracking *who works there*, as employees always seem to be disappearing and reappearing, and, their *hours*, or *timesheets.*

Right now everyone pretty much does the same thing - scoop ice cream - but in the future that may change.

## Tasks

This assignment is broken into stages. For each stage you'll need to do the following:

1. Using everything you have learned, create a database model/schema diagram for the scenario. **This is open-ended, so, you will have to make some design decisions.**

2. Using everything you have learned, turn your diagram into a Postgres data schema (including mock data).

*Recommendation: You may want to create different git branches for each stage, so you can easily refer back to your previous work.*

## Stage 1

Currently there is only  one store, so, don't worry about multiple locations (yet). Mr. Bumbledore says he wants to keep it simple, and, since he did a little bit of programming in his early days, suggested you:

- Keep inventory simple and treat Buckets of Ice Cream and Boxes of Cones as two separate entities
- Keep it as simple as you can with employees/hours and sales.


## Stage 2

Exciting news! 32 Flavors has opened up a second, and a third, location! Two of them are even in the same state, and, since the employees seem to be able to move very, very quickly (almost as if they're somehow flying) from Point A to Point B, **several of them are now working at multiple stores**. Model this using what you've learned about constraints and relationships.

## Stage 3

Mr. Bumbledore wants to institute a Customer Loyalty program, where customers who buy a certain amount of ice cream get a special prize.

Also, with all these stores, he's begun promoting some employees to be store managers. He wants each store to always have a manager.

He is very pleased with the work you've done, but would like to see the system tested out with some fake data. Use ChatGPT to generate:

- A minimum of 3 different store locations.
- A minimum of 3 employees working at each store (overlap is OK), including 1 and only 1 manager per store.
- At least one timesheet entry (hours worked) for each employee.
- Some inventory.
- At least 1 customer per store making at least 1 purchase.

He'd also like SQL queries to find:
- Number of employee hours worked per store
- Number of purchases per store
- Profit (amount of money made) per store from customer purchases
