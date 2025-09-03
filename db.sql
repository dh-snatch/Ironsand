CREATE TABLE DEPOSIT(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    rock_type VARCHAR(50) NOT NULL,
    description TEXT,
    date_discovered DATE NOT NULL
);