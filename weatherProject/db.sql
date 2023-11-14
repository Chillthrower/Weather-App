-- Create user and set password
CREATE USER 'hello'@'%' IDENTIFIED BY '12345';

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS weather;

-- Grant all privileges to the user on the database
GRANT ALL PRIVILEGES ON weather.* TO 'hello'@'%';

-- Apply the changes and reload privileges
FLUSH PRIVILEGES;

-- Use the newly created database
USE weather;