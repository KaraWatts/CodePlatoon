# Game Store III

Utilizing the provided `csv` data and the provided `sql` file for the Game Store project. Take into account the following considerations and apply the appropriate constraints.

- Action Figure
  - action_figure_title: Should only accept Title format, Chars, Integers, and a '-' within the input string, and it should be unique.
  - quantity: The store will always contain one copy in stock for display otherwise we have enough storage to hold up to 30 copies of each figure.
  - price: The minimum price we can afford without losing money is for an action figure to be sold at $10 and the maximum price we will ever charge will be $100.
- Employee
  - employee_name: All Employee names should be in title format and should not allow for special characters or integers
  - position: The only available positions within the store are Sales Associate, Store Manager, Inventory Clerk, Customer Service Representative, IT Specialist, Marketing Coordinator, Assistant Manager, Finance Analyst, Security Officer, HR Coordinator. No other input should be accepted.
  - salary: We will always pay above $16.66 an hour but we can't pay anything higher than $31.25 an hour.
- Poster
  - poster_title: Should be in title format, unique to every poster and should accept '-' as a special character.
  - quantity: We will always keep one item in stock and have enough storage to hold up to 30 of this item.
  - price: We will never charge more than $20 for a poster but we can't afford to go lower than $6.
