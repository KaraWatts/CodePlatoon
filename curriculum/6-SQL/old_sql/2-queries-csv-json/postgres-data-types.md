# A Guide to Postgres Data Types

This is a guide to the most important data types along with general recommendations of how to handle different sorts of data in Postgres.

## Table of Contents

1. [Tradeoffs](#tradeoffs-space-vs-size-limits-and-the-cost-of-change)
2. [Character Types](#character-types)
3. [Numeric Types](#numeric-types)
4. [Monetary Type](#monetary-types)
5. [Date/Time Types](#datetime-types)
6. [Boolean Type](#boolean-type)

Postgres has [a lot of data types](https://www.postgresql.org/docs/current/datatype.html). They even have a [geometric type](https://www.postgresql.org/docs/current/datatype-geometric.html) for points and lines and shapes, a [UUID type](https://www.postgresql.org/docs/current/datatype-uuid.html), and a very, very powerful [JSON type](https://www.postgresql.org/docs/current/datatype-json.html).

While these more advanced data types are extremely powerful, 75% or more of a good data schema can be accomplished with the simpler and more common types you may already be familiar with. Those types will be the focus of our class.

### Tradeoffs: Space vs Size Limits, and The Cost of Change

Using data types that use the least amount of memory possible is important, especially for big database holding hundreds of millions of records.

At the same time, the data schema is one of the hardest things to change in a real software system: 

- It already has data in it
- All the other software depends on it and would have to be changed too.

While it is good to practice choosing the data type that uses the minimum amount of space, you also need to think about if the input size of your data gets bigger over time or has edge cases. Being conservative, and choosing a data type bigger than you need, *is sometimes a good real-world engineering practice*

Code tends to live a long time - what seems like a reasonable size today, may be too small twenty or fifty years from now. The classic example of this, though not having to do with databases per se, is the [Y2K Problem, where the U.S. spent billions of dollars preparing for the year 2000 because computer code written decades ago had only used two decimal places ("98" instead of "1998", and thus "00" would be "1900" -- not "2000") to store dates.](https://time.com/5752129/y2k-bug-history/)

### Character types

- `varchar(n)` is the variable-length character string.  With varchar(n),  you can store up to n characters.

- `text` is the variable-length character string that in theory has unlimited length.

- `varchar` without a number is exactly the same as `text`.

The [official Postgres recommendation](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_varchar.28n.29_by_default) is to use `text` or `varchar`, **not** `varchar(n)`. The reason is Postgres only takes up the space needed - the actual number of characters of the input. `varchar(n)` [may actually be slower](https://www.postgresql.org/docs/9.1/datatype-character.html) than `text` or `varchar`

### Numeric types

There are three kinds of integers in PostgreSQL:

- Small integer (`smallint`) is 2-byte signed integer that has a range from -32,768 to 32,767.
- Integer (`int`) is a 4-byte integer that has a range from -2,147,483,648 to 2,147,483,647.
- Serial is the same as integer except that PostgreSQL will *automatically generate and populate values into the `serial` column.* We've seen this `serial int` for **primary key** columns.

For integers, use `int`. it is a good trade off between storage and expressiveness for most applications.

If you need a floating-point number, use `numeric`. It represents the exact number, [unlike other floating-point types which can be a bit trickier](https://www.prisma.io/dataguide/postgresql/introduction-to-data-types#numbers-and-numeric-values).

### Monetary types

Postgres has a `money` type specifically for storing monetary values [but the official recommendation is not to use it](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_money). For money:

- Use `numeric`
- Store the currency in an adjacent column.

If you don't need to worry about fractions of cents, another strategy is to store the money value in cents with an integer type.

### Date/Time types

Dates, times, *and timezones* are notoriously tricky to deal with in programming. Consider:

- What is your server timezone set to?
- What is your database server's timezone set to?
- What is the timezone of the user's browser?

For timestamps - [always use `timestamptz`](https://wiki.postgresql.org/wiki/Don't_Do_This#Date.2FTime_storage), [which converts from the user's timezone into UTC](https://community.spiceworks.com/topic/2454825-zone-of-misunderstanding). Here are [more good recommendations on Postgres timestamps](https://justatheory.com/2012/04/postgres-use-timestamptz/).

There is also a `date` type, which just stores a date, and `time`, which just stores a time.

Postgres also has an `interval` type [which stores an interval (duration) of time](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-interval/) (1.5 hours, 3 days, 23 minutes, etc)

Postgres has [lots of very helpful date/time functions](https://www.postgresql.org/docs/current/functions-datetime.html).

### Boolean Type

Boolean constants can be represented in SQL queries by the SQL key words TRUE, FALSE, and NULL.  For a `boolean` column, any of these inputs as strings can represent `TRUE`:

- true
- t
- yes
- on
- 1

and any of these can represent `FALSE`:

- false
- f
- no
- off
- 0

When writing queries the key words `TRUE` and `FALSE` [are preferred](https://www.postgresql.org/docs/current/datatype-boolean.html).

## References

- [Getting Started with Postgres Data Types](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/)

- [Postgres data types explained with examples](https://estuary.dev/postgresql-data-types/)
