/* Create bob's microphone purchase 
and alice's spatula purchase in one single SQL statement */
INSERT INTO purchases (customer_id, item, quantity, cost)
VALUES 
(1, 'microphone', 1, 100),
(2, 'spatula', 5, 2);