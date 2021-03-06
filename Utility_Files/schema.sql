DROP DATABASE IF EXISTS scot;
CREATE DATABASE scot;

USE scot;

DROP TABLE IF EXISTS time_slices;
CREATE TABLE time_slices (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	start_year SMALLINT UNSIGNED NOT NULL,
	end_year SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS similar_words;
CREATE TABLE similar_words (
	word1 VARCHAR(64) NOT NULL,
	word2 VARCHAR(64) NOT NULL,
	score INT UNSIGNED NOT NULL,
	time_id INT UNSIGNED NOT NULL
);

CREATE INDEX word1_idx ON similar_words(word1);
CREATE INDEX word2_idx ON similar_words(word2);

CREATE INDEX time_id_idx ON similar_words(time_id);