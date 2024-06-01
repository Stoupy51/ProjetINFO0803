
-- Création de la base de données
CREATE DATABASE projet_803;
USE projet_803;

-- Création de l'utilisateur web_api
CREATE USER 'web_api'@'%' IDENTIFIED WITH caching_sha2_password BY 'projet_803_password';
GRANT ALL PRIVILEGES ON projet_803.* TO 'web_api'@'%';

-- Création de la table contacts
CREATE TABLE contacts (
    prenom VARCHAR(50),
    nom VARCHAR(50),
    email VARCHAR(100),
    attributs VARCHAR(1024),
    CONSTRAINT PK_Contacts PRIMARY KEY (prenom,nom)
);

-- Insertion des données
INSERT INTO contacts (prenom, nom, email, attributs) VALUES 
	('Justin', 'Case', 'justincase@smtwent.bad', '{"employeur": "TrustUS", "poste": "Responsable communication"}'),
	('Bob', 'Bobby', 'bobbobby@gmail.com', '{"employeur": "Gouvernement", "poste": "Directeur tres important", "info": "Je suis un peu plus important que le directeur"}'),
	('Alice', 'Liddell', 'liddell@mnms.fr', '{"employeur": "m&ms", "poste": "Developpeuse"}'),
	('David', 'Guetter', 'david.guetta@passesimple.fr', '{"employeur": "Passe Simple", "poste": "Responsable de la musique"}'),
	('Pierre', 'Feuille', 'pierre.feuille@ciseaux.fr', '{"employeur": "Jeu", "poste": "Responsable de la pierre"}');

