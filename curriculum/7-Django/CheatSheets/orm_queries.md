# Django ORM Queries and Their SQL Equivalents

In this markdown file, we will explore different methods for writing Django ORM queries and provide a more extensive explanation of each method, along with its SQL equivalent. Understanding these methods will help you interact with the database using Django's powerful Object-Relational Mapping (ORM) layer.

## 1. `all()`

- Django ORM: `Model.objects.all()`
- SQL Equivalent: `SELECT * FROM table_name;`
- Explanation: Retrieves all objects from the specified table. It returns a QuerySet that represents all the rows in the table.

## 2. `filter()`

- Django ORM: `Model.objects.filter(field=value)`
- SQL Equivalent: `SELECT * FROM table_name WHERE field=value;`
- Explanation: Filters the objects based on the specified condition. It retrieves a QuerySet containing objects that satisfy the condition.

## 3. `exclude()`

- Django ORM: `Model.objects.exclude(field=value)`
- SQL Equivalent: `SELECT * FROM table_name WHERE NOT field=value;`
- Explanation: Retrieves objects that do not match the specified condition. It returns a QuerySet excluding the objects that meet the condition.

## 4. `get()`

- Django ORM: `Model.objects.get(field=value)`
- SQL Equivalent: `SELECT * FROM table_name WHERE field=value LIMIT 1;`
- Explanation: Retrieves a single object that matches the specified condition. It throws a `Model.DoesNotExist` exception if multiple objects are found or none exist.

## 5. `first()`

- Django ORM: `Model.objects.first()`
- SQL Equivalent: `SELECT * FROM table_name LIMIT 1;`
- Explanation: Retrieves the first object from the table. It returns the first object found or `None` if no objects exist.

## 6. `last()`

- Django ORM: `Model.objects.last()`
- SQL Equivalent: `SELECT * FROM table_name ORDER BY id DESC LIMIT 1;`
- Explanation: Retrieves the last object from the table based on the primary key (assumes an incrementing `id` field). It returns the last object found or `None` if no objects exist.

## 7. `values()`

- Django ORM: `Model.objects.values('field1', 'field2')`
- SQL Equivalent: `SELECT field1, field2 FROM table_name;`
- Explanation: Retrieves specific fields' values from the table. It returns a QuerySet containing dictionaries with field-value pairs.

## 8. `order_by()`

- Django ORM: `Model.objects.order_by('field')`
- SQL Equivalent: `SELECT * FROM table_name ORDER BY field ASC;`
- Explanation: Retrieves objects sorted in ascending order based on the specified field. It returns a QuerySet with objects sorted accordingly.

## 9. `distinct()`

- Django ORM: `Model.objects.distinct()`
- SQL Equivalent: `SELECT DISTINCT * FROM table_name;`
- Explanation: Retrieves distinct objects from the table, removing duplicates. It returns a QuerySet containing distinct objects.

## 10. `annotate()`

- Django ORM: `Model.objects.annotate(field_alias=expression)`
- SQL Equivalent: Depends on the expression used.
- Explanation: Adds a computed field to each object based on the provided expression. It returns a QuerySet with the annotated field.

## 11. `count()`

- Django ORM: `Model.objects.count()`
- SQL Equivalent: `SELECT COUNT(*) FROM table_name;`
- Explanation: Retrieves the number of objects in the table. It returns an integer representing the count.

## 12. `exists()`

- Django ORM: `Model.objects.filter(field=value).exists()`
- SQL Equivalent: `SELECT 1 FROM table_name WHERE field=value LIMIT 1;`
- Explanation: Checks if any object exists in the table that matches the specified condition. It returns `True` if a matching object is found; otherwise, `False`.

## Conclusion

These are some of the common methods for writing Django ORM queries along with their SQL equivalents. Each method provides a different way to retrieve and manipulate data from the database. By utilizing these methods effectively, you can interact with the database and perform complex operations while leveraging the power and convenience of Django's ORM.
