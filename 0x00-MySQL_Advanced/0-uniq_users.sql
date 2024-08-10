-- creates a table, users, with the following requirements:
-- -> id (int, never null, autoincrement & primary key)
-- -> email (string, never null & unique)
-- -> name (string)
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMEMNT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
