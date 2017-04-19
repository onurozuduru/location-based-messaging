PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
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
INSERT INTO "users" VALUES(1,'example0','example0p');
INSERT INTO "users" VALUES(2,'example1','example1p');
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
INSERT INTO "messages" VALUES(1,2,'test1',NULL,1.0,2.2);
INSERT INTO "messages" VALUES(2,2,'test2',NULL,2.0,1.0);
INSERT INTO "messages" VALUES(3,2,'test2',NULL,5.0,1.0);
INSERT INTO "messages" VALUES(4,2,'test2',NULL,5.0,5.0);
INSERT INTO "messages" VALUES(5,2,'test2',NULL,1.0,5.0);
INSERT INTO "messages" VALUES(6,2,'test2',NULL,1.0,3.0);
INSERT INTO "messages" VALUES(7,2,'test2',NULL,-1.0,3.0);
INSERT INTO "messages" VALUES(8,2,'test2',NULL,-5.0,3.0);
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
COMMIT;
