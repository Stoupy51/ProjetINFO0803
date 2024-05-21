CREATE DATABASE projet_803;
USE projet_803;

CREATE USER 'web_api'@'%' IDENTIFIED WITH caching_sha2_password BY 'projet_803_password';
GRANT ALL PRIVILEGES ON projet_803.* TO 'web_api'@'%';

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(50),
    nom VARCHAR(50),
    email VARCHAR(100),
    attributs VARCHAR(1024)
);

INSERT INTO contacts (prenom, nom, email, attributs) VALUES ('John', 'Doe', 'john@example.com', '["employeur":"URCA","poste":"prof"]');
