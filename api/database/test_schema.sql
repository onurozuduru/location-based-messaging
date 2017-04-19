CREATE TABLE items (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR NOT NULL, 
	password VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
CREATE TABLE messages (
	id INTEGER NOT NULL, 
	sender INTEGER, 
	message VARCHAR, 
	timestamp DATETIME, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sender) REFERENCES users (id)
);
CREATE TABLE items_owned (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	item_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(item_id) REFERENCES items (id)
);
CREATE TABLE messages_found (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	message_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(message_id) REFERENCES messages (id)
);
