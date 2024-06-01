CREATE DATABASE projet_803;
USE projet_803;

CREATE USER 'web_api'@'%' IDENTIFIED WITH caching_sha2_password BY 'projet_803_password';
GRANT ALL PRIVILEGES ON projet_803.* TO 'web_api'@'%';

CREATE TABLE contacts (
    prenom VARCHAR(50),
    nom VARCHAR(50),
    email VARCHAR(100),
    attributs VARCHAR(1024),
    CONSTRAINT PK_Contacts PRIMARY KEY (prenom,nom)
);

-- Insertion des données avec des blagues / jeu de mots
INSERT INTO contacts (prenom, nom, email, attributs) VALUES 
('Justin', 'Case', 'justincase@smtwent.bad', '{"employeur": "TrustUS", "poste": "Responsable communication"}'),
('Bob', 'Bobby', 'bobbobby@gmail.com', '{"employeur": "Gouvernement", "poste": "Directeur très important", "info": "Je suis un peu plus important que le directeur"}')
;
