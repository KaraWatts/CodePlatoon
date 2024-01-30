DROP TABLE IF EXISTS actors CASCADE;
CREATE TABLE actors (
  id serial PRIMARY KEY,
  name varchar(255) NOT NULL
);

DROP TABLE IF EXISTS films CASCADE;
CREATE TABLE films (
  id serial PRIMARY KEY,
  title varchar(255) NOT NULL
);

DROP TABLE IF EXISTS actor_film_association;
CREATE TABLE actor_film_association (
  id serial PRIMARY KEY,
  actor_id integer,
  film_id integer,
  CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id),
  CONSTRAINT fk_film FOREIGN KEY(film_id) REFERENCES films(id)
);

-- CONSTRAINT fk_lead_actor FOREIGN KEY(lead_actor_id) REFERENCES actors(id)


INSERT INTO actors (name) VALUES 
('Jason Momoa'), 
('Gal Gadot'), 
('Ben Affleck');

INSERT INTO films (title) VALUES 
('Aquaman'),
('Wonder Woman'),
('The Last Duel'),
('Justice League');

INSERT INTO actor_film_association (actor_id, film_id) VALUES
(1, 1),
(1, NULL),
(2, 2),
(3, 3),
(1, 4),
(2, 4),
(3, 4),
(NULL, 4);