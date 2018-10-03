USE sakila;
-- 1a. Display the first and last names of all actors from the table actor.
SELECT first_name, last_name FROM actor;
-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT CONCAT(first_name, ' ', last_name) AS actor_name FROM actor;
-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'Joe';
-- 2b. Find all actors whose last name contain the letters GEN.
SELECT actor_id, first_name, last_name FROM actor WHERE last_name LIKE '%gen%';
-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order.
SELECT actor_id, last_name, first_name FROM actor WHERE last_name LIKE '%li%' ORDER BY last_name, first_name;
-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China.
SELECT country_id, country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');
-- 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, so create a column in the table actor named description and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).
ALTER TABLE actor ADD COLUMN description BLOB;
SELECT actor_id, description FROM actor LIMIT 5;
-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor DROP COLUMN description;
SELECT * FROM actor LIMIT 5;
-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(*) AS same_last_name_actors FROM actor GROUP BY last_name;
-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors.
SELECT last_name, COUNT(*) AS same_last_name_actors FROM actor GROUP BY last_name HAVING COUNT(*) > 1;
-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor SET first_name = 'HARPO' WHERE first_name = 'Groucho' AND last_name = 'Williams';
SELECT actor_id, first_name, last_name, last_update FROM actor WHERE first_name = 'Harpo'AND last_name = 'Williams';
-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor SET first_name = 'GROUCHO' WHERE first_name = 'Harpo' AND last_name = 'Williams';
SELECT actor_id, first_name, last_name, last_update FROM actor WHERE first_name = 'Groucho'AND last_name = 'Williams';
-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
CREATE TABLE IF NOT EXISTS address (
  address_id SMALLINT(5) UNSIGNED NOT NULL AUTO_INCREMENT,
  address VARCHAR(50) NOT NULL,
  address2 VARCHAR(50) DEFAULT NULL,
  district VARCHAR(20) NOT NULL,
  city_id SMALLINT(5) unsigned NOT NULL,
  postal_code VARCHAR(10) DEFAULT NULL,
  phone VARCHAR(20) NOT NULL,
  location GEOMETRY NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (address_id),
  KEY idx_fk_city_id (city_id),
  SPATIAL KEY idx_location (location),
  CONSTRAINT fk_address_city FOREIGN KEY (city_id) REFERENCES city (city_id) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8;
-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address.
SELECT s.first_name, s.last_name, a.address 
FROM staff s
LEFT JOIN address AS a on s.address_id = a.address_id;
-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
CREATE TEMPORARY TABLE aug05_payments
SELECT staff_id, SUM(amount) AS aug05_payment FROM payment WHERE MONTH(payment_date) = 8 AND YEAR(payment_date) = 2005 GROUP BY staff_id;
SELECT s.staff_id, s.first_name, s.last_name, p.aug05_payment
FROM staff s
LEFT JOIN aug05_payments AS p ON s.staff_id = p.staff_id;
DROP TABLE aug05_payments;
-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT f.film_id, f.title, fa.actor_count 
FROM film f
INNER JOIN (SELECT film_id, COUNT(*) AS actor_count FROM film_actor GROUP BY film_id) AS fa ON f.film_id = fa.film_id;
-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT COUNT(*) AS hi_copies_count FROM inventory WHERE film_id = (SELECT film_id FROM film WHERE title = 'Hunchback Impossible' LIMIT 1);
-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name.
SELECT c.customer_id,c.first_name, c.last_name, p.total_paid
FROM customer AS c
LEFT JOIN (SELECT customer_id, SUM(amount) AS total_paid FROM payment GROUP BY customer_id) AS p ON c.customer_id = p.customer_id
ORDER BY last_name;
-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT f.title
FROM film f
INNER JOIN language AS l ON f.language_id = l.language_id
WHERE (f.title LIKE 'K%' OR f.title LIKE 'Q%') AND l.name = 'English';
-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT a.actor_id, a.first_name, a.last_name
FROM actor AS a
INNER JOIN film_actor AS fa ON fa.actor_id = a.actor_id
INNER JOIN film AS f ON f.film_id = fa.film_id
WHERE f.title = 'Alone Trip';
-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT cs.first_name, cs.last_name, cs.email
FROM customer AS cs
INNER JOIN address AS a ON cs.address_id = a.address_id
INNER JOIN city AS ci ON a.city_id = ci.city_id
INNER JOIN country AS co ON ci.country_id = co.country_id
WHERE co.country = 'Canada';
-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.
SELECT f.film_id, f.title
FROM film AS f
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Family';
-- 7e. Display the most frequently rented movies in descending order.
SELECT f.title, r.rentals
FROM film f
INNER JOIN (SELECT i.film_id, COUNT(*) AS rentals
			FROM rental AS r
            INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
            GROUP BY i.film_id) AS r ON f.film_id = r.film_id
ORDER BY r.rentals DESC, title;
-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, r.total_earnings
FROM store AS s
INNER JOIN (SELECT store_id, SUM(p.amount) total_earnings
			FROM payment AS p
            INNER JOIN rental AS r ON p.rental_id = r.rental_id
            INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
            GROUP BY store_id) AS r ON s.store_id = r.store_id;
-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, ci.city, co.country
FROM store AS s
INNER JOIN address AS a ON s.address_id = a.address_id
INNER JOIN city AS ci ON a.city_id = ci.city_id
INNER JOIN country AS co ON ci.country_id = co.country_id;
-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT c.name, r.revenue
FROM category AS c
INNER JOIN (SELECT fc.category_id, SUM(p.amount) AS revenue
			FROM payment AS p
			INNER JOIN rental AS r ON p.rental_id = r.rental_id
			INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
			INNER JOIN film_category AS fc ON i.film_id = fc.film_id
			GROUP BY fc.category_id
			ORDER BY revenue DESC LIMIT 5) AS r ON c.category_id = r.category_id;
-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE OR REPLACE VIEW top_5_genres AS  SELECT c.name, r.revenue
										FROM category AS c
										INNER JOIN (SELECT fc.category_id, SUM(p.amount) revenue
													FROM payment AS p
													INNER JOIN rental AS r ON p.rental_id = r.rental_id
													INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
													INNER JOIN film_category AS fc ON i.film_id = fc.film_id
													GROUP BY fc.category_id
													ORDER BY revenue DESC LIMIT 5) AS r ON c.category_id = r.category_id;
-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top_5_genres;
-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW IF EXISTS top_5_genres;