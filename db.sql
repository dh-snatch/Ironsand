CREATE TABLE IF NOT EXISTS SAMPLE(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    rock_type VARCHAR(50) NOT NULL,
    description TEXT,
    date_discovered DATE NOT NULL
);

-- LLM generated sample data
INSERT INTO SAMPLE (name, latitude, longitude, rock_type, description, date_discovered) VALUES
('Cape Palliser Iron Sand', -41.6167, 175.2833, 'Iron Sand', 'Black sand rich in iron near Cape Palliser.', '2022-06-15'),
('Hokitika Greenstone', -42.7167, 170.9667, 'Pounamu', 'Famous greenstone deposits along the Hokitika River.', '2021-11-10'),
('Coromandel Gold Quartz', -36.8333, 175.5000, 'Quartz', 'Small gold-bearing quartz veins in Coromandel.', '2023-01-05'),
('Kauri Gum Beach', -36.8833, 174.5833, 'Fossil Resin', 'Ancient kauri resin deposits along the beach.', '2020-09-22'),
('Waipoua Sandstone', -35.1333, 173.8833, 'Sandstone', 'Exposed sandstone formations in Waipoua Forest.', '2022-03-18');