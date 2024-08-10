-- creates a table, users, with the following requirements
-- -> id (int, never null, auto_increment, primary key)
-- -> email (string<255 chars>, never null, unique)
-- -> name (string <255 chars>)
-- -> country

CREATE TABLE IF NOT EXISTS users (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);
