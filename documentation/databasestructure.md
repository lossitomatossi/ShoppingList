# Create table statements:
```
CREATE TABLE list (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	info VARCHAR(144),
	account_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
```
CREATE TABLE account (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	username VARCHAR(144) NOT NULL,
	password VARCHAR(144) NOT NULL,
	role VARCHAR(30) NOT NULL,
	PRIMARY KEY (id)
);
```
```
CREATE TABLE category (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	PRIMARY KEY (id)
);
```
```
CREATE TABLE item (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	amount INTEGER,
	bought BOOLEAN NOT NULL,
	account_id INTEGER NOT NULL,
	category_id INTEGER NOT NULL,
	list_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	CHECK (bought IN (0, 1)),
	FOREIGN KEY(account_id) REFERENCES account (id),
	FOREIGN KEY(category_id) REFERENCES category (id),
	FOREIGN KEY(list_id) REFERENCES list (id)
);
```
