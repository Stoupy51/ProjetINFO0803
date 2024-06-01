

# Vérification des arguments
import sys
if len(sys.argv) not in (6,7):
	print("Erreur d'utilisation, format :")
	print(sys.executable, sys.argv[0], "<database_ip> <database> <contact_table> <database_login> <database_password> [<api_port>]")
	sys.exit(1)
DATABASE_IP = sys.argv[1]
DATABASE_NAME = sys.argv[2]
CONTACT_TABLE = sys.argv[3]
LOGIN = sys.argv[4]
PASSWORD = sys.argv[5]
API_PORT = sys.argv[6] if len(sys.argv) == 7 else 5000

# Imports & constants
import time
import json
import pymysql
from flask import Flask, request, jsonify, Response

# Connexion à la base de données
DATABASE_CONNEXION = pymysql.connect(host=DATABASE_IP, user=LOGIN, password=PASSWORD, database=DATABASE_NAME)
CURSOR = DATABASE_CONNEXION.cursor()
print("Connexion à la base de données réussie")

# Création d'une instance de l'application Flask
app = Flask(__name__)

# Recevoir les ajout de contact
@app.route("/api/add", methods=["POST"])
def add_contact() -> tuple[Response, int]:
	
	# Récupération des données ({"nom": "nom", "prenom": "prenom", "email": "email", "attributs": {"employeur": "URCA", "poste": "prof", "resp": "Directeur"}})
	data = request.form
	nom = data.get("nom")
	prenom = data.get("prenom")
	email = data.get("email")
	attributs = data.get("attributs")
	if not nom:
		return jsonify({"error": "Nom manquant"}), 400
	if not prenom:
		return jsonify({"error": "Prénom manquant"}), 400
	if not email:
		return jsonify({"error": "Email manquant"}), 400
	if not attributs:
		return jsonify({"error": "Attributs manquants"}), 400
	try:
		attributs = json.loads(attributs)
	except:
		return jsonify({"error": "Attributs doit être un dictionnaire, actuellement : " + str(attributs)}), 400

	# Ajout du contact avec des bindings pour éviter les injections SQL
	CURSOR.execute(f"INSERT INTO {CONTACT_TABLE} (nom, prenom, email, attributs) VALUES (%s, %s, %s, %s)", (nom, prenom, email, json.dumps(attributs)))
	DATABASE_CONNEXION.commit()
	return jsonify({"success": "Contact ajouté"}), 200


# Recevoir les suppressions de contact
@app.route("/api/remove", methods=["POST"])
def remove_contact() -> tuple[Response, int]:
	
	# Récupération des données ({"nom": "nom", "prenom": "prenom"})
	data = request.form
	nom = data.get("nom")
	prenom = data.get("prenom")
	if not nom:
		return jsonify({"error": "Nom manquant"}), 400
	if not prenom:
		return jsonify({"error": "Prénom manquant"}), 400
	
	# Suppression du contact
	CURSOR.execute(f"DELETE FROM {CONTACT_TABLE} WHERE nom = %s AND prenom = %s", (nom, prenom))

	# Vérification de la suppression
	if CURSOR.rowcount == 0:
		return jsonify({"error": "Contact non trouvé"}), 404
	DATABASE_CONNEXION.commit()
	return jsonify({"success": "Contact supprimé"}), 200


# Recevoir les demandes d'affichage de tous les contacts ou à partir de critères
@app.route("/api/get", methods=["POST"])
def get_contacts() -> tuple[Response, int]:
	criteres = {}
	if request.form:
		criteres = request.form
		if not isinstance(criteres, dict):
			return jsonify({"error": "Les criteres doivent être un dictionnaire, ex: { 'nom':'Dupont','attributs':{'poste':'prof'} }"}), 400

	# Récupération des contacts
	query = f"SELECT * FROM {CONTACT_TABLE}"
	if len(criteres) > 0:
		query += " WHERE "
		for key, value in criteres.items():
			if key == "attributs":
				value = json.loads(value)	# Convert string to dict
				for key2, value2 in value.items():
					query += f'(attributs LIKE \'%"{key2}":"{value2}"%\' OR attributs LIKE \'%"{key2}": "{value2}"%\') AND'
			else:
				query += f"{key} = '{value}' AND"
		query = query[:-4]	# Remove last " AND"

	rows = []
	try:
		CURSOR.execute(query)
		rows = CURSOR.fetchall()
		column_names = [desc[0] for desc in CURSOR.description]
	except:
		pass
	contacts = []
	for row in rows:
		contact = {}
		for i, value in enumerate(row):
			contact[column_names[i]] = value
		contacts.append(contact)
	return jsonify(contacts), 200

# Exécution de l'application
if __name__ == "__main__":
	app.run("0.0.0.0", API_PORT)



