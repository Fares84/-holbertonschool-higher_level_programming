-- script that creates the table unique_id on MySQL server
-- with default and unique value
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
;
