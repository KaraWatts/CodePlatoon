# Queries and Joins

Certainly! Below are SQL queries that cover various aspects such as SELECT, *, SUM, AVG, AS, SORTED_BY, GROUP_BY, DESCEND, LEFT_JOIN, RIGHT_JOIN, JOIN, LIKE, IN, WHERE, and other essential queries in reference to the "games" and "genres" tables:

1. **Basic SELECT:**

   ```sql
   SELECT * FROM games;
   ```

2. **SELECT with Alias (AS):**

   ```sql
   SELECT game_title AS title, quantity AS stock FROM games;
   ```

3. **SUM and GROUP BY:**

   ```sql
   SELECT genre_id, SUM(quantity) AS total_stock
   FROM games
   GROUP BY genre_id;
   ```

4. **AVG and GROUP BY:**

   ```sql
   SELECT genre_id, AVG(price) AS avg_price
   FROM games
   GROUP BY genre_id;
   ```

5. **Sorted By and DESCEND:**

   ```sql
   SELECT game_title, quantity
   FROM games
   ORDER BY quantity DESC;
   ```

6. **LEFT JOIN:**

   ```sql
   SELECT game_title, quantity, genre_name
   FROM games
   LEFT JOIN genres ON games.genre_id = genres.genre_id;
   ```

7. **RIGHT JOIN:**
   ```sql
   SELECT game_title, quantity, genre_name
   FROM genres
   RIGHT JOIN games ON genres.genre_id = games.genre_id;
   ```

8. **INNER JOIN (JOIN):**
   ```sql
   SELECT game_title, quantity, genre_name
   FROM games
   INNER JOIN genres ON games.genre_id = genres.genre_id;
   ```

9. **LIKE:**
   ```sql
   SELECT game_title, quantity
   FROM games
   WHERE game_title LIKE 'Call%';
   ```

10. **IN:**

    ```sql
    SELECT game_title, quantity
    FROM games
    WHERE genre_id IN (1, 3, 5);
    ```

11. **Combining Conditions in WHERE:**

    ```sql
    SELECT game_title, quantity
    FROM games
    WHERE genre_id = 3 AND price > 50.00;
    ```

These queries cover a range of SQL operations including basic SELECT statements, aliases, aggregate functions (SUM, AVG), sorting, grouping, different types of joins (LEFT, RIGHT, INNER), filtering using LIKE, IN, and WHERE conditions. Adjust them based on your specific needs and table structures.
