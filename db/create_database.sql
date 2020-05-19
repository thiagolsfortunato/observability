CREATE DATABASE IF NOT EXISTS chat;

USE chat;

CREATE TABLE messages (
    id INT NOT NULL AUTO_INCREMENT,
    message VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT CONS_MESSAGE UNIQUE (message)
);

INSERT INTO messages SET message = 'msg1';
INSERT INTO messages SET message = 'msg2';
INSERT INTO messages SET message = 'msg3';
INSERT INTO messages SET message = 'msg4';
INSERT INTO messages SET message = 'msg5';
INSERT INTO messages SET message = 'msg6';
INSERT INTO messages SET message = 'msg7';
INSERT INTO messages SET message = 'msg8';
INSERT INTO messages SET message = 'msg9';
INSERT INTO messages SET message = 'msg10';
