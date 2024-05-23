
# Vérification des arguments
import sys
if len(sys.argv) != 3:
	print("Erreur d'utilisation, format :")
	print(sys.executable, sys.argv[0], "<api_ip> <api_port>")
	sys.exit(1)
API_IP = sys.argv[1]
API_PORT = sys.argv[2]

# Import flask & constants
import requests
from flask import Flask, request, jsonify, Response, redirect
BASE_URL = f"http://{API_IP}:{API_PORT}"
API_GET = BASE_URL + "/api/get"
API_ADD = BASE_URL + "/api/add"
API_REMOVE = BASE_URL + "/api/remove"

# Création d'une instance de l'application Flask
app = Flask(__name__)

# Page principale: récupère toutes les informations
@app.route("/", methods=["GET"])
def home():
	contacts = []
	try:
		contacts = requests.post(API_GET).json()
	except:
		return "Erreur lors de la récupération des contacts", 500
	
	# Création de la page HTML
	html = """
<!DOCTYPE html>
<html>
	<head>
		<title>Contacts</title>
	</head>
	<body>
		<h1>Liste des contacts</h1>
		<ul>
"""
	for contact in contacts:
		remove_icon = "<a href='/remove?nom=" + contact["nom"] + "&prenom=" + contact["prenom"] + "'>❌</a>"
		html += "\t\t\t<li>" + str(contact) + remove_icon + "</li>\n"
	html += """
		</ul>
		<h2>Ajouter un contact</h2>
		<form method="POST" action="/add">
			<label for="nom">Nom:</label>
			<input type="text" id="nom" name="nom" required placeholder="Doe">
			<label for="prenom">Prénom:</label>
			<input type="text" id="prenom" name="prenom" required placeholder="John">
			<label for="email">Email:</label>
			<input type="email" id="email" name="email" required placeholder="john_doe@uwu.net">
			<label for="attributs">Attributs:</label>
			<input type="textarea" id="attributs" name="attributs" required placeholder='{"employeur": "URCA", "poste": "prof", "resp": "Directeur"}'>
			<button type="submit">Ajouter</button>
		</form>
	</body>
</html>
"""
	return html, 200

# Ajout d'un contact
@app.route("/add", methods=["POST"])
def add_contact():

	# Ajout du contact
	try:
		r = requests.post(API_ADD, data = request.form)
		if r.status_code != 200:
			return r.text + str(request.form), r.status_code
	except:
		return "Erreur lors de l'ajout du contact", 500
	
	# Reroute client to home page ("/")
	return redirect("/")


# Suppression d'un contact
@app.route("/remove", methods=["GET"])
def remove_contact():
	nom = request.args.get("nom")
	prenom = request.args.get("prenom")
	if not nom:
		return "Nom manquant", 400
	if not prenom:
		return "Prénom manquant", 400

	# Suppression du contact
	try:
		r = requests.post(API_REMOVE, data = {"nom": nom, "prenom": prenom})
		if r.status_code != 200:
			return r.text, r.status_code
	except:
		return "Erreur lors de la suppression du contact", 500
	return redirect("/")

# Exécution de l'application
if __name__ == "__main__":
	app.run("0.0.0.0", 80)

